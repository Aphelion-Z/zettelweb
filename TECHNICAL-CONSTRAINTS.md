# Technical Constraints & Stack Decisions

**Projekt:** ZettelWeb
**Version:** 2.0
**Datum:** 2025-11-04
**Autoren:** Team 7

---

## 📋 Übersicht

Dieses Dokument definiert die **technischen Rahmenbedingungen** für das ZettelWeb-Projekt, einschließlich:
- Technologie-Stack (Libraries, Tools)
- Architektur-Entscheidungen (mit Begründungen)
- Gegebene technische Einschränkungen (Zettelstore API, Browser-Umgebung)
- Deployment-Constraints

---

## 🏗️ Architektur-Pattern

### ✅ Client-Server / 3-Tier Architektur

**WICHTIG:** ZettelWeb ist eine **verteilte Web-Anwendung**, NICHT MVC!

```
┌─────────────────────────────────────────┐
│  TIER 1: Presentation (Browser)         │
│  - HTML/CSS/JavaScript                  │
│  - D3.js Graph Rendering                │
│  - User Interaction Handling            │
│  - LocalStorage für Positionen          │
└─────────────┬───────────────────────────┘
              │ HTTP/JSON (REST API)
              ▼
┌─────────────────────────────────────────┐
│  TIER 2: Application Logic (Optional)   │
│  - Falls benötigt: Node.js Backend      │
│  - Aktuell: NICHT vorhanden (Frontend-Only) │
└─────────────┬───────────────────────────┘
              │ HTTP/JSON
              ▼
┌─────────────────────────────────────────┐
│  TIER 3: Data (Zettelstore)             │
│  - Zettelstore REST API                 │
│  - Zettel-Inhalte, Metadaten, Links     │
│  - .zettel-Dateien (Persistenz)         │
└─────────────────────────────────────────┘
```

**Warum NICHT MVC?**
- Browser und Server sind **getrennte Prozesse** (kein gemeinsamer Speicher)
- Kommunikation über **zustandsloses HTTP** (keine direkten Objektreferenzen)
- View (Browser) kann Model (Server) nicht direkt kennen

**Referenz:** Siehe `aufgaben-erklaert/04-Strategischer-Entwurf-ERKLAERT.md` für detaillierte Erklärung.

---

## 🛠️ Technology Stack

### Frontend (Tier 1)

#### Core Technologies

**1. HTML5**
- Semantic HTML für Struktur
- Canvas-Element für Graph-Rendering
- Modals/Overlays für Zettel-Details

**2. CSS3**
- Moderne Layout (Flexbox/Grid)
- CSS Variables für Theme-Konsistenz
- Transitions für smooth UX

**3. JavaScript (ES6+)**
- Moderne Syntax (Arrow Functions, Destructuring, Modules)
- Async/Await für API-Calls
- Event-Driven Architecture

**Warum Vanilla JavaScript?**
- ✅ Keine Framework-Overhead (React/Vue/Angular)
- ✅ Team kennt JavaScript-Basics
- ✅ Direkter DOM-Zugriff für Performance
- ✅ D3.js arbeitet direkt mit DOM
- ❌ Aber: Manuelles State-Management nötig

**Alternative (falls Komplexität wächst):**
- **Svelte** (kompiliert zu Vanilla JS, minimaler Overhead)
- **React** (falls Komponenten-Architektur nötig)

---

#### Graph Visualization Library

**Entscheidung: D3.js v7**

**Begründung:**
```
✅ Force-Simulation out-of-the-box (forceSimulation, forceLink, forceManyBody)
✅ Barnes-Hut Approximation integriert (O(n log n) Performance)
✅ Flexibles API für Custom Layouts
✅ Große Community, viele Beispiele
✅ Gut dokumentiert (d3js.org)
✅ Keine eigene Physik-Engine schreiben nötig!
```

**Alternativen (abgelehnt):**

| Library | Pro | Contra | Warum abgelehnt? |
|---------|-----|--------|------------------|
| **Cytoscape.js** | Graph-spezialisiert, viele Layouts | Größere Library (~500KB) | D3 reicht, unnötiger Overhead |
| **Vis.js** | Einfaches API | Weniger Kontrolle, veraltetes Projekt | Community nicht mehr aktiv |
| **Three.js (WebGL)** | 3D-Graphen möglich | Sehr komplex, Overkill | 2D reicht, zu steile Lernkurve |
| **Eigene Implementierung** | Volle Kontrolle | 30+ Stunden nur für Physik | Scope-Sprengung, Rad neu erfinden |

**Code-Beispiel (D3.js Force Simulation):**
```javascript
const simulation = d3.forceSimulation(nodes)
  .force("link", d3.forceLink(links).id(d => d.id).distance(100))
  .force("charge", d3.forceManyBody().strength(-300))
  .force("center", d3.forceCenter(width / 2, height / 2))
  .force("collision", d3.forceCollide().radius(30))
  .on("tick", updatePositions);
```

**Ressourcen:**
- [D3 Force Simulation Dokumentation](https://github.com/d3/d3-force)
- [Observable: Force-Directed Graph Examples](https://observablehq.com/@d3/force-directed-graph)

---

#### Rendering Engine

**Entscheidung: HTML5 Canvas 2D**

**Begründung:**
```
✅ Performant für 200+ Objekte (Raster-basiert)
✅ Volle Kontrolle über Rendering-Loop
✅ Kompatibel mit D3.js (d3.select(canvas))
✅ Einfaches API (fillRect, arc, lineTo)
✅ RequestAnimationFrame für 60fps
```

**Canvas vs. SVG:**

| Kriterium | Canvas | SVG | Gewinner |
|-----------|--------|-----|----------|
| **Performance (200+ Objekte)** | ⚡ Sehr gut (keine DOM-Nodes) | 🐢 Langsam (jeder Zettel = DOM-Element) | Canvas |
| **Zoom/Pan** | ✋ Manuell (transform matrix) | ✅ Automatisch (CSS transform) | SVG |
| **Hit-Detection** | ✋ Manuell (Koordinaten-Berechnung) | ✅ Automatisch (event.target) | SVG |
| **Skalierbarkeit** | ❌ Pixel-basiert (Blur bei Zoom) | ✅ Vektor-basiert (immer scharf) | SVG |
| **Komplexität** | ✅ Einfach (weniger Code) | ✋ Mehr Code (SVG-Manipulation) | Canvas |

**Fazit:** Canvas gewinnt wegen **Performance-Anforderung** (NFR-1: 200@30fps).

**Optimierungen:**
- **Viewport Culling:** Nur sichtbare Zettel rendern
- **Dirty Regions:** Nur geänderte Bereiche neu zeichnen
- **OffscreenCanvas:** Background-Rendering (Web Workers)

**Code-Beispiel (Render Loop):**
```javascript
function render() {
  ctx.clearRect(0, 0, width, height);

  // Render links
  links.forEach(link => {
    ctx.beginPath();
    ctx.moveTo(link.source.x, link.source.y);
    ctx.lineTo(link.target.x, link.target.y);
    ctx.stroke();
  });

  // Render nodes (only visible ones)
  nodes.filter(isInViewport).forEach(node => {
    ctx.beginPath();
    ctx.arc(node.x, node.y, radius, 0, 2 * Math.PI);
    ctx.fill();
  });

  requestAnimationFrame(render);
}
```

---

#### Data Persistence

**Entscheidung: LocalStorage (primär) + IndexedDB (fallback)**

**WICHTIG:** Nicht SQLite! SQLite läuft NICHT im Browser!

**LocalStorage:**
```
✅ Einfaches Key-Value API
✅ Synchronous (keine Promises)
✅ ~5-10MB Speicher (ausreichend für Positionen)
✅ Automatisch persistent (überdauert Browser-Neustarts)
❌ Nur Strings (JSON.stringify nötig)
❌ Blocking (aber schnell genug für unsere Daten)
```

**IndexedDB (Fallback):**
```
✅ Größerer Speicher (~50MB+)
✅ Strukturierte Daten (kein JSON-Parsing)
❌ Asynchrones API (komplexer)
❌ Overkill für unseren Use-Case
```

**Datenschema (LocalStorage):**
```json
{
  "version": "1.0",
  "lastUpdated": "2025-11-04T14:23:45Z",
  "positions": {
    "20251027134512": { "x": 450.5, "y": 320.8 },
    "20251028091234": { "x": 120.0, "y": 500.3 }
  },
  "state": {
    "zoom": 1.5,
    "pan": { "x": 100, "y": 200 },
    "filter": ["#projekt", "#wichtig"]
  }
}
```

**Code-Beispiel:**
```javascript
// Save
const data = { positions, state };
localStorage.setItem('zettelweb-graph', JSON.stringify(data));

// Load
const savedData = JSON.parse(localStorage.getItem('zettelweb-graph') || '{}');
```

**Warum NICHT SQLite?**
- SQLite ist eine **native Library** (C/C++)
- Browser können KEINE nativen Libraries laden
- Alternative: sql.js (SQLite kompiliert zu WebAssembly) → aber Overkill

---

#### Markdown Rendering

**Entscheidung: marked.js**

**Begründung:**
```
✅ Leichtgewichtig (~10KB minified)
✅ CommonMark-konform
✅ Einfaches API: marked.parse(markdown)
✅ Kein jQuery benötigt
✅ XSS-Schutz integriert (sanitize option)
```

**Alternative:**
- **markdown-it** (größer, mehr Features)
- **Showdown** (veraltetes Projekt)

**Code-Beispiel:**
```javascript
import { marked } from 'https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js';

const html = marked.parse(zettel.content, {
  sanitize: true,  // XSS-Schutz
  breaks: true     // Newlines → <br>
});
```

---

### Backend (Tier 2)

**Aktuell: NICHT VORHANDEN**

ZettelWeb ist eine **Frontend-Only Anwendung**:
- Direkte API-Calls von Browser zu Zettelstore
- Kein eigener Server nötig

**Mögliche Szenarien für Backend:**

| Szenario | Lösung | Benötigt Backend? |
|----------|--------|-------------------|
| Zettelstore auf localhost | Direkt von Browser | ❌ Nein |
| Zettelstore remote (gleiches Origin) | Direkt von Browser | ❌ Nein |
| Zettelstore remote (CORS-Problem) | Proxy-Server | ✅ Ja (Node.js) |
| Erweiterte Features (Multi-User) | Backend mit DB | ✅ Ja (Express + DB) |

**Falls Backend nötig (CORS-Proxy):**
```javascript
// server.js (Node.js + Express)
const express = require('express');
const app = express();

app.get('/api/zettel', async (req, res) => {
  const response = await fetch('http://zettelstore:23123/z');
  const data = await response.json();
  res.json(data);
});

app.listen(3000);
```

---

### Data Source (Tier 3)

**Zettelstore REST API**

**API-Endpunkte (relevant für ZettelWeb):**

| Endpunkt | Methode | Beschreibung | Benötigt? |
|----------|---------|--------------|-----------|
| `/z` | GET | Alle Zettel (Liste mit IDs) | ✅ Ja |
| `/z/{id}` | GET | Einzelner Zettel (voller Inhalt) | ✅ Ja |
| `/z?q={query}` | GET | Zettel-Suche | 🟡 Optional (FR-3.1) |

**Datenformat (Beispiel /z/{id}):**
```json
{
  "id": "20251027134512",
  "meta": {
    "title": "Force-Directed Graphs",
    "tags": "#graphentheorie #visualisierung",
    "role": "zettel",
    "syntax": "markdown"
  },
  "content": "# Force-Directed Graphs\n\nPhysik-basierte Layout-Algorithmen...",
  "links": [
    { "id": "20251028091234", "type": "link" }
  ]
}
```

**API-Client (Wrapper-Klasse):**
```javascript
class ZettelstoreClient {
  constructor(baseURL) {
    this.baseURL = baseURL;
  }

  async fetchAll() {
    const response = await fetch(`${this.baseURL}/z`);
    return response.json();
  }

  async fetchById(id) {
    const response = await fetch(`${this.baseURL}/z/${id}`);
    return response.json();
  }

  async search(query) {
    const response = await fetch(`${this.baseURL}/z?q=${encodeURIComponent(query)}`);
    return response.json();
  }
}
```

---

## 🔒 Gegebene Einschränkungen

### 1. Browser-Kompatibilität (NFR-2)

**Unterstützte Browser:**
- Chrome/Edge (Chromium-basiert) ≥90
- Firefox ≥88
- Safari ≥14

**Erforderliche Browser-Features:**
- Canvas 2D API
- ES6+ (Modules, Arrow Functions, Async/Await)
- LocalStorage
- Fetch API
- RequestAnimationFrame

**NICHT unterstützt:**
- Internet Explorer (End-of-Life)
- Alte Mobile-Browser (<2020)

---

### 2. Zettelstore-Abhängigkeit

**ZettelWeb funktioniert NUR, wenn:**
```
✅ Zettelstore läuft und erreichbar ist (localhost oder remote)
✅ REST API aktiviert ist (Standard-Port: 23123)
✅ CORS-Header korrekt gesetzt (falls remote)
```

**Fehler-Szenarien:**
```
❌ Zettelstore offline → Fehlermeldung "Zettelstore nicht erreichbar"
❌ API-Änderung → Breaking Changes (abhängig von Zettelstore-Version)
❌ CORS-Blockierung → Browser-Fehler (Proxy-Server nötig)
```

**Versionierung:**
- Zettelstore API ist **nicht versioniert** (Rolling Release)
- ZettelWeb entwickelt gegen: **Zettelstore v0.17+**
- Bei Breaking Changes: Update erforderlich

---

### 3. Performance-Budget

**Anforderungen (NFR-1):**
- 200 Zettel @ 30fps
- Initial Render <3s
- Interaktions-Latenz <100ms

**Budget pro Frame (33ms @ 30fps):**
```
- Physik-Update:     max. 10ms
- Canvas-Rendering:  max. 6ms
- Hit-Detection:     max. 2ms
- Event-Handling:    max. 2ms
- Browser-Overhead:  ~13ms
─────────────────────────────
GESAMT:              33ms (30fps)
```

**Optimierungs-Strategie:**
1. **Physik:** Barnes-Hut Approximation (D3.js)
2. **Rendering:** Viewport Culling, Dirty Regions
3. **Events:** Debouncing, Throttling
4. **Speicher:** Object Pooling (Garbage Collection reduzieren)

---

### 4. Keine serverseitige Persistenz

**Einschränkung:** Positionen werden NUR im Browser gespeichert.

**Konsequenzen:**
```
❌ Keine Synchronisierung zwischen Geräten
❌ Cache-Löschung → Positionen verloren
❌ Anderer Browser → Positionen verloren
❌ Inkognito-Modus → Keine Persistenz
```

**Workaround:**
- Export/Import-Feature (JSON-Download) → würde manuelle Übertragung ermöglichen (nicht in v1.0)

---

## 📦 Dependencies (npm)

**package.json (Minimal):**
```json
{
  "name": "zettelweb",
  "version": "1.0.0",
  "type": "module",
  "dependencies": {
    "d3": "^7.8.5",
    "marked": "^11.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "eslint": "^8.54.0"
  }
}
```

**Warum Vite?**
- ⚡ Schneller Dev-Server (ES Modules)
- 📦 Einfaches Bundling (Rollup-basiert)
- 🔥 Hot Module Replacement
- ✅ Zero-Config

**Alternative:** Webpack (komplexer, langsamer)

---

## 🚀 Deployment-Strategie

### Option 1: Static Hosting (Empfohlen)

**Hosting-Plattformen:**
- GitHub Pages (kostenlos)
- Netlify (kostenlos)
- Vercel (kostenlos)

**Workflow:**
```bash
npm run build           # Vite erstellt dist/
git push origin main    # GitHub Action deployed automatisch
```

**Vorteile:**
- ✅ Kostenlos
- ✅ HTTPS automatisch
- ✅ CDN (schnell weltweit)
- ✅ Einfaches Setup

---

### Option 2: Lokal (Development)

**Setup:**
```bash
npm install
npm run dev  # Startet Vite Dev-Server auf http://localhost:5173
```

**Zettelstore muss parallel laufen:**
```bash
# Terminal 1
zettelstore run -d ./zettel

# Terminal 2
npm run dev
```

---

## 🧪 Testing-Constraints

**Anforderung (NFR-6):**
- Unit Tests für Kern-Logik
- Manual Testing für UI

**Testing-Stack:**
- **Unit Tests:** Vitest (Vite-kompatibel)
- **E2E Tests:** NICHT geplant (zu aufwändig)
- **Manual Testing:** Checklists (siehe NFR)

**Was wird getestet?**
```
✅ Graph-Datenstruktur (Nodes/Links)
✅ LocalStorage-Funktionen (Save/Load)
✅ API-Client (Mocked Fetch)
❌ NICHT: Canvas-Rendering (visuell, manuell testen)
❌ NICHT: D3.js Force-Simulation (Library-Test unnötig)
```

---

## 🔧 Development Tools

**Code Editor:**
- VS Code (empfohlen)
  - Extensions: ESLint, Prettier, Live Server

**Browser DevTools:**
- Performance Monitor (fps, memory)
- Network Tab (API-Calls)
- Canvas Inspector (Rendering)

**Version Control:**
- Git + GitHub
- Branch-Strategie: Feature Branches + main
- Commits: Conventional Commits (feat:, fix:, docs:)

---

## 📚 Referenzen

**Bestehende Architektur-Dokumente:**
- [wiki/Strategischer-Entwurf/ADR-01.md](wiki/Strategischer-Entwurf/ADR-01.md) - System-Integration (Standalone App)
- [wiki/Strategischer-Entwurf/ADR-02.md](wiki/Strategischer-Entwurf/ADR-02.md) - Datenbank-Wahl (~~SQLite~~ → LocalStorage!)
- [aufgaben-erklaert/04-Strategischer-Entwurf-ERKLAERT.md](aufgaben-erklaert/04-Strategischer-Entwurf-ERKLAERT.md) - Warum MVC falsch ist

**Externe Ressourcen:**
- [D3.js Documentation](https://d3js.org/)
- [Zettelstore API](https://zettelstore.de/manual/h/00001012920000.html)
- [Canvas Performance Tips](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas)
- [Force-Directed Graph Tutorial](https://observablehq.com/@d3/force-directed-graph)

---

## ✅ Decision Summary

| Bereich | Entscheidung | Begründung |
|---------|--------------|------------|
| **Architecture** | Client-Server (3-Tier) | Verteiltes System, kein MVC |
| **Framework** | Vanilla JavaScript | Einfachheit, D3-Kompatibilität |
| **Graph Library** | D3.js v7 | Force-Simulation, Barnes-Hut |
| **Rendering** | Canvas 2D | Performance (200@30fps) |
| **Storage** | LocalStorage | Einfachheit, ausreichend |
| **Markdown** | marked.js | Leichtgewichtig, sicher |
| **Build Tool** | Vite | Schnell, einfach |
| **Hosting** | GitHub Pages | Kostenlos, einfach |
| **Testing** | Vitest (Unit) + Manual | Pragmatisch |

---

**Nächste Schritte:**
1. Development-Umgebung aufsetzen (Node.js, Vite)
2. D3.js-Tutorial durcharbeiten
3. Canvas-Rendering-Prototyp erstellen
4. Zettelstore API testen

---

**Siehe auch:**
- [REQUIREMENTS.md](REQUIREMENTS.md) - Vollständige Anforderungen
- [wiki/Funktionale-Anforderungen.md](wiki/Funktionale-Anforderungen.md) - User Stories
- [wiki/Nicht-Funktionale-Anforderungen.md](wiki/Nicht-Funktionale-Anforderungen.md) - Performance, Qualität
