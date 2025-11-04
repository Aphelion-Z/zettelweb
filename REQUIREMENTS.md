# 📋 ZettelWeb - Requirements Specification

**Projekt:** ZettelWeb - Graphische Visualisierung für Zettelstore
**Team:** Group 7, HS Heilbronn, WIN3, WiSe 2025/26
**Version:** 2.0 (Komplette Überarbeitung)
**Datum:** 2025-11-04
**Status:** Approved

---

## 🎯 VISION & SCOPE

### Vision Statement

**ZettelWeb** ist eine interaktive, web-basierte Graph-Visualisierung für Detlef Sterns Zettelstore-System.

**Problem:**
Zettelstore zeigt Zettel als einfache Liste. Bei vielen Zetteln verliert man die Übersicht über Zusammenhänge und Verbindungen.

**Lösung:**
ZettelWeb visualisiert alle Zettel als **interaktiven Graphen** mit force-directed Layout, bei dem:
- **Zettel = Knoten** (Kreise/Rechtecke)
- **Verbindungen = Kanten** (Linien)
- **Position = automatisch** (basierend auf Verbindungsstruktur)

**Kern-Innovation:**
- 🔷 **Force-Directed Layout:** Zettel positionieren sich automatisch basierend auf ihren Verbindungen
- 🔷 **Interaktive Exploration:** Click, Drag, Zoom, Pan für intuitive Navigation
- 🔷 **Intelligente Filterung:** Tag-basiert mit semi-transparenter Darstellung externer Verbindungen
- 🔷 **Persistent State:** Manuell positionierte Zettel bleiben gespeichert

### Elevator Pitch

> "ZettelWeb verwandelt die Liste deiner Zettel in ein lebendiges, interaktives Netzwerk-Diagramm - wie eine Mind-Map, die sich selbst organisiert!"

### Haupt-Use-Case

```
1. User öffnet ZettelWeb im Browser
2. System lädt alle Zettel von Zettelstore via API
3. Graph wird mit force-directed Layout gerendert
4. User erkundet den Graphen:
   - Click auf Zettel → Inhalt anzeigen
   - Drag Zettel → Position manuell anpassen
   - Filter nach Tag → Fokus auf Thema
   - Zoom & Pan → Navigation durch großen Graph
5. Positionen werden automatisch gespeichert
6. Beim nächsten Öffnen: Gleiche Anordnung
```

### Expliziter Scope

**✅ IM SCOPE:**
- Graph-Visualisierung von Zetteln & Verbindungen
- Force-directed automatic layout
- Interaktive Navigation (Zoom, Pan, Drag)
- Click zum Öffnen von Zettel-Inhalten
- Tag-basierte Filterung
- Persistierung von Positionen & Graph-State
- Performance: 200+ Zettel @ 30fps

**❌ NICHT IM SCOPE:**
- Zettel-Inhalte bearbeiten (nur anzeigen!)
- Multi-User / Kollaboration
- Cloud-Synchronisation
- Export/Import Features
- Mobile App (Desktop-First)
- 3D-Visualisierung
- Authentication/Login

Siehe Abschnitt [Nicht-Anforderungen](#-nicht-anforderungen) für Details.

---

## 📊 FUNKTIONALE ANFORDERUNGEN (User Stories)

Insgesamt **11 User Stories** gruppiert in **4 Epics**.

**Story Points Gesamt:** 45 Punkte = ~90-100 Arbeitsstunden Implementierung

**Priorisierung:**
- 🔴 **Must-Have:** 5 Stories (24 SP) - Kern-Features, ohne diese funktioniert nichts
- 🟡 **Should-Have:** 4 Stories (16 SP) - Wichtig für gute Usability
- 🟢 **Nice-to-Have:** 2 Stories (5 SP) - Polish, wenn Zeit übrig

---

### Epic 1: Graph-Visualisierung 🔴

**Kern-Feature:** Force-Directed Graph-Darstellung aller Zettel

---

#### FR-1.1: Force-Directed Graph Layout anzeigen 🔴

**Als** Nutzer
**will ich** alle Zettel als interaktiven Graphen mit automatischer Positionierung sehen,
**damit** ich sofort erkenne welche Zettel miteinander verbunden sind und wie das gesamte Wissens-Netzwerk strukturiert ist.

**Akzeptanzkriterien:**
- [ ] Alle Zettel aus Zettelstore werden als Knoten (Kreise/Rechtecke) dargestellt
- [ ] Zettel-Titel ist auf dem Knoten sichtbar (oder bei Hover)
- [ ] Verbindungen zwischen Zetteln werden als Linien gezeichnet
- [ ] Force-Directed Layout positioniert Zettel automatisch:
  - Verbundene Zettel ziehen sich an (Spring force)
  - Alle Zettel stoßen sich ab (Repulsion force)
  - Simulation erreicht stabiles Equilibrium
- [ ] Graph ist innerhalb 3 Sekunden nach Laden sichtbar
- [ ] Mindestens 200 Zettel werden flüssig dargestellt (30+ fps)

**Technische Hinweise:**
- D3.js force simulation (d3.forceSimulation, d3.forceLink, d3.forceManyBody)
- HTML5 Canvas für Rendering (performanter als SVG bei vielen Objekten)
- Viewport-Culling: Nur sichtbare Zettel rendern

**Priorität:** 🔴 Must-Have
**Story Points:** 8
**Epic:** Graph-Visualisierung

**Test-Szenario:**
```
Gegeben: Zettelstore mit 200 Zetteln und 150 Verbindungen
Wenn: User öffnet ZettelWeb
Dann:
  - Graph wird innerhalb 3s angezeigt
  - Alle 200 Zettel sind sichtbar
  - Verbindungen sind als Linien erkennbar
  - Stark verbundene Zettel sind räumlich nah
  - Unverbundene Zettel sind getrennt
```

---

#### FR-1.2: Visuelle Darstellung von Verbindungen 🔴

**Als** Nutzer
**will ich** Verbindungen zwischen Zetteln als Linien sehen,
**damit** ich sofort erkenne welche Zettel miteinander verknüpft sind.

**Akzeptanzkriterien:**
- [ ] Jede Verbindung zwischen Zetteln ist als Linie dargestellt
- [ ] Linien verbinden Zettel-Mittelpunkte oder Ränder
- [ ] Linien sind deutlich sichtbar (Farbe, Dicke konfigurierbar)
- [ ] Linien überlappen Zettel nicht (gehen bis zum Zettel-Rand)
- [ ] Hover über Linie hebt beide verbundenen Zettel hervor (optional)
- [ ] Bidirektionale Verbindungen werden als eine Linie dargestellt

**Technische Hinweise:**
- Canvas lineTo() für Linien-Rendering
- Collision detection für Linie-Zettel Intersection
- Line color/width als Konfiguration

**Priorität:** 🔴 Must-Have
**Story Points:** 3
**Epic:** Graph-Visualisierung

**Test-Szenario:**
```
Gegeben: Zettel A verlinkt zu Zettel B und C
Wenn: Graph wird angezeigt
Dann:
  - Zwei Linien sind sichtbar: A→B und A→C
  - Linien starten/enden am Zettel-Rand
  - Linien sind durchgängig (keine Lücken)
```

---

#### FR-1.3: Initialer Graph-Load & Rendering 🔴

**Als** Nutzer
**will ich** beim Öffnen der Anwendung automatisch den Graphen geladen bekommen,
**damit** ich sofort mit der Exploration beginnen kann.

**Akzeptanzkriterien:**
- [ ] App startet automatisch mit Graph-Ansicht (kein "Load"-Button nötig)
- [ ] Daten werden von Zettelstore REST API geholt (GET /z)
- [ ] Loading-Indicator wird während des Ladens angezeigt
- [ ] Bei Fehler (Zettelstore nicht erreichbar): Fehlermeldung mit Retry-Option
- [ ] Gespeicherte Positionen werden aus Browser-Storage geladen (falls vorhanden)
- [ ] Falls keine gespeicherten Positionen: Force-Simulation initialisiert Layout

**Technische Hinweise:**
- fetch() API für Zettelstore-Zugriff
- LocalStorage/IndexedDB für gespeicherte Positionen
- Error Handling mit User-Feedback

**Priorität:** 🔴 Must-Have
**Story Points:** 5
**Epic:** Graph-Visualisierung

**Test-Szenario:**
```
Gegeben: Zettelstore läuft auf localhost:23123
Wenn: User öffnet ZettelWeb URL
Dann:
  - Loading Spinner erscheint
  - API-Call zu /z wird ausgeführt
  - Zettel-Daten werden geparst
  - Graph wird gerendert
  - Loading verschwindet

Fehler-Fall:
Gegeben: Zettelstore ist offline
Wenn: User öffnet ZettelWeb
Dann:
  - Fehlermeldung: "Zettelstore nicht erreichbar"
  - "Retry" Button wird angezeigt
```

---

### Epic 2: Interaktion 🔴🟡

**Features für Navigation und Exploration des Graphen**

---

#### FR-2.1: Zettel-Inhalt anzeigen (Click) 🔴

**Als** Nutzer
**will ich** durch Klick auf einen Zettel dessen Inhalt sehen,
**damit** ich die Informationen lesen kann ohne Zettelstore selbst öffnen zu müssen.

**Akzeptanzkriterien:**
- [ ] Single-Click auf Zettel öffnet Detail-Ansicht
- [ ] Detail-Ansicht zeigt:
  - [ ] Zettel-Titel (groß, hervorgehoben)
  - [ ] Zettel-Inhalt (vollständiger Text)
  - [ ] Metadaten (Tags, Erstellungsdatum, ID)
  - [ ] Liste verknüpfter Zettel (anklickbar)
- [ ] Detail-Ansicht als Modal/Sidebar (nicht neues Fenster)
- [ ] "Schließen" Button oder ESC-Taste schließt Detail-Ansicht
- [ ] Click auf verknüpften Zettel in Liste öffnet diesen Zettel
- [ ] Markdown-Formatierung wird korrekt dargestellt (falls Zettelstore Markdown nutzt)

**Technische Hinweise:**
- Modal/Sidebar-Component
- Markdown-Parser (marked.js oder ähnlich)
- Event-Handling für Click-Detection auf Canvas-Objekten

**Priorität:** 🔴 Must-Have
**Story Points:** 3
**Epic:** Interaktion

**Test-Szenario:**
```
Gegeben: Graph mit sichtbaren Zetteln
Wenn: User klickt auf Zettel "Projektideen"
Dann:
  - Modal öffnet sich
  - Titel "Projektideen" wird angezeigt
  - Vollständiger Zettel-Text ist lesbar
  - Tags werden angezeigt: #projekt, #idee
  - "Schließen" (X) Button ist vorhanden

Wenn: User klickt auf "Schließen"
Dann: Modal schließt sich, Graph bleibt sichtbar
```

---

#### FR-2.2: Zettel manuell verschieben (Drag & Drop) 🟡

**Als** Nutzer
**will ich** Zettel mit der Maus verschieben können,
**damit** ich die Anordnung nach meinen Vorstellungen anpassen kann.

**Akzeptanzkriterien:**
- [ ] Mouse-Down auf Zettel startet Drag-Operation
- [ ] Während Drag: Zettel folgt Maus-Cursor smooth
- [ ] Visuelles Feedback während Drag (z.B. Cursor ändert sich, Zettel hebt sich ab)
- [ ] Mouse-Up beendet Drag, Zettel bleibt an neuer Position
- [ ] Neue Position wird sofort in Browser-Storage gespeichert
- [ ] Verbindungslinien bewegen sich mit dem Zettel
- [ ] Andere Zettel werden NICHT automatisch bewegt (manueller Drag pausiert Physik-Simulation)
- [ ] Drag funktioniert auch bei überlappenden Zetteln (oberster wird gedragged)

**Technische Hinweise:**
- Canvas mouse events (mousedown, mousemove, mouseup)
- Collision detection für Zettel-Selection
- Debouncing für Storage-Writes (nicht bei jedem Pixel!)

**Priorität:** 🟡 Should-Have
**Story Points:** 5
**Epic:** Interaktion

**Test-Szenario:**
```
Gegeben: Graph mit Zettel an Position (100, 100)
Wenn: User klickt auf Zettel und zieht zu (200, 200)
Dann:
  - Zettel folgt Maus smooth
  - Verbindungslinien passen sich an
  - Nach Mouse-Up: Zettel bleibt bei (200, 200)

Wenn: User refresht Browser
Dann: Zettel ist immer noch bei (200, 200) (persistiert!)
```

---

#### FR-2.3: Zoom & Pan Navigation 🟡

**Als** Nutzer
**will ich** den Graphen zoomen und verschieben können,
**damit** ich bei vielen Zetteln die Übersicht behalte und Details erkenne.

**Akzeptanzkriterien:**
- [ ] **Zoom:**
  - [ ] Mouse Wheel up = Zoom In
  - [ ] Mouse Wheel down = Zoom Out
  - [ ] Zoom-Range: 50% bis 200%
  - [ ] Zoom-Zentrum ist Maus-Position (nicht Canvas-Mitte)
- [ ] **Pan:**
  - [ ] Drag auf leerem Canvas (nicht auf Zettel) = Pan
  - [ ] Alternative: Mittlere Maustaste + Drag = Pan
  - [ ] Smooth Movement (keine Sprünge)
- [ ] **UI-Feedback:**
  - [ ] Zoom-Level wird angezeigt (z.B. "100%")
  - [ ] "Fit to View" Button zentriert Graphen
- [ ] **Performance:**
  - [ ] Zoom/Pan ist flüssig (30+ fps)
  - [ ] Keine Lags bei schnellen Operationen

**Technische Hinweise:**
- Canvas transform (scale, translate)
- Viewport transformation für Koordinaten
- RequestAnimationFrame für smooth rendering

**Priorität:** 🟡 Should-Have
**Story Points:** 3
**Epic:** Interaktion

**Test-Szenario:**
```
Gegeben: Graph bei 100% Zoom
Wenn: User scrollt Mouse Wheel up 5x
Dann: Zoom erhöht sich auf ~150%, Graph ist größer

Gegeben: Graph gezoomt
Wenn: User drückt "Fit to View"
Dann: Graph wird zentriert und auf optimalen Zoom gesetzt
```

---

### Epic 3: Filter & Fokus 🟡🟢

**Features für fokussiertes Arbeiten mit Teilmengen**

---

#### FR-3.1: Tag-basierte Filterung 🟡

**Als** Nutzer
**will ich** den Graphen nach Tags filtern können,
**damit** ich nur Zettel zu einem bestimmten Thema sehe.

**Akzeptanzkriterien:**
- [ ] Tag-Filter-Dropdown in der UI (Liste aller vorhandenen Tags)
- [ ] Auswahl eines Tags:
  - [ ] Nur Zettel mit diesem Tag werden voll angezeigt
  - [ ] Zettel ohne Tag werden ausgeblendet (opacity 0 oder unsichtbar)
- [ ] "Alle anzeigen" Option entfernt Filter
- [ ] Mehrfach-Auswahl möglich (z.B. #projekt UND #wichtig)
- [ ] Filterung erfolgt sofort (keine Verzögerung)
- [ ] Filter-State wird gespeichert (bei Reload aktiv)

**Technische Hinweise:**
- Tag-Extraktion aus Zettelstore-Metadaten
- Filter-Logic vor Rendering
- Multi-Select Dropdown oder Checkbox-Liste

**Priorität:** 🟡 Should-Have
**Story Points:** 5
**Epic:** Filter & Fokus

**Test-Szenario:**
```
Gegeben: 100 Zettel, davon 20 mit Tag #projekt
Wenn: User wählt Filter "#projekt"
Dann:
  - 20 Zettel mit #projekt sind sichtbar
  - 80 andere Zettel sind ausgeblendet

Wenn: User klickt "Alle anzeigen"
Dann: Alle 100 Zettel sind wieder sichtbar
```

---

#### FR-3.2: Semi-transparente externe Verbindungen 🟢

**Als** Nutzer
**will ich** bei aktiver Tag-Filterung auch Zettel außerhalb des Filters sehen wenn sie verbunden sind,
**damit** ich Zusammenhänge über Tag-Grenzen hinweg erkenne.

**Akzeptanzkriterien:**
- [ ] Bei aktivem Tag-Filter:
  - [ ] Zettel MIT Filter-Tag: voll sichtbar (opacity 1.0)
  - [ ] Zettel OHNE Filter-Tag aber MIT Verbindung zu gefilterten Zetteln:
    - [ ] Semi-transparent dargestellt (opacity 0.3)
    - [ ] Titel erkennbar aber gedimmt
  - [ ] Zettel OHNE Filter-Tag und OHNE Verbindung: komplett ausgeblendet
- [ ] Verbindungslinien:
  - [ ] Innerhalb Filter (Tag ↔ Tag): normale Farbe
  - [ ] Zu semi-transparenten Zetteln (Tag ↔ Nicht-Tag): gestrichelt oder heller
- [ ] Hover über semi-transparenten Zettel zeigt Tooltip mit Tags
- [ ] Click auf semi-transparenten Zettel öffnet Detail-Ansicht (wie normal)

**Technische Hinweise:**
- Graph-Traversierung für "connected nodes"
- Opacity-Styling basierend auf Filter-Status
- CSS/Canvas opacity settings

**Priorität:** 🟢 Nice-to-Have
**Story Points:** 3
**Epic:** Filter & Fokus

**Test-Szenario:**
```
Gegeben:
  - Zettel A (#projekt)
  - Zettel B (#projekt)
  - Zettel C (#idee) - verbunden mit B
  - Zettel D (#random) - nicht verbunden

Wenn: User filtert nach #projekt
Dann:
  - A: voll sichtbar
  - B: voll sichtbar
  - C: semi-transparent (wegen Verbindung zu B!)
  - D: ausgeblendet (keine Verbindung)
```

---

#### FR-3.3: Hover-Highlighting verbundener Zettel 🟢

**Als** Nutzer
**will ich** beim Überfahren eines Zettels sehen welche anderen Zettel damit verbunden sind,
**damit** ich schnell Zusammenhänge erkenne.

**Akzeptanzkriterien:**
- [ ] Hover über Zettel:
  - [ ] Dieser Zettel wird hervorgehoben (z.B. größer, farbig umrandet)
  - [ ] Alle direkt verbundenen Zettel werden hervorgehoben
  - [ ] Alle anderen Zettel werden gedimmt (opacity 0.3)
  - [ ] Verbindungslinien zum gehover-ten Zettel werden dicker/farbig
- [ ] Hover-Effekt verschwindet sofort nach Mouse-Out
- [ ] Hover funktioniert auch bei aktivem Tag-Filter
- [ ] Performance: Kein Lag bei Hover-Operationen

**Technische Hinweise:**
- Mousemove event tracking
- Graph-Traversierung für connected nodes
- Temporary styling (ohne State-Change)

**Priorität:** 🟢 Nice-to-Have
**Story Points:** 2
**Epic:** Filter & Fokus

**Test-Szenario:**
```
Gegeben: Zettel A verbunden mit B, C, D
Wenn: User hovert über A
Dann:
  - A wird hervorgehoben
  - B, C, D werden hervorgehoben
  - Alle anderen Zettel sind gedimmt
  - Linien A↔B, A↔C, A↔D sind dick/farbig

Wenn: Mouse bewegt sich weg von A
Dann: Alle Zettel wieder normal
```

---

### Epic 4: Persistence 🔴🟡

**Features für Speicherung von Zuständen**

---

#### FR-4.1: Zettel-Positionen persistieren 🔴

**Als** Nutzer
**will ich** dass manuell verschobene Zettel an ihrer Position bleiben,
**damit** ich beim nächsten Öffnen die gleiche Anordnung wiederfinde.

**Akzeptanzkriterien:**
- [ ] Nach jedem manuellen Drag eines Zettels:
  - [ ] Position (x, y Koordinaten) wird gespeichert
  - [ ] Speicherung erfolgt automatisch (kein "Save"-Button)
  - [ ] Speicherung innerhalb 1 Sekunde nach Drag-Ende
- [ ] Beim Neuladen der App:
  - [ ] Gespeicherte Positionen werden geladen
  - [ ] Zettel erscheinen an gespeicherter Position
  - [ ] Force-Simulation berücksichtigt gespeicherte Positionen (oder läuft nicht)
- [ ] Storage-Mechanismus:
  - [ ] Browser LocalStorage oder IndexedDB
  - [ ] Format: JSON mit Zettel-ID und Koordinaten
  - [ ] Fehlertoleranz: Auch bei Browser-Crash wiederherstellbar
- [ ] "Reset Layout" Button löscht alle gespeicherten Positionen

**Technische Hinweise:**
- localStorage.setItem('zettelweb-positions', JSON.stringify(positions))
- Debouncing für Storage-Writes (nicht bei jedem Frame!)
- Fallback wenn Storage voll

**Priorität:** 🔴 Must-Have
**Story Points:** 5
**Epic:** Persistence

**Test-Szenario:**
```
Gegeben: Zettel A bei default Position (100, 100)
Wenn: User zieht A zu (500, 300)
Dann: Position wird gespeichert

Wenn: User refresht Browser
Dann: Zettel A erscheint bei (500, 300)

Wenn: User klickt "Reset Layout"
Dann:
  - Gespeicherte Positionen werden gelöscht
  - Force-Simulation positioniert alles neu
```

---

#### FR-4.2: Graph-State persistieren 🟡

**Als** Nutzer
**will ich** dass Zoom-Level, Pan-Position und Filter-Einstellungen gespeichert werden,
**damit** ich beim Wiederkehren an der gleichen Stelle weitermachen kann.

**Akzeptanzkriterien:**
- [ ] Folgende Zustände werden gespeichert:
  - [ ] Zoom-Level (z.B. 150%)
  - [ ] Pan-Position (Canvas-Offset x, y)
  - [ ] Aktiver Tag-Filter (falls vorhanden)
- [ ] Speicherung erfolgt automatisch bei Änderung (mit Debouncing)
- [ ] Beim Reload:
  - [ ] Graph erscheint mit gleichem Zoom
  - [ ] Canvas ist an gleicher Position
  - [ ] Tag-Filter ist aktiv (falls vorher gesetzt)
- [ ] "Reset View" Button setzt alles auf Default zurück

**Technische Hinweise:**
- localStorage.setItem('zettelweb-state', JSON.stringify(state))
- Debouncing (z.B. 500ms nach letzter Änderung)
- Separate Keys für Positions vs. View-State

**Priorität:** 🟡 Should-Have
**Story Points:** 3
**Epic:** Persistence

**Test-Szenario:**
```
Gegeben: User hat Graph gezoomt (150%), gepanned und #projekt-Filter gesetzt
Wenn: User schließt Browser und öffnet später wieder
Dann:
  - Graph ist bei 150% Zoom
  - Canvas-Position ist gleich
  - #projekt-Filter ist aktiv
```

---

## ⚙️ NICHT-FUNKTIONALE ANFORDERUNGEN (NFRs)

**6 NFRs** zur Sicherstellung von Qualitätsattributen.

---

### NFR-1: Graph-Rendering Performance 🔴⭐

**Kategorie:** Performance

**Beschreibung:**
Das System soll auch bei vielen Zetteln flüssig und responsive bleiben.

**Messbare Kriterien:**
- **Framerate:** ≥30 fps während normaler Nutzung (Drag, Zoom, Pan)
- **Initial Render:** <3 Sekunden für 200 Zettel (vom API-Call bis sichtbarer Graph)
- **Interaktions-Latenz:** <100ms Reaktionszeit auf User-Input (Click, Drag-Start)
- **Smooth Animations:** Keine sichtbaren Ruckler (frame drops)
- **Skalierbarkeit:** Bei 300 Zetteln <20% Performance-Degradation (≥24 fps noch ok)

**Test-Methode:**
- Browser DevTools Performance Profiler
- FPS-Counter während verschiedener Operationen
- Benchmark mit Test-Datensets (200, 250, 300 Zettel)
- Lighthouse Performance Score >80

**Technische Strategie:**
- D3.js force simulation (O(n log n) mit Barnes-Hut approximation)
- Canvas 2D Rendering (performanter als DOM/SVG bei vielen Objekten)
- RequestAnimationFrame für Render-Loop (60fps target)
- Viewport-Culling (nur sichtbare Zettel rendern)
- Debouncing/Throttling für Storage-Writes

**Priorität:** 🔴 Must-Have (Kern-Qualitätsziel!)

**Akzeptanztest:**
```
Gegeben: Testdaten mit 200 Zetteln, 300 Verbindungen
Wenn: Graph gerendert und User performed Drag-Operation
Dann: FPS-Counter zeigt ≥30fps durchgehend

Gegeben: 300 Zettel im Graph
Wenn: User zoomt und panned
Dann: Keine sichtbaren Lags, smooth movement
```

---

### NFR-2: Browser-Kompatibilität 🔴

**Kategorie:** Kompatibilität

**Beschreibung:**
Das System soll in allen gängigen modernen Browsern funktionieren.

**Messbare Kriterien:**
- **Unterstützte Browser:**
  - Chrome/Edge 90+ (letzte 2 Major-Versionen)
  - Firefox 88+ (letzte 2 Major-Versionen)
  - Safari 15+ (macOS, iOS)
- **Screen-Größen:**
  - Desktop: 1920x1080 optimal, 1280x720 minimum
  - Tablet: 1024x768 nutzbar
  - Mobile: Nicht optimiert (Desktop-First)
- **Keine Polyfills nötig:** Native ES6+ Support vorausgesetzt
- **Canvas 2D Support:** Erforderlich

**Test-Methode:**
- Cross-Browser-Testing auf BrowserStack oder lokal
- Test auf verschiedenen Auflösungen
- Feature-Detection für kritische APIs (Canvas, LocalStorage, fetch)

**Priorität:** 🔴 Must-Have

**Akzeptanztest:**
```
Gegeben: ZettelWeb läuft
Wenn: Geöffnet in Chrome 120, Firefox 121, Safari 17
Dann: Graph funktioniert in allen Browsern identisch

Gegeben: 1280x720 Display
Wenn: ZettelWeb geöffnet
Dann: UI ist vollständig sichtbar, keine abgeschnittenen Elemente
```

---

### NFR-3: Usability - Intuitive Bedienung 🟡

**Kategorie:** Usability

**Beschreibung:**
Die Anwendung soll ohne Anleitung verständlich und bedienbar sein.

**Messbare Kriterien:**
- **Standard-Interaktionen:**
  - Zoom: Mouse Wheel (universell erwartet)
  - Pan: Drag auf leerem Canvas
  - Drag Zettel: Mouse Down + Move (wie bekannte Tools)
- **Visuelles Feedback:**
  - Hover-States für alle interaktiven Elemente
  - Cursor ändert sich (pointer, grab, grabbing)
  - Drag: Visueller "Lift-off" Effekt (Shadow, Highlight)
- **Discoverability:**
  - Wichtigste Funktionen in sichtbarer UI (Buttons, nicht versteckt)
  - Tooltips für alle Buttons
  - Keyboard Shortcuts optional (mit Anzeige)
- **Effizienz:**
  - Jede Hauptfunktion erreichbar in ≤3 Klicks
  - Keine tiefen Menü-Hierarchien

**Test-Methode:**
- Usability-Test mit 3 Test-Personen (nicht aus dem Team!)
- Task: "Finde einen Zettel, ändere seine Position, filtere nach Tag"
- Erfolgsrate: ≥80% ohne Hilfe
- System Usability Scale (SUS) Score ≥70 (durchschnittlich)

**Priorität:** 🟡 Should-Have

**Akzeptanztest:**
```
Gegeben: Test-Person ohne Vorkenntnisse
Wenn: Aufgabe gestellt: "Verschiebe einen Zettel"
Dann: Person schafft es innerhalb 30 Sekunden ohne Hilfe

Gegeben: Hover über Zettel
Wenn: Cursor über interaktivem Element
Dann: Cursor ändert sich zu "pointer", Tooltip erscheint
```

---

### NFR-4: Daten-Persistierung Zuverlässigkeit 🔴

**Kategorie:** Zuverlässigkeit / Data Integrity

**Beschreibung:**
Manuell positionierte Zettel und Einstellungen dürfen nicht verloren gehen.

**Messbare Kriterien:**
- **Speicher-Latenz:** Position-Update innerhalb 1 Sekunde nach Drag-Ende
- **Fehlertoleranz:**
  - Bei Browser-Crash: Daten bis letzte Speicherung wiederherstellbar
  - Bei vollem Storage: Fehlermeldung + Graceful Degradation (älteste Daten löschen)
- **Storage-Limit:** <10 MB für 500 Zettel (mit Positionen, State, Filter)
- **Daten-Format:** JSON (human-readable, debuggable)
- **Konsistenz:** Keine korrupten Daten nach Interrupt

**Test-Methode:**
- Crash-Recovery-Test: Browser hart killen während Drag
- Storage-Voll-Test: LocalStorage-Limit simulieren
- Daten-Integritäts-Check: JSON validation

**Priorität:** 🔴 Must-Have

**Akzeptanztest:**
```
Gegeben: User hat 50 Zettel manuell positioniert
Wenn: Browser crasht während Drag-Operation
Dann: Nach Neustart sind 49 Positionen gespeichert (letzte evtl. verloren)

Gegeben: LocalStorage ist fast voll
Wenn: System versucht neue Positionen zu speichern
Dann: Fehlermeldung "Storage voll" + Option alte Daten zu löschen
```

---

### NFR-5: Initial Load Time 🟡

**Kategorie:** Performance

**Beschreibung:**
Erste Anzeige des Graphen soll schnell erfolgen für gute User Experience.

**Messbare Kriterien:**
- **Time to Interactive (TTI):** <5 Sekunden (von URL-Eingabe bis Graph klickbar)
- **API Response Time:** Zettelstore /z Endpoint <1 Sekunde
- **Force-Simulation Stabilisierung:** <3 Sekunden bis Graph "zur Ruhe kommt"
- **Bundle Size:** <500 KB (gzipped) für JavaScript
- **Perceived Performance:** Loading-Spinner mit Fortschritts-Anzeige

**Test-Methode:**
- Lighthouse Performance Audit
- Network throttling (Slow 3G Simulation)
- Messung mit Performance API (performance.now())

**Priorität:** 🟡 Should-Have

**Akzeptanztest:**
```
Gegeben: Zettelstore mit 200 Zetteln auf localhost
Wenn: User öffnet ZettelWeb URL in Browser
Dann:
  - Nach <1s: Loading Spinner erscheint
  - Nach <3s: Graph ist sichtbar (evtl. noch animierend)
  - Nach <5s: Graph ist stabil und interaktiv

Lighthouse Score: Performance ≥80/100
```

---

### NFR-6: Wartbarkeit & Code-Qualität 🟢

**Kategorie:** Wartbarkeit

**Beschreibung:**
Code soll verständlich, strukturiert und erweiterbar sein.

**Messbare Kriterien:**
- **Dokumentation:**
  - JSDoc für alle öffentlichen Funktionen/Klassen
  - README mit Setup-Anleitung
  - Architecture Decision Records (ADRs) für wichtige Entscheidungen
- **Code-Struktur:**
  - Modulare Trennung (separate Dateien für Rendering, Physics, Storage, etc.)
  - Max. 200 Zeilen pro Funktion (Komplexität begrenzen)
  - Klar benannte Variablen/Funktionen (keine Abkürzungen wie `z`, `tmp`)
- **Linting:**
  - ESLint konfiguriert
  - 0 Errors, <10 Warnings
- **Version Control:**
  - Git mit aussagekräftigen Commit-Messages
  - Feature-Branches für neue Features

**Test-Methode:**
- ESLint Check in CI/CD
- Code Review vor Merge
- Onboarding-Test: Neues Team-Mitglied kann Code verstehen

**Priorität:** 🟢 Nice-to-Have (wichtig, aber nicht kritisch für Funktion)

**Akzeptanztest:**
```
Gegeben: Codebase
Wenn: ESLint ausgeführt
Dann: 0 Errors, <10 Warnings

Gegeben: Neues Team-Mitglied
Wenn: README gelesen, Code angeschaut
Dann: Kann grundlegende Änderung vornehmen (<2h Einarbeitung)
```

---

## ⛔ NICHT-ANFORDERUNGEN

**Explizit NICHT im Scope** von ZettelWeb v1.0.

Diese Features werden bewusst **nicht** implementiert, um Fokus und Realismus zu wahren.

---

### 1. Kollaboration & Multi-User ❌

**Ausgeschlossen:**
- Kein Multi-User-Modus (nur Single-User lokal)
- Keine gleichzeitige Bearbeitung durch mehrere Nutzer
- Keine Real-time Synchronisation zwischen Clients
- Kein User-Management / Rollen-System

**Begründung:**
Multi-User erhöht Komplexität massiv (WebSockets, Conflict Resolution, Locking). Zeitrahmen (1 Semester) ist zu kurz. Zettelstore selbst ist auch Single-User-fokussiert.

**Mögliche Zukunft (V2+):**
Wenn Zettelstore Multi-User-Support bekommt, könnte ZettelWeb das übernehmen. Aktuell keine Priorität.

---

### 2. Cloud-Speicherung & Synchronisation ❌

**Ausgeschlossen:**
- Keine Cloud-Speicherung von Positionen/State
- Keine Geräte-übergreifende Synchronisation (Desktop ↔ Laptop ↔ Tablet)
- Kein Online-Backup von Visualisierungs-Daten
- Keine Account-Verwaltung

**Begründung:**
Würde Backend-Server erfordern (Hosting, Wartung, Kosten). Fokus ist lokale Visualisierung. Zettelstore läuft lokal, ZettelWeb folgt diesem Ansatz.

**Alternativen:**
User können Zettelstore-Verzeichnis (inkl. Browser-Storage) manuell synchronisieren (Dropbox, Git, etc.).

---

### 3. Zettel-Inhalt-Bearbeitung ❌

**Ausgeschlossen:**
- Keine Zettel-Erstellung in ZettelWeb
- Keine Text-Bearbeitung von Zettel-Inhalten
- Keine Metadaten-Änderungen (Tags hinzufügen/entfernen, Titel ändern)
- Keine Zettel-Löschung
- Keine Verbindungs-Erstellung (nur Anzeige bestehender)

**Begründung:**
**Zettelstore ist Master** für alle Inhalte. ZettelWeb ist **View-Only Visualisierung**. Duplicate Editing-UI wäre Scope Creep und würde Sync-Probleme verursachen.

**Workflow:**
User editiert Zettel in Zettelstore → Refresh in ZettelWeb → Änderungen sichtbar.

**Mögliche Zukunft:**
"Quick Edit" Modal könnte Änderungen via Zettelstore API zurückschreiben. Aktuell nicht geplant.

---

### 4. Export & Import Features ❌

**Ausgeschlossen:**
- Kein Graph-Export als Bild (PNG, SVG, PDF)
- Kein Export der Visualisierungs-Daten (Positionen, Layout)
- Kein Import aus anderen Zettelkasten-Systemen (Obsidian, Roam Research, Notion)
- Kein "Share Graph" Feature (Link generieren)

**Begründung:**
Nice-to-Have, aber nicht Kern-Feature. Export erhöht Komplexität (Rendering zu Bild, Format-Konvertierung). Zeit besser in Kern-Features investiert.

**Workarounds:**
- Screenshot via Browser (Ctrl+Shift+S)
- Zettelstore selbst hat Export-Features für Inhalte

---

### 5. Erweiterte Visualisierungen ❌

**Ausgeschlossen:**
- Keine 3D-Visualisierung (WebGL 3D Graph)
- Keine Zeitleisten-Ansicht (Timeline basierend auf Zettel-Erstellungsdatum)
- Keine Hierarchische Tree-View
- Keine Mind-Map-Modus (radialer Layout)
- Keine Matrix-Ansicht
- Keine Heatmap (Zettel-Aktivität)

**Begründung:**
**Force-Directed Graph ist die gewählte Visualisierung** und ausreichend für Use-Case. Andere Layouts würden Komplexität und Wartungsaufwand multiplizieren. Fokus auf ein gutes Layout statt viele mittelmäßige.

**Mögliche Zukunft:**
Alternative Layout-Modi als Plugin-System (wenn Kern stabil).

---

### 6. UI-Anpassbarkeit ❌

**Ausgeschlossen:**
- Keine Schriftart-Änderung für Zettel-Titel
- Keine Schriftgröße-Anpassung (feste Größe)
- Keine Farb-Themes (Dark Mode / Light Mode)
- Keine UI-Layout-Anpassung (Sidebar-Position, Button-Größe)
- Keine Zettel-Stil-Anpassung (Form, Farbe pro Zettel)

**Begründung:**
Customization erhöht UI-Komplexität massiv (Settings-Menü, State-Management, Testing für alle Varianten). Standard-Design ist für Use-Case ausreichend.

**Ausnahme:**
Zoom-Level und Pan-Position sind anpassbar (Teil der Kern-Navigation, nicht "Customization").

---

### 7. Mobile-App & Touch-Optimierung ❌

**Ausgeschlossen:**
- Keine dedizierte Mobile-App (iOS, Android)
- Keine Touch-Gesten-Optimierung (Pinch-to-Zoom, Two-Finger-Pan)
- Kein Responsive Design für Smartphones
- Keine Progressive Web App (PWA) Features (Offline, Install)

**Begründung:**
**Desktop-First Anwendung.** Zettelkasten-Arbeit ist primär Desktop-Use-Case. Touch-Interaktionen mit vielen kleinen Zetteln sind schwierig. Zeitrahmen erlaubt keine zwei Plattformen.

**Minimale Tablet-Unterstützung:**
Auf Tablets (1024x768+) sollte es grundlegend funktionieren (mit Maus/Trackpad), aber nicht optimiert.

---

### 8. Offline-Modus ❌

**Ausgeschlossen:**
- Kein vollständiger Offline-Modus
- Keine Service Workers für Caching
- Kein "Work without Zettelstore" Modus

**Begründung:**
Zettelstore muss laufen und erreichbar sein (http://localhost:23123). ZettelWeb ist **Visualisierung für Zettelstore**, nicht eigenständige App. Offline-Support würde Daten-Caching und Sync-Logic erfordern → zu komplex.

**Funktioniert:**
Lokal (Zettelstore + ZettelWeb beide lokal) auch ohne Internet.

**Funktioniert NICHT:**
ZettelWeb öffnen wenn Zettelstore offline ist.

---

### 9. Authentication & Security ❌

**Ausgeschlossen:**
- Kein Login / User-Management
- Keine Passwort-Geschützte Graphen
- Keine Zugriffs-Beschränkungen (wer darf was sehen)
- Keine Verschlüsselung von gespeicherten Positionen
- Kein HTTPS-Erzwingung

**Begründung:**
**Lokale Anwendung** (localhost). Security ist Verantwortung von Zettelstore. Wenn Zettelstore geschützt ist, ist ZettelWeb automatisch geschützt. Zusätzliche Auth-Layer wäre Overkill für lokalen Use-Case.

**Falls Remote-Zugriff:**
User müssen Zettelstore hinter Reverse-Proxy mit Auth stellen (z.B. nginx + Basic Auth).

---

### 10. Erweiterte Physik-Features ❌

**Ausgeschlossen:**
- Keine manuell konfigurierbaren Physik-Parameter (Spring-Strength, Repulsion, etc.) in UI
- Keine "Freeze Node" Funktion (Zettel fixieren gegen Physik)
- Keine Collisions-Vermeidung (Zettel dürfen überlappen)
- Keine Animationen außer Force-Simulation (keine "Bounce", "Elastic Snap")

**Begründung:**
Erweiterte Physik-Kontrolle ist "Power-User" Feature. Für V1.0 reicht default D3.js Konfiguration. Drag & Drop erlaubt manuelle Positionierung (ersetzt "Freeze").

**Standard-Verhalten:**
D3.js default Physics-Parameter. Manuell gedraggede Zettel bleiben an Position (implizites "Freeze").

---

## 📦 ZUSAMMENFASSUNG

### Requirements Übersicht

| Kategorie | Anzahl | Must-Have | Should-Have | Nice-to-Have |
|-----------|--------|-----------|-------------|--------------|
| **Funktionale Requirements** | 11 Stories | 5 (24 SP) | 4 (16 SP) | 2 (5 SP) |
| **Nicht-Funktionale Requirements** | 6 NFRs | 3 | 2 | 1 |
| **Nicht-Anforderungen** | 10 Kategorien | - | - | - |
| **Gesamt Story Points** | 45 SP | ~90-100h Implementierung | | |

### Feature-Priorisierung

**🔴 Phase 1: MVP (Must-Have) - 60% Aufwand**
- Force-Directed Graph Visualisierung
- Zettel-Inhalt anzeigen (Click)
- Positionen persistieren
- Performance: 200 Zettel @ 30fps
- Browser-Kompatibilität

**Ziel:** Basis-Visualisierung funktioniert, benutzbar.
**Dauer:** 6-8 Wochen

**🟡 Phase 2: Enhanced (Should-Have) - 30% Aufwand**
- Drag & Drop
- Zoom & Pan
- Tag-Filterung
- Graph-State persistieren
- Usability-Verbesserungen

**Ziel:** Vollständige, intuitive Anwendung.
**Dauer:** 3-4 Wochen

**🟢 Phase 3: Polish (Nice-to-Have) - 10% Aufwand**
- Semi-transparente Filterung
- Hover-Highlighting
- Code-Qualität

**Ziel:** Finish, wenn Zeit übrig.
**Dauer:** 1-2 Wochen

### Erfolgskriterien

**Projekt gilt als erfolgreich wenn:**
- ✅ Alle Must-Have Features implementiert
- ✅ NFR-1 (Performance) erfüllt: 200 Zettel @ 30fps
- ✅ NFR-2 (Browser) erfüllt: Läuft in Chrome, Firefox, Safari
- ✅ NFR-4 (Persistence) erfüllt: Positionen bleiben gespeichert
- ✅ Professor-Review positiv (keine fundamentalen Fehler wie MVC-Diskussion!)
- ✅ Demo funktioniert live vor Team/Prof

**Nice-to-Have (Bonus):**
- ✅ Should-Have Features teilweise implementiert
- ✅ Lighthouse Score >80
- ✅ Usability-Test mit externen Personen erfolgreich

---

## 📚 REFERENZEN & RESOURCEN

### Technologie-Entscheidungen

Siehe separate Datei: [`TECHNICAL-CONSTRAINTS.md`](TECHNICAL-CONSTRAINTS.md)

**Key Stack:**
- **Frontend:** Vanilla JavaScript (oder Vue.js 3)
- **Graph-Library:** D3.js v7 (force simulation)
- **Rendering:** HTML5 Canvas 2D
- **Storage:** Browser LocalStorage / IndexedDB
- **API:** Zettelstore REST API

### Verwandte Dokumente

- [`wiki/Funktionale-Anforderungen.md`](wiki/Funktionale-Anforderungen.md) - User Stories detailliert
- [`wiki/Nicht-Funktionale-Anforderungen.md`](wiki/Nicht-Funktionale-Anforderungen.md) - NFRs detailliert
- [`wiki/Nicht-Anforderungen.md`](wiki/Nicht-Anforderungen.md) - Scope-Abgrenzung
- [`aufgaben-erklaert/REQUIREMENTS-CHANGELOG.md`](aufgaben-erklaert/REQUIREMENTS-CHANGELOG.md) - Was wurde geändert von V1.0

### Inspirationen

Ähnliche Tools (zur Orientierung, NICHT kopieren!):
- Obsidian Graph View
- Roam Research Graph
- Neo4j Bloom
- Gephi
- D3.js Force Examples

---

**Ende des Requirements-Dokuments**

Nächste Schritte: Siehe [Roadmap](#-zusammenfassung) für Implementierungs-Plan.

Bei Fragen oder Änderungswünschen: GitHub Issues erstellen oder Team-Meeting einberufen.
