/**
 * graph.js - D3.js Force-Directed Graph Visualisierung
 *
 * Hauptkomponente fuer die interaktive Zettel-Visualisierung.
 * Features:
 * - Force-directed Layout mit D3.js
 * - Canvas-Rendering fuer Performance
 * - Drag & Drop mit Positionsspeicherung
 * - Zoom & Pan
 * - Tag-basierte Filterung
 * - Suche mit Highlighting
 * - Detail-Panel bei Click
 */

// ============================================================================
// KONFIGURATION
// ============================================================================

const CONFIG = {
    // Knoten-Darstellung
    node: {
        radius: 24,
        color: '#3498db',
        highlightColor: '#2980b9',
        dimmedOpacity: 0.2,
        strokeColor: '#2c3e50',
        strokeWidth: 2,
        font: '12px sans-serif',
        textColor: '#2c3e50'
    },

    // Kanten-Darstellung
    link: {
        color: '#bdc3c7',
        highlightColor: '#7f8c8d',
        width: 1.5,
        dimmedOpacity: 0.1
    },

    // Force-Simulation
    force: {
        charge: -150,           // Abstossung zwischen Knoten (reduziert fuer kompakteres Layout)
        linkDistance: 60,       // Idealer Abstand zwischen verbundenen Knoten
        linkStrength: 0.5,      // Staerke der Verbindungs-Kraefte
        centerStrength: 0.1,    // Zentrierung (staerker fuer kompakteres Layout)
        collisionRadius: 26     // Kollisions-Radius (knapp ueber node.radius)
    },

    // Zoom
    zoom: {
        min: 0.3,
        max: 3.0,
        initial: 1.0
    },

    // Debounce fuer Position-Speicherung (ms)
    saveDebounce: 500
};


// ============================================================================
// STATE
// ============================================================================

const state = {
    // Daten
    nodes: [],
    links: [],
    nodeMap: new Map(),  // Schneller Zugriff: id -> node

    // D3 Objekte
    simulation: null,
    transform: d3.zoomIdentity,

    // Canvas
    canvas: null,
    ctx: null,
    width: 0,
    height: 0,

    // Interaktion
    hoveredNode: null,
    selectedNode: null,
    draggedNode: null,
    wasDragging: false,  // Verhindert Click nach Drag

    // Filter
    searchQuery: '',
    tagFilter: '',
    filteredNodeIds: new Set(),

    // Debounce Timer
    saveTimer: null
};


// ============================================================================
// INITIALISIERUNG
// ============================================================================

/**
 * Hauptinitialisierung - wird beim Laden der Seite ausgefuehrt.
 */
async function init() {
    setupCanvas();
    setupEventListeners();

    try {
        await loadData();
        await loadTags();
        await restoreState();
        startSimulation();
        render();
        hideLoading();
    } catch (error) {
        showError(error.message);
    }
}


/**
 * Canvas und Context einrichten.
 */
function setupCanvas() {
    state.canvas = document.getElementById('graph-canvas');
    state.ctx = state.canvas.getContext('2d');

    // Groesse an Container anpassen
    resizeCanvas();

    // High-DPI Support
    const dpr = window.devicePixelRatio || 1;
    state.canvas.width = state.width * dpr;
    state.canvas.height = state.height * dpr;
    state.ctx.scale(dpr, dpr);
    state.canvas.style.width = state.width + 'px';
    state.canvas.style.height = state.height + 'px';
}


/**
 * Canvas-Groesse an Container anpassen.
 */
function resizeCanvas() {
    const container = document.getElementById('graph-container');
    state.width = container.clientWidth;
    state.height = container.clientHeight;

    if (state.canvas) {
        const dpr = window.devicePixelRatio || 1;
        state.canvas.width = state.width * dpr;
        state.canvas.height = state.height * dpr;
        state.ctx.scale(dpr, dpr);
        state.canvas.style.width = state.width + 'px';
        state.canvas.style.height = state.height + 'px';

        render();
    }
}


// ============================================================================
// DATEN LADEN
// ============================================================================

/**
 * Graph-Daten vom Backend laden.
 */
async function loadData() {
    showLoading();

    const [graphData, positions] = await Promise.all([
        api.getGraph(),
        api.getPositions()
    ]);

    state.nodes = graphData.nodes;
    state.links = graphData.links;

    // Node-Map aufbauen
    state.nodeMap.clear();
    state.nodes.forEach(node => {
        state.nodeMap.set(node.id, node);
    });

    // Gespeicherte Positionen anwenden
    applyPositions(positions);

    // Filter zuruecksetzen
    state.filteredNodeIds = new Set(state.nodes.map(n => n.id));
}


/**
 * Gespeicherte Positionen auf Knoten anwenden.
 */
function applyPositions(positions) {
    let hasPositions = false;

    state.nodes.forEach(node => {
        if (positions[node.id]) {
            const pos = positions[node.id];
            node.x = pos.x;
            node.y = pos.y;
            node.fx = pos.fixiert ? pos.x : null;
            node.fy = pos.fixiert ? pos.y : null;
            hasPositions = true;
        } else {
            // Zufaellige Startposition falls keine gespeichert
            node.x = state.width / 2 + (Math.random() - 0.5) * 200;
            node.y = state.height / 2 + (Math.random() - 0.5) * 200;
        }
    });

    return hasPositions;
}


/**
 * Tags fuer Filter laden.
 */
async function loadTags() {
    try {
        const data = await api.getTags();
        const select = document.getElementById('tag-filter');

        data.tags.forEach(tag => {
            const option = document.createElement('option');
            option.value = tag;
            option.textContent = tag;
            select.appendChild(option);
        });
    } catch (error) {
        console.warn('Tags konnten nicht geladen werden:', error);
    }
}


/**
 * Gespeicherten State wiederherstellen.
 */
async function restoreState() {
    try {
        // Zoom wiederherstellen
        const zoomData = await api.getState('zoom');
        if (zoomData.value) {
            const zoom = parseFloat(zoomData.value);
            if (!isNaN(zoom)) {
                state.transform = state.transform.scale(zoom / state.transform.k);
                updateZoomDisplay();
            }
        }

        // Pan wiederherstellen
        const panData = await api.getState('pan');
        if (panData.value) {
            try {
                const pan = JSON.parse(panData.value);
                state.transform = d3.zoomIdentity
                    .translate(pan.x, pan.y)
                    .scale(state.transform.k);
            } catch (e) {
                // Ignorieren wenn JSON ungueltig
            }
        }

        // Filter wiederherstellen
        const filterData = await api.getState('filter');
        if (filterData.value) {
            document.getElementById('tag-filter').value = filterData.value;
            state.tagFilter = filterData.value;
            applyFilter();
        }
    } catch (error) {
        console.warn('State konnte nicht wiederhergestellt werden:', error);
    }
}


// ============================================================================
// D3 FORCE SIMULATION
// ============================================================================

/**
 * Force-Simulation starten.
 */
function startSimulation() {
    // Links auf Nodes mappen
    const linksCopy = state.links.map(link => ({
        source: state.nodeMap.get(link.source) || link.source,
        target: state.nodeMap.get(link.target) || link.target
    }));

    state.simulation = d3.forceSimulation(state.nodes)
        .force('link', d3.forceLink(linksCopy)
            .id(d => d.id)
            .distance(CONFIG.force.linkDistance)
            .strength(CONFIG.force.linkStrength))
        .force('charge', d3.forceManyBody()
            .strength(CONFIG.force.charge))
        .force('center', d3.forceCenter(state.width / 2, state.height / 2)
            .strength(CONFIG.force.centerStrength))
        .force('collision', d3.forceCollide()
            .radius(CONFIG.force.collisionRadius))
        .on('tick', render);

    // Links aktualisieren
    state.links = linksCopy;
}


// ============================================================================
// RENDERING
// ============================================================================

/**
 * Hauptrender-Funktion - zeichnet den gesamten Graphen.
 */
function render() {
    const ctx = state.ctx;
    const transform = state.transform;

    // Canvas leeren
    ctx.clearRect(0, 0, state.width, state.height);

    // Transformation anwenden
    ctx.save();
    ctx.translate(transform.x, transform.y);
    ctx.scale(transform.k, transform.k);

    // Kanten zeichnen
    drawLinks();

    // Knoten zeichnen
    drawNodes();

    ctx.restore();
}


/**
 * Kanten zeichnen.
 */
function drawLinks() {
    const ctx = state.ctx;

    state.links.forEach(link => {
        const source = link.source;
        const target = link.target;

        // Sichtbarkeit pruefen
        const sourceVisible = state.filteredNodeIds.has(source.id);
        const targetVisible = state.filteredNodeIds.has(target.id);

        if (!sourceVisible && !targetVisible) return;

        // Highlighting
        const isHighlighted = state.hoveredNode &&
            (source.id === state.hoveredNode.id || target.id === state.hoveredNode.id);

        ctx.beginPath();
        ctx.moveTo(source.x, source.y);
        ctx.lineTo(target.x, target.y);

        if (isHighlighted) {
            ctx.strokeStyle = CONFIG.link.highlightColor;
            ctx.lineWidth = CONFIG.link.width * 2;
        } else if (!sourceVisible || !targetVisible) {
            ctx.strokeStyle = CONFIG.link.color;
            ctx.globalAlpha = CONFIG.link.dimmedOpacity;
            ctx.lineWidth = CONFIG.link.width;
        } else {
            ctx.strokeStyle = CONFIG.link.color;
            ctx.lineWidth = CONFIG.link.width;
        }

        ctx.stroke();
        ctx.globalAlpha = 1;
    });
}


/**
 * Knoten zeichnen.
 */
function drawNodes() {
    const ctx = state.ctx;

    state.nodes.forEach(node => {
        const isVisible = state.filteredNodeIds.has(node.id);
        const isHovered = state.hoveredNode && state.hoveredNode.id === node.id;
        const isConnectedToHovered = state.hoveredNode && isConnected(node, state.hoveredNode);
        const matchesSearch = matchesSearchQuery(node);

        // Dimming bei Hover oder Filter
        let alpha = 1;
        if (state.hoveredNode && !isHovered && !isConnectedToHovered) {
            alpha = CONFIG.node.dimmedOpacity;
        }
        if (!isVisible) {
            alpha = CONFIG.node.dimmedOpacity;
        }

        ctx.globalAlpha = alpha;

        // Kreis zeichnen
        ctx.beginPath();
        ctx.arc(node.x, node.y, CONFIG.node.radius, 0, Math.PI * 2);

        // Fuellfarbe
        if (isHovered) {
            ctx.fillStyle = CONFIG.node.highlightColor;
        } else if (matchesSearch && state.searchQuery) {
            ctx.fillStyle = '#e74c3c';  // Rot fuer Suchergebnisse
        } else {
            ctx.fillStyle = CONFIG.node.color;
        }
        ctx.fill();

        // Rand
        ctx.strokeStyle = CONFIG.node.strokeColor;
        ctx.lineWidth = CONFIG.node.strokeWidth;
        ctx.stroke();

        // Titel zeichnen
        ctx.fillStyle = CONFIG.node.textColor;
        ctx.font = CONFIG.node.font;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';

        // Text kuerzen wenn zu lang
        const maxWidth = CONFIG.node.radius * 1.6;
        let title = node.title || node.id;
        if (ctx.measureText(title).width > maxWidth) {
            while (ctx.measureText(title + '...').width > maxWidth && title.length > 0) {
                title = title.slice(0, -1);
            }
            title += '...';
        }

        ctx.fillText(title, node.x, node.y);
        ctx.globalAlpha = 1;
    });
}


/**
 * Pruefen ob zwei Knoten verbunden sind.
 */
function isConnected(nodeA, nodeB) {
    return state.links.some(link =>
        (link.source.id === nodeA.id && link.target.id === nodeB.id) ||
        (link.source.id === nodeB.id && link.target.id === nodeA.id)
    );
}


/**
 * Pruefen ob Knoten zur Suchanfrage passt.
 */
function matchesSearchQuery(node) {
    if (!state.searchQuery) return true;

    const query = state.searchQuery.toLowerCase();
    return node.title.toLowerCase().includes(query) ||
           node.id.toLowerCase().includes(query);
}


// ============================================================================
// EVENT HANDLERS
// ============================================================================

/**
 * Alle Event-Listener einrichten.
 */
function setupEventListeners() {
    const canvas = state.canvas;

    // D3 Zoom - nur bei leerem Bereich, nicht auf Knoten
    state.zoomBehavior = d3.zoom()
        .scaleExtent([CONFIG.zoom.min, CONFIG.zoom.max])
        .filter(function(event) {
            // Zoom nur wenn kein Knoten unter dem Cursor
            const pos = getMousePositionFromEvent(event);
            const node = findNodeAtPosition(pos.x, pos.y);
            // Bei Wheel-Event immer zoomen, bei anderen Events nur wenn kein Knoten
            return event.type === 'wheel' || !node;
        })
        .on('zoom', handleZoom);

    d3.select(canvas).call(state.zoomBehavior);

    // D3 Drag fuer Knoten
    state.dragBehavior = d3.drag()
        .container(canvas)
        .subject(dragSubject)
        .on('start', dragStarted)
        .on('drag', dragged)
        .on('end', dragEnded);

    d3.select(canvas).call(state.dragBehavior);

    // Mouse Events (fuer Hover und Click)
    canvas.addEventListener('mousemove', handleMouseMove);
    canvas.addEventListener('click', handleClick);

    // Window Events
    window.addEventListener('resize', debounce(resizeCanvas, 200));

    // UI Controls
    document.getElementById('search').addEventListener('input', handleSearch);
    document.getElementById('tag-filter').addEventListener('change', handleTagFilter);
    document.getElementById('btn-reset').addEventListener('click', handleResetLayout);
    document.getElementById('btn-fit').addEventListener('click', handleFitView);
    document.getElementById('btn-retry').addEventListener('click', handleRetry);
    document.getElementById('close-panel').addEventListener('click', closeDetailPanel);

    // Keyboard
    document.addEventListener('keydown', handleKeyDown);
}


/**
 * Hilfsfunktion: Mouse-Position aus Event (fuer D3 filter)
 */
function getMousePositionFromEvent(event) {
    const rect = state.canvas.getBoundingClientRect();
    const x = (event.clientX || event.sourceEvent?.clientX || 0) - rect.left;
    const y = (event.clientY || event.sourceEvent?.clientY || 0) - rect.top;
    return {
        x: (x - state.transform.x) / state.transform.k,
        y: (y - state.transform.y) / state.transform.k
    };
}


/**
 * D3 Drag: Subject bestimmen (welcher Knoten wird gezogen?)
 */
function dragSubject(event) {
    const pos = getMousePositionFromEvent(event);
    const node = findNodeAtPosition(pos.x, pos.y);
    return node;
}


/**
 * D3 Drag: Start
 */
function dragStarted(event) {
    if (!event.subject) return;

    state.draggedNode = event.subject;
    state.wasDragging = false;  // Noch nicht wirklich gedraggt
    state.simulation.alphaTarget(0.3).restart();
    state.canvas.style.cursor = 'move';

    // Knoten fixieren
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
}


/**
 * D3 Drag: Waehrend des Ziehens
 */
function dragged(event) {
    if (!event.subject) return;

    state.wasDragging = true;  // Jetzt wird wirklich gedraggt

    // Position aus Event berechnen
    event.subject.fx = (event.sourceEvent.offsetX - state.transform.x) / state.transform.k;
    event.subject.fy = (event.sourceEvent.offsetY - state.transform.y) / state.transform.k;

    state.simulation.alpha(0.3).restart();
}


/**
 * D3 Drag: Ende
 */
function dragEnded(event) {
    if (!event.subject) return;

    state.simulation.alphaTarget(0);
    state.canvas.style.cursor = 'default';

    // Position bleibt fixiert und wird gespeichert
    savePosition(event.subject);
    state.draggedNode = null;
}


/**
 * Zoom-Handler.
 */
function handleZoom(event) {
    state.transform = event.transform;
    updateZoomDisplay();
    render();

    // State speichern (debounced)
    debouncedSaveState();
}


/**
 * Mouse Move Handler (nur fuer Hover/Tooltip).
 */
function handleMouseMove(event) {
    const pos = getMousePosition(event);
    const node = findNodeAtPosition(pos.x, pos.y);

    // Hover-State aktualisieren
    if (node !== state.hoveredNode) {
        state.hoveredNode = node;
        render();

        // Tooltip aktualisieren
        if (node) {
            showTooltip(node.title || node.id, event.clientX, event.clientY);
            if (!state.draggedNode) {
                state.canvas.style.cursor = 'pointer';
            }
        } else {
            hideTooltip();
            if (!state.draggedNode) {
                state.canvas.style.cursor = 'default';
            }
        }
    }
}


/**
 * Click Handler.
 */
function handleClick(event) {
    // Nur wenn kein Drag stattgefunden hat
    if (state.wasDragging) {
        state.wasDragging = false;
        return;
    }

    const pos = getMousePosition(event);
    const node = findNodeAtPosition(pos.x, pos.y);

    if (node) {
        state.selectedNode = node;
        showDetailPanel(node);
    }
}


/**
 * Search Handler.
 */
function handleSearch(event) {
    state.searchQuery = event.target.value;
    render();
}


/**
 * Tag Filter Handler.
 */
function handleTagFilter(event) {
    state.tagFilter = event.target.value;
    applyFilter();
    render();

    // State speichern
    api.saveState('filter', state.tagFilter).catch(console.warn);
}


/**
 * Filter anwenden.
 */
function applyFilter() {
    if (!state.tagFilter) {
        // Alle anzeigen
        state.filteredNodeIds = new Set(state.nodes.map(n => n.id));
    } else {
        // Nur Zettel mit diesem Tag
        state.filteredNodeIds = new Set(
            state.nodes
                .filter(n => n.tags && n.tags.includes(state.tagFilter))
                .map(n => n.id)
        );
    }
}


/**
 * Reset Layout Handler.
 */
async function handleResetLayout() {
    if (!confirm('Alle Positionen zuruecksetzen?')) return;

    try {
        await api.resetPositions();

        // Fixierungen loesen
        state.nodes.forEach(node => {
            node.fx = null;
            node.fy = null;
        });

        // Simulation neu starten
        state.simulation.alpha(1).restart();

    } catch (error) {
        showError('Fehler beim Zuruecksetzen: ' + error.message);
    }
}


/**
 * Fit View Handler.
 */
function handleFitView() {
    if (state.nodes.length === 0) return;

    // Bounding Box berechnen
    let minX = Infinity, maxX = -Infinity;
    let minY = Infinity, maxY = -Infinity;

    state.nodes.forEach(node => {
        minX = Math.min(minX, node.x);
        maxX = Math.max(maxX, node.x);
        minY = Math.min(minY, node.y);
        maxY = Math.max(maxY, node.y);
    });

    // Padding
    const padding = 50;
    minX -= padding;
    maxX += padding;
    minY -= padding;
    maxY += padding;

    // Zoom berechnen
    const graphWidth = maxX - minX;
    const graphHeight = maxY - minY;
    const scaleX = state.width / graphWidth;
    const scaleY = state.height / graphHeight;
    const scale = Math.min(scaleX, scaleY, CONFIG.zoom.max);

    // Zentrierung
    const centerX = (minX + maxX) / 2;
    const centerY = (minY + maxY) / 2;

    state.transform = d3.zoomIdentity
        .translate(state.width / 2, state.height / 2)
        .scale(scale)
        .translate(-centerX, -centerY);

    updateZoomDisplay();
    render();
    debouncedSaveState();
}


/**
 * Retry Handler.
 */
async function handleRetry() {
    hideError();
    try {
        await loadData();
        startSimulation();
        render();
        hideLoading();
    } catch (error) {
        showError(error.message);
    }
}


/**
 * Keyboard Handler.
 */
function handleKeyDown(event) {
    // ESC schliesst Detail-Panel
    if (event.key === 'Escape') {
        closeDetailPanel();
    }
}


// ============================================================================
// DETAIL PANEL
// ============================================================================

/**
 * Detail-Panel anzeigen.
 */
async function showDetailPanel(node) {
    try {
        const detail = await api.getZettelDetail(node.id);

        document.getElementById('detail-title').textContent = detail.title;
        document.getElementById('detail-id').textContent = 'ID: ' + detail.id;

        // Tags
        const tagsContainer = document.getElementById('detail-tags');
        tagsContainer.innerHTML = detail.tags
            .map(tag => `<span class="tag">${escapeHtml(tag)}</span>`)
            .join('');

        // Content (XSS-safe)
        document.getElementById('detail-content').textContent = detail.content;

        // Meta
        document.getElementById('detail-meta').textContent = detail.meta;

        // Links
        const linksList = document.getElementById('detail-links-list');
        linksList.innerHTML = detail.links
            .map(link => `<li><a href="#" data-id="${escapeHtml(link.id)}">${escapeHtml(link.title)}</a></li>`)
            .join('');

        // Click-Handler fuer Links
        linksList.querySelectorAll('a').forEach(a => {
            a.addEventListener('click', (e) => {
                e.preventDefault();
                const linkedNode = state.nodeMap.get(e.target.dataset.id);
                if (linkedNode) {
                    showDetailPanel(linkedNode);
                }
            });
        });

        // Panel einblenden
        document.getElementById('detail-panel').classList.add('visible');

    } catch (error) {
        console.error('Fehler beim Laden der Details:', error);
    }
}


/**
 * Detail-Panel schliessen.
 */
function closeDetailPanel() {
    document.getElementById('detail-panel').classList.remove('visible');
    state.selectedNode = null;
}


// ============================================================================
// HILFSFUNKTIONEN
// ============================================================================

/**
 * Mausposition in Graph-Koordinaten umrechnen.
 */
function getMousePosition(event) {
    const rect = state.canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Transform umkehren
    return {
        x: (x - state.transform.x) / state.transform.k,
        y: (y - state.transform.y) / state.transform.k
    };
}


/**
 * Knoten an Position finden.
 */
function findNodeAtPosition(x, y) {
    const radius = CONFIG.node.radius;

    for (let i = state.nodes.length - 1; i >= 0; i--) {
        const node = state.nodes[i];
        const dx = x - node.x;
        const dy = y - node.y;

        if (dx * dx + dy * dy < radius * radius) {
            return node;
        }
    }

    return null;
}


/**
 * Zoom-Anzeige aktualisieren.
 */
function updateZoomDisplay() {
    const percent = Math.round(state.transform.k * 100);
    document.getElementById('zoom-level').textContent = percent + '%';
}


/**
 * Position speichern (debounced).
 */
function savePosition(node) {
    clearTimeout(state.saveTimer);
    state.saveTimer = setTimeout(() => {
        api.savePosition(node.id, node.x, node.y).catch(console.warn);
    }, CONFIG.saveDebounce);
}


/**
 * State speichern (debounced).
 */
const debouncedSaveState = debounce(() => {
    api.saveState('zoom', state.transform.k.toString()).catch(console.warn);
    api.saveState('pan', JSON.stringify({
        x: state.transform.x,
        y: state.transform.y
    })).catch(console.warn);
}, CONFIG.saveDebounce);


/**
 * Debounce-Hilfsfunktion.
 */
function debounce(fn, delay) {
    let timer;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
    };
}


/**
 * HTML escapen (XSS-Schutz).
 */
function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}


/**
 * Loading anzeigen.
 */
function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
}


/**
 * Loading ausblenden.
 */
function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
}


/**
 * Fehler anzeigen.
 */
function showError(message) {
    hideLoading();
    document.getElementById('error-message').textContent = message;
    document.getElementById('error-box').classList.remove('hidden');
}


/**
 * Fehler ausblenden.
 */
function hideError() {
    document.getElementById('error-box').classList.add('hidden');
}


/**
 * Tooltip anzeigen.
 */
function showTooltip(text, x, y) {
    const tooltip = document.getElementById('tooltip');
    tooltip.textContent = text;
    tooltip.style.left = (x + 15) + 'px';
    tooltip.style.top = (y + 15) + 'px';
    tooltip.classList.remove('hidden');
}


/**
 * Tooltip ausblenden.
 */
function hideTooltip() {
    document.getElementById('tooltip').classList.add('hidden');
}


// ============================================================================
// START
// ============================================================================

// App starten wenn DOM bereit
document.addEventListener('DOMContentLoaded', init);
