# Nicht-Funktionale Anforderungen (NFRs)

**Projekt:** ZettelWeb
**Version:** 2.0
**Datum:** 2025-11-04
**Gesamt:** 6 NFRs

---

## 📋 Übersicht

| ID | Kategorie | Beschreibung | Priorität |
|----|-----------|--------------|-----------|
| **NFR-1** | Performance | Graph-Rendering Performance | 🔴 Must |
| **NFR-2** | Kompatibilität | Browser-Kompatibilität | 🔴 Must |
| **NFR-3** | Usability | Intuitive Bedienung | 🟡 Should |
| **NFR-4** | Zuverlässigkeit | Daten-Persistierung | 🔴 Must |
| **NFR-5** | Performance | Initial Load Time | 🟡 Should |
| **NFR-6** | Wartbarkeit | Code-Qualität | 🟢 Nice |

**Legende:**
- 🔴 Must-Have (3 NFRs) - Kritisch
- 🟡 Should-Have (2 NFRs) - Wichtig
- 🟢 Nice-to-Have (1 NFR) - Bonus

---

## NFR-1: Graph-Rendering Performance 🔴⭐

### Kategorie
**Performance**

### Beschreibung
Das System soll auch bei vielen Zetteln (200+) flüssig und responsive bleiben, ohne sichtbare Verzögerungen oder Ruckler.

### Messbare Kriterien

#### 1. Framerate (FPS)
**Anforderung:** ≥30 fps während normaler Nutzung
**Test-Szenarien:**
- **Idle State:** Graph angezeigt, keine Interaktion → ≥30 fps
- **Drag-Operation:** Zettel wird gezogen → ≥30 fps durchgehend
- **Zoom/Pan:** Schnelles Zoomen & Pan → ≥30 fps
- **Force-Simulation:** Während Animation → ≥30 fps

**Messmethode:** Browser DevTools Performance Monitor, FPS-Counter

#### 2. Initial Render Time
**Anforderung:** <3 Sekunden für 200 Zettel (vom API-Call bis sichtbarer Graph)
**Test-Szenario:**
```
1. Zettelstore mit 200 Zetteln startet
2. User öffnet ZettelWeb
3. Zeit messen: fetch() Start → Graph sichtbar

Akzeptiert: <3s
```

**Messmethode:** performance.now(), Lighthouse Performance Audit

#### 3. Interaktions-Latenz
**Anforderung:** <100ms Reaktionszeit auf User-Input
**Test-Szenarien:**
- **Click auf Zettel:** Event → Modal erscheint → <100ms
- **Drag-Start:** MouseDown → Zettel "greift" → <100ms
- **Zoom:** Mouse Wheel → Zoom sichtbar → <100ms

**Messmethode:** performance.mark/measure, DevTools Timeline

#### 4. Smooth Animations
**Anforderung:** Keine sichtbaren Ruckler (frame drops)
**Test:**
- 60 Sekunden Graph-Nutzung (Drag, Zoom, Pan)
- FPS-Tracking
- Akzeptiert: <5% der Frames unter 30fps

#### 5. Skalierbarkeit
**Anforderung:** Bei 300 Zetteln <20% Performance-Degradation
**Test:**
```
200 Zettel: Durchschnitt X fps
300 Zettel: Durchschnitt Y fps

Formel: (X - Y) / X * 100% < 20%

Beispiel:
200 Zettel: 40 fps
300 Zettel: 33 fps
Degradation: (40-33)/40 = 17.5% ✅ Akzeptiert
```

### Test-Methoden

#### Automatisiert:
- **Lighthouse Performance Score:** Target >80
- **Custom Performance Tests:** Jest + Puppeteer
  ```javascript
  test('Graph renders 200 nodes within 3s', async () => {
    const start = performance.now();
    await renderGraph(200);
    const duration = performance.now() - start;
    expect(duration).toBeLessThan(3000);
  });
  ```

#### Manual:
- **FPS-Counter:** DevTools → Rendering → FPS Meter
- **Visual Inspection:** Ruckler sichtbar? Lag bei Drag?
- **Benchmark Suite:** Test-Datensets mit 100, 200, 300 Zetteln

### Technische Strategie

**Optimierungen:**
1. **D3.js Barnes-Hut Approximation:** O(n log n) statt O(n²)
2. **Canvas Rendering:** Performanter als DOM/SVG bei vielen Objekten
3. **RequestAnimationFrame:** Sync mit Browser Repaint (60fps target)
4. **Viewport-Culling:** Nur sichtbare Zettel rendern
5. **Debouncing/Throttling:** Storage-Writes nicht bei jedem Frame

**Performance-Budget:**
- Physik-Update: max. 10ms/Frame
- Rendering: max. 6ms/Frame
- Event-Handling: max. 2ms/Frame
- **Gesamt:** 18ms/Frame → ~55fps möglich

### Akzeptanztest

**Test-Setup:**
```
- Testdaten: 200 Zettel, 300 Verbindungen
- Browser: Chrome 120, i5 Prozessor, 8GB RAM
- Netzwerk: localhost (Zettelstore lokal)
```

**Test-Durchführung:**
1. Graph laden → Stopwatch startet
2. Graph sichtbar → Stopwatch stoppt → <3s? ✅
3. FPS-Monitor aktivieren
4. 10 Drag-Operationen durchführen
5. 10 Zoom-Operationen durchführen
6. FPS-Log auswerten → Min ≥30fps? ✅
7. 300 Zettel laden → FPS vergleichen → <20% Verlust? ✅

**Pass-Kriterien:**
- ✅ Initial Render <3s
- ✅ FPS durchgehend ≥30
- ✅ Keine sichtbaren Lags
- ✅ 300 Zettel Performance ok

### Priorität
🔴 **Must-Have** - Kern-Qualitätsziel!

### Siehe auch
- [NFR-5: Initial Load Time](#nfr-5-initial-load-time-)

---

## NFR-2: Browser-Kompatibilität 🔴

### Kategorie
**Kompatibilität**

### Beschreibung
Das System soll in allen gängigen modernen Browsern ohne Einschränkungen funktionieren.

### Messbare Kriterien

#### 1. Unterstützte Browser
**Anforderung:** Funktioniert in folgenden Browsern
- **Chrome/Edge:** Version 90+ (letzte 2 Major-Versionen ab Release)
- **Firefox:** Version 88+ (letzte 2 Major-Versionen)
- **Safari:** Version 15+ (macOS, iOS)

**NICHT unterstützt:**
- Internet Explorer (EOL)
- Browser ohne Canvas 2D Support
- Browser ohne ES6 Support

#### 2. Screen-Größen
**Anforderung:** Funktioniert auf diesen Auflösungen
- **Desktop:** 1920x1080 (optimal), 1280x720 (minimum)
- **Tablet:** 1024x768 (grundlegend nutzbar)
- **Mobile:** NICHT optimiert (Desktop-First)

#### 3. Feature-Anforderungen
**Erforderliche Browser-Features:**
- ✅ Canvas 2D Context
- ✅ LocalStorage / IndexedDB
- ✅ Fetch API
- ✅ ES6+ (Arrow Functions, Classes, Promises, async/await)
- ✅ CSS Flexbox
- ✅ Mouse Events + Wheel Events

**Optional (Nice-to-Have):**
- Touch Events (für Tablet-Nutzung)
- Pointer Events (unified Touch/Mouse)

#### 4. Performance pro Browser
**Anforderung:** NFR-1 (30fps) gilt für ALLE unterstützten Browser
```
Chrome 120: 200 Zettel @ ≥30fps ✅
Firefox 121: 200 Zettel @ ≥30fps ✅
Safari 17: 200 Zettel @ ≥30fps ✅
```

### Test-Methoden

#### Automatisiert:
- **BrowserStack / Sauce Labs:** Automatisierte Cross-Browser-Tests
- **Can I Use Check:** Feature-Detection Script
  ```javascript
  const features = {
    canvas: !!document.createElement('canvas').getContext,
    localStorage: !!window.localStorage,
    fetch: !!window.fetch
  };
  ```

#### Manual:
- **Test-Matrix:** Jedes Release in allen 3 Browsern testen
  ```
  | Feature | Chrome ✅ | Firefox ✅ | Safari ✅ |
  |---------|----------|-----------|----------|
  | Graph Render | ✅ | ✅ | ✅ |
  | Drag & Drop | ✅ | ✅ | ✅ |
  | Zoom/Pan | ✅ | ✅ | ✅ |
  | Persistence | ✅ | ✅ | ✅ |
  ```

- **Visual Regression Testing:** Screenshots vergleichen

### Akzeptanztest

**Test-Procedure:**
1. Setup: VM/BrowserStack mit Chrome, Firefox, Safari
2. ZettelWeb in allen 3 Browsern öffnen (gleiche Zettelstore-Daten)
3. Test-Checkliste durchgehen:
   - [ ] Graph lädt und rendert
   - [ ] Click auf Zettel öffnet Modal
   - [ ] Drag & Drop funktioniert
   - [ ] Zoom/Pan funktioniert
   - [ ] Positionen persistieren (Reload-Test)
   - [ ] FPS ≥30 in allen Browsern
4. Bug-Report für jede Inkonsistenz

**Pass-Kriterien:**
- ✅ Alle Features funktionieren in allen 3 Browsern
- ✅ Visuelle Darstellung identisch (±5px)
- ✅ Performance-Anforderungen erfüllt

### Priorität
🔴 **Must-Have**

---

## NFR-3: Usability - Intuitive Bedienung 🟡

### Kategorie
**Usability**

### Beschreibung
Die Anwendung soll ohne Anleitung verständlich und effizient bedienbar sein.

### Messbare Kriterien

#### 1. Standard-Interaktionen
**Anforderung:** Nutzt universelle Interaktions-Patterns
- **Zoom:** Mouse Wheel (Standard in Maps, Diagrammen, etc.)
- **Pan:** Drag auf leerem Canvas (Standard in Map-Apps)
- **Drag Object:** Mouse Down + Move (Standard in UI-Design)
- **Click:** Single-Click für Aktion (Standard)

**Test:** User führt Aktionen ohne Instruktion aus → Erfolgsrate >80%

#### 2. Visuelles Feedback
**Anforderung:** Jede Interaktion gibt sofortiges visuelles Feedback

| Interaktion | Erwartetes Feedback |
|-------------|---------------------|
| **Hover über Zettel** | Cursor → `pointer`, Zettel hebt sich ab |
| **Hover über leerem Canvas** | Cursor → `default` |
| **Drag-Start (Zettel)** | Cursor → `grabbing`, Zettel "lifts" (Shadow) |
| **Drag (Canvas)** | Cursor → `grab`, Canvas bewegt sich |
| **Zoom** | Zoom-Level angezeigt (z.B. "150%") |
| **Loading** | Spinner + "Lade Daten..." Text |
| **Error** | Roter Fehlertext + Icon |

**Test:** Jede Interaktion hat sichtbaren Effekt innerhalb 100ms

#### 3. Discoverability
**Anforderung:** Hauptfunktionen sind sichtbar/auffindbar

**UI-Elemente (mindestens):**
- [ ] Tag-Filter Dropdown (prominent platziert)
- [ ] "Fit to View" Button (Zoom Reset)
- [ ] "Reset Layout" Button (Positionen löschen)
- [ ] Zoom-Level Anzeige
- [ ] Hilfe/Info-Button (optional)

**Tooltips:**
- Alle Buttons haben Tooltip bei Hover
- Tooltip erscheint nach 500ms, verschwindet bei Mouse-Out

#### 4. Effizienz
**Anforderung:** Jede Hauptfunktion in ≤3 Klicks erreichbar

**Task-Effizienz-Tests:**
| Task | Max. Klicks | Durchschnitt |
|------|-------------|--------------|
| Zettel-Inhalt öffnen | 1 (Click auf Zettel) | 1 |
| Nach Tag filtern | 2 (Dropdown → Tag) | 2 |
| Zettel verschieben | 1 (Drag) | 1 |
| Zoom zurücksetzen | 1 ("Fit to View") | 1 |
| Layout neu initialisieren | 1 ("Reset Layout") | 1 |

**Kein tiefer Menu-Hierarchien!**

#### 5. Lernkurve
**Anforderung:** Neue Nutzer sind produktiv innerhalb 5 Minuten
- Erste 30s: Graph erkennbar, verstehen was gezeigt wird
- Erste 2min: Zettel-Click, Zoom/Pan ausprobiert
- Erste 5min: Alle Hauptfunktionen bekannt

### Test-Methoden

#### Usability-Test mit Test-Personen:
**Setup:**
- 3 Test-Personen (NICHT aus dem Team!)
- Keine Vorkenntnisse mit ZettelWeb
- Moderator beobachtet, redet NICHT (außer bei Stuck >2min)

**Test-Tasks:**
```
Task 1: "Finde den Zettel mit Titel 'Projektideen' und öffne ihn"
→ Erfolg wenn: Zettel gefunden + Modal geöffnet in <60s

Task 2: "Verschiebe diesen Zettel nach rechts oben"
→ Erfolg wenn: Zettel gedragged + Position geändert in <30s

Task 3: "Zeige nur Zettel mit Tag '#projekt' an"
→ Erfolg wenn: Filter gesetzt + nur #projekt sichtbar in <60s

Task 4: "Vergrößere den Graphen"
→ Erfolg wenn: Gezoomt (irgendeine Methode) in <30s

Task 5: "Bringe den Graphen wieder in Ausgangszustand"
→ Erfolg wenn: "Fit to View" gefunden + geclicked in <45s
```

**Erfolgsrate:** ≥80% (4 von 5 Tasks erfolgreich, Durchschnitt über 3 Personen)

#### System Usability Scale (SUS):
- Fragebogen mit 10 Fragen nach Test
- Score berechnen (0-100 Skala)
- **Target:** SUS ≥70 (durchschnittlich), >80 (gut)

### Akzeptanztest

**Criteria:**
- ✅ 3 von 3 Test-Personen erfolgreich bei ≥4 Tasks
- ✅ SUS Score ≥70
- ✅ Keine "How do I...?" Fragen für Basis-Features
- ✅ Positives Feedback ("intuitiv", "selbsterklärend")

### Priorität
🟡 **Should-Have**

---

## NFR-4: Daten-Persistierung Zuverlässigkeit 🔴

### Kategorie
**Zuverlässigkeit / Data Integrity**

### Beschreibung
Manuell positionierte Zettel und Einstellungen dürfen nicht verloren gehen, auch bei Fehler-Szenarien.

### Messbare Kriterien

#### 1. Speicher-Latenz
**Anforderung:** Position-Update innerhalb 1 Sekunde nach Drag-Ende
```
User: Drag-Ende (MouseUp)
  → System: Debounce-Timer 500ms
  → System: localStorage.setItem()
  → Gesamt: <1s
```

**Test:** 10x Drag durchführen, Zeit messen → Alle <1s?

#### 2. Crash-Recovery
**Anforderung:** Daten bis letzte erfolgreiche Speicherung wiederherstellbar

**Test-Szenarien:**
```
Szenario A: Browser-Crash während Drag
  → Nach Neustart: Letzte gespeicherte Position geladen ✅
  → Aktueller Drag verloren (akzeptabel)

Szenario B: Browser-Crash während Storage-Write
  → Nach Neustart: Entweder alte oder neue Position ✅
  → NIEMALS: korrupte Daten oder App-Crash

Szenario C: Tab geschlossen während Graph aktiv
  → Beim Wiederöffnen: Alle Positionen da ✅
```

#### 3. Storage-Limits
**Anforderung:** Funktioniert auch bei begrenztem Storage

**Test:**
```
localStorage Limit: ~5-10 MB (Browser-abhängig)
ZettelWeb für 500 Zettel: <10 MB

Berechnung:
- 500 Zettel × (ID: 20B, x: 8B, y: 8B) = ~18KB
- State (Zoom, Pan, Filter): ~1KB
- Gesamt: <50KB für 500 Zettel ✅
```

**Fehlerbehandlung bei vollem Storage:**
```javascript
try {
  localStorage.setItem('zettelweb-pos', data);
} catch (QuotaExceededError) {
  // Graceful Degradation:
  // 1. User-Meldung: "Speicher voll"
  // 2. Angebot: "Alte Daten löschen?"
  // 3. Fallback: Im RAM halten (geht verloren bei Reload)
}
```

#### 4. Daten-Format & Validierung
**Anforderung:** JSON (human-readable, debuggable), validiert beim Laden
```json
{
  "version": "1.0",
  "positions": {
    "20251027134512": { "x": 450.5, "y": 320.8 },
    "20251028091234": { "x": 123.0, "y": 456.0 }
  },
  "state": {
    "zoom": 1.5,
    "pan": { "x": 100, "y": 200 },
    "filter": ["#projekt"]
  }
}
```

**Validation beim Laden:**
```javascript
const data = JSON.parse(localStorage.getItem('zettelweb-data'));
if (!data || !data.version || !data.positions) {
  // Korrupte Daten → Ignorieren, default verwenden
}
```

#### 5. Konsistenz
**Anforderung:** Keine partial Updates, atomic Writes
```javascript
// FALSCH: Zwei separate Writes (nicht atomic!)
localStorage.setItem('zettelweb-pos', positions);
localStorage.setItem('zettelweb-state', state); // Crash hier → inkonsistent!

// RICHTIG: Ein Write mit allem
const data = { positions, state };
localStorage.setItem('zettelweb-data', JSON.stringify(data));
```

### Test-Methoden

#### Automatisiert:
```javascript
describe('Persistence', () => {
  test('saves position within 1s after drag', async () => {
    const start = Date.now();
    await dragZettel(zettel, { x: 500, y: 300 });
    await waitForStorageUpdate();
    expect(Date.now() - start).toBeLessThan(1000);
  });

  test('recovers from crash', () => {
    // Mock: Positionen speichern
    savePositions({ '123': { x: 100, y: 200 } });
    // Simulate: Browser reload
    reloadApp();
    // Verify: Positionen geladen
    expect(getZettelPosition('123')).toEqual({ x: 100, y: 200 });
  });
});
```

#### Manual:
**Crash-Recovery-Test:**
1. ZettelWeb öffnen, 10 Zettel manuell positionieren
2. Browser-Tab hart killen (Task Manager → Kill Process)
3. Browser neu starten, ZettelWeb öffnen
4. Verify: 10 Positionen sind da (oder 9, falls letzter Drag unterbrochen)

**Storage-Voll-Test:**
1. localStorage-Limit simulieren (DevTools → Application → Clear → Fill)
2. Zettel verschieben → Fehler auslösen
3. Verify: Fehlermeldung erscheint, App crasht NICHT

### Akzeptanztest

**Pass-Kriterien:**
- ✅ 10x Drag → alle Positionen innerhalb 1s gespeichert
- ✅ Crash-Test → Daten wiederhergestellt (±1 Drag)
- ✅ Storage-Voll → Graceful Error Handling
- ✅ JSON validation → Keine Crashes bei korrupten Daten

### Priorität
🔴 **Must-Have**

---

## NFR-5: Initial Load Time 🟡

### Kategorie
**Performance**

### Beschreibung
Erste Anzeige des Graphen soll schnell erfolgen für gute User Experience (keine lange Wartezeit).

### Messbare Kriterien

#### 1. Time to Interactive (TTI)
**Anforderung:** <5 Sekunden (von URL-Eingabe bis Graph klickbar)

**Breakdown:**
```
0.0s: User drückt Enter in URL-Bar
0.1s: HTML geladen
0.5s: JavaScript geladen + parsed
1.0s: App initialisiert, API-Call startet (GET /z)
2.0s: API Response da (1s für Zettelstore)
2.5s: Daten geparst, Graph-Rendering startet
3.5s: Force-Simulation stabilisiert sich
4.0s: Graph vollständig interaktiv

Gesamt: 4.0s ✅ (<5s)
```

#### 2. API Response Time
**Anforderung:** Zettelstore /z Endpoint <1 Sekunde
- localhost: <100ms (typisch)
- LAN: <500ms
- Akzeptiert: <1000ms

#### 3. Force-Simulation Stabilisierung
**Anforderung:** <3 Sekunden bis Graph "zur Ruhe kommt"
- D3.js simulation.alphaTarget(0)
- Simulation stoppt wenn alpha < alphaMin (0.001)
- Max. 300 Iterations (~ 3s bei 60fps)

#### 4. Bundle Size
**Anforderung:** <500 KB (gzipped) für JavaScript
```
- D3.js: ~250 KB (minified + gzip)
- App Code: ~100 KB
- Dependencies: ~100 KB
- Gesamt: ~450 KB ✅
```

#### 5. Perceived Performance
**Anforderung:** Loading-Feedback mit Fortschrittsanzeige
```
Phase 1: "Lade Zettel..." (0-1s)
Phase 2: "Berechne Layout..." (1-3s)
Phase 3: "Fertig!" → verschwindet (3s)
```

### Test-Methoden

#### Lighthouse Performance Audit:
```bash
lighthouse https://localhost:8080/zettelweb --only-categories=performance
```
**Target:** Performance Score ≥80/100

#### Network Throttling:
**Test unter schlechten Bedingungen:**
- Slow 3G Simulation (DevTools → Network → Throttling)
- Auch hier: TTI <10s (2x Faktor ok bei Slow Network)

#### Performance API:
```javascript
// Measure TTI
performance.mark('app-start');
// ... app loads ...
performance.mark('app-interactive');
performance.measure('TTI', 'app-start', 'app-interactive');

const tti = performance.getEntriesByName('TTI')[0].duration;
console.log(`TTI: ${tti}ms`);
```

### Akzeptanztest

**Test-Setup:**
- Zettelstore mit 200 Zetteln auf localhost
- Chrome DevTools Performance Recording
- 3 Test-Runs (Cache leer bei jedem Run)

**Pass-Kriterien:**
- ✅ TTI Durchschnitt <5s
- ✅ Lighthouse Score ≥80
- ✅ Kein "White Screen" länger als 1s
- ✅ Loading Spinner erscheint sofort (<500ms)

### Priorität
🟡 **Should-Have**

---

## NFR-6: Wartbarkeit & Code-Qualität 🟢

### Kategorie
**Wartbarkeit**

### Beschreibung
Code soll verständlich, strukturiert und leicht erweiterbar sein für zukünftige Entwicklung.

### Messbare Kriterien

#### 1. Dokumentation
**Anforderung:**
- [ ] JSDoc für alle öffentlichen Funktionen/Klassen (100% Coverage)
- [ ] README.md mit Setup-Anleitung
- [ ] ARCHITECTURE.md mit System-Übersicht
- [ ] ADRs für wichtige Entscheidungen (mindestens 3)

**Beispiel JSDoc:**
```javascript
/**
 * Renders all Zettel nodes on the canvas.
 * @param {Array<Zettel>} zettel - Array of Zettel objects
 * @param {CanvasRenderingContext2D} ctx - Canvas context
 * @param {Object} options - Rendering options
 * @param {number} options.zoom - Current zoom level (0.5-2.0)
 * @returns {void}
 */
function renderZettel(zettel, ctx, options) { /* ... */ }
```

#### 2. Code-Struktur
**Anforderung:** Modulare, übersichtliche Struktur

**Ordnerstruktur:**
```
src/
├── rendering/
│   ├── canvas.js         (Canvas setup, drawing primitives)
│   ├── zettel-renderer.js (Zettel drawing)
│   └── graph-renderer.js (Complete graph rendering)
├── physics/
│   ├── simulation.js     (D3.js force simulation wrapper)
│   └── layout.js         (Layout calculations)
├── storage/
│   ├── persistence.js    (LocalStorage abstraction)
│   └── state-manager.js  (State management)
├── api/
│   └── zettelstore.js    (API client)
├── ui/
│   ├── modal.js          (Zettel detail modal)
│   └── controls.js       (Zoom, Filter controls)
└── main.js               (App entry point)
```

**Regeln:**
- Max. 200 Zeilen pro Datei (sonst splitten!)
- Max. 50 Zeilen pro Funktion
- Ein Modul = eine Verantwortung

#### 3. Naming Conventions
**Anforderung:** Klar benannte Variablen/Funktionen
```javascript
// SCHLECHT:
function z(x, y) { return x * y; }
let tmp = getData();

// GUT:
function calculateZoomFactor(targetZoom, currentZoom) {
  return targetZoom / currentZoom;
}
let zettelDataFromAPI = fetchZettelFromStore();
```

#### 4. Linting
**Anforderung:** ESLint konfiguriert, 0 Errors, <10 Warnings
```bash
eslint src/**/*.js
# Output: 0 errors, 3 warnings ✅
```

**ESLint Config:**
- airbnb-base Styleguide
- Custom Rules: max-lines (200), max-len (100)

#### 5. Version Control
**Anforderung:** Git Best Practices
- Aussagekräftige Commit-Messages (nicht "fix", "update")
- Feature-Branches (nicht direkt in main!)
- Pull Requests mit Code Review (mindestens 1 Reviewer)

**Commit-Message-Format:**
```
<type>(<scope>): <subject>

<body>

<footer>

Beispiel:
feat(rendering): Add viewport culling for performance

Only render Zettel that are visible in current viewport.
Reduces render calls by ~60% when zoomed in.

Closes #42
```

### Test-Methoden

#### Automatisiert:
```bash
# Linting
npm run lint

# JSDoc Coverage
npm run docs:coverage

# Complexity Analysis
npm run complexity
```

#### Code Review Checklist:
- [ ] Code ist verständlich ohne Kommentare (oder Kommentare vorhanden)
- [ ] Keine Magic Numbers (z.B. `if (zoom > 1.5)` → const `MAX_ZOOM`)
- [ ] Error Handling vorhanden
- [ ] Keine Code-Duplizierung (DRY-Prinzip)

### Akzeptanztest

**Onboarding-Test:**
- Neues Team-Mitglied (oder externer Developer)
- Bekommt README.md + Code
- Task: "Ändere Zettel-Farbe zu Blau"
- **Pass:** Änderung innerhalb 2h ohne Hilfe

**Maintenance-Test:**
- 3 Monate nach Projekt-Ende
- Bug-Fix oder kleines Feature
- **Pass:** Team kann Code noch verstehen, Änderung in <4h

### Priorität
🟢 **Nice-to-Have** (wichtig, aber nicht kritisch für Funktion)

---

## 📊 NFR Zusammenfassung

### Test-Matrix

| NFR | Auto-Test | Manual-Test | Kontinuierlich | Release-Gate |
|-----|-----------|-------------|----------------|--------------|
| **NFR-1: Performance** | ✅ Lighthouse | ✅ FPS Monitor | ✅ Jeder Commit | ✅ <30fps → Block |
| **NFR-2: Browser** | ✅ BrowserStack | ✅ Manual Matrix | ⚠️ Jede Woche | ✅ 1 Browser fail → Block |
| **NFR-3: Usability** | ❌ Schwer | ✅ User Tests | ❌ Manual only | ⚠️ SUS <60 → Warning |
| **NFR-4: Persistence** | ✅ Jest Tests | ✅ Crash Tests | ✅ Jeder Commit | ✅ Daten verloren → Block |
| **NFR-5: Load Time** | ✅ Lighthouse | ✅ Stopwatch | ⚠️ Jede Woche | ⚠️ >7s → Warning |
| **NFR-6: Code Quality** | ✅ ESLint | ✅ Code Review | ✅ Jeder Commit | ⚠️ >20 Warnings → Warning |

### Release-Kriterien

**Must-Pass für Release:**
- ✅ NFR-1: Performance Tests bestanden
- ✅ NFR-2: Funktioniert in allen 3 Browsern
- ✅ NFR-4: Persistence Tests bestanden

**Should-Pass (Warnings ok):**
- ⚠️ NFR-3: Usability-Test wenn möglich
- ⚠️ NFR-5: Load Time ok, aber nicht kritisch
- ⚠️ NFR-6: Code-Qualität gut, aber nicht blockierend

---

## 📚 Referenzen

### Test-Tools
- **Performance:** Lighthouse, WebPageTest, DevTools Performance
- **Cross-Browser:** BrowserStack, Sauce Labs, local VMs
- **Linting:** ESLint, Prettier
- **Testing:** Jest, Puppeteer (E2E)

### Standards
- **Usability:** ISO 9241 (Ergonomics), SUS Questionnaire
- **Performance:** Web Vitals (Google), RAIL Model
- **Code Quality:** Airbnb Style Guide, Clean Code Principles

### Verwandte Dokumente
- [REQUIREMENTS.md](../REQUIREMENTS.md) - Vollständige Requirements
- [Funktionale-Anforderungen.md](Funktionale-Anforderungen.md) - User Stories
- [TECHNICAL-CONSTRAINTS.md](../TECHNICAL-CONSTRAINTS.md) - Tech Stack

---

**Ende der Nicht-Funktionalen Anforderungen**

Bei Fragen oder Änderungswünschen: GitHub Issues erstellen.
