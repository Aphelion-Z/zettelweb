# Funktionale Anforderungen - User Stories

**Projekt:** ZettelWeb
**Version:** 2.0
**Datum:** 2025-11-04
**Gesamt:** 11 User Stories, 45 Story Points

---

## 📋 Übersicht

| Epic | Stories | Story Points | Must/Should/Nice |
|------|---------|--------------|------------------|
| **Epic 1: Graph-Visualisierung** | 3 | 16 SP | 3x Must |
| **Epic 2: Interaktion** | 3 | 11 SP | 1x Must, 2x Should |
| **Epic 3: Filter & Fokus** | 3 | 10 SP | 1x Should, 2x Nice |
| **Epic 4: Persistence** | 2 | 8 SP | 1x Must, 1x Should |
| **GESAMT** | **11** | **45 SP** | 5M + 4S + 2N |

**Legende:**
- 🔴 Must-Have (5 Stories, 24 SP) - Kritisch für MVP
- 🟡 Should-Have (4 Stories, 16 SP) - Wichtig für Usability
- 🟢 Nice-to-Have (2 Stories, 5 SP) - Polish

---

## Epic 1: Graph-Visualisierung 🔴

### FR-1.1: Force-Directed Graph Layout anzeigen 🔴

**User Story:**
> Als Nutzer will ich alle Zettel als interaktiven Graphen mit automatischer Positionierung sehen, damit ich sofort erkenne welche Zettel miteinander verbunden sind.

**Akzeptanzkriterien:**
- [ ] Alle Zettel aus Zettelstore als Knoten dargestellt
- [ ] Zettel-Titel ist sichtbar/bei Hover
- [ ] Verbindungen als Linien gezeichnet
- [ ] Force-Directed Layout (Anziehung + Abstoßung)
- [ ] Simulation stabilisiert sich
- [ ] Graph sichtbar innerhalb 3s nach Laden
- [ ] Mind. 200 Zettel @ 30+ fps

**Technisch:**
- D3.js forceSimulation, forceLink, forceManyBody
- Canvas 2D Rendering
- Viewport-Culling

**Priorität:** 🔴 Must-Have
**Story Points:** 8
**Ready for GitHub Issue:** ✅

---

### FR-1.2: Visuelle Darstellung von Verbindungen 🔴

**User Story:**
> Als Nutzer will ich Verbindungen zwischen Zetteln als Linien sehen, damit ich Verknüpfungen erkenne.

**Akzeptanzkriterien:**
- [ ] Jede Verbindung = Linie
- [ ] Linien verbinden Zettel-Mittelpunkte/Ränder
- [ ] Linien deutlich sichtbar (konfigurierbar)
- [ ] Linien überlappen Zettel nicht
- [ ] Hover über Linie hebt Zettel hervor (optional)
- [ ] Bidirektionale Links = eine Linie

**Technisch:**
- Canvas lineTo()
- Collision detection

**Priorität:** 🔴 Must-Have
**Story Points:** 3
**Ready for GitHub Issue:** ✅

---

### FR-1.3: Initialer Graph-Load & Rendering 🔴

**User Story:**
> Als Nutzer will ich beim Öffnen automatisch den Graphen geladen bekommen, damit ich sofort explorieren kann.

**Akzeptanzkriterien:**
- [ ] App startet automatisch (kein "Load"-Button)
- [ ] Daten von Zettelstore API (GET /z)
- [ ] Loading-Indicator während Laden
- [ ] Fehler → Fehlermeldung + Retry
- [ ] Gespeicherte Positionen laden (falls vorhanden)
- [ ] Sonst: Force-Simulation initialisiert Layout

**Technisch:**
- fetch() für Zettelstore
- LocalStorage für Positionen
- Error Handling

**Priorität:** 🔴 Must-Have
**Story Points:** 5
**Ready for GitHub Issue:** ✅

---

## Epic 2: Interaktion 🔴🟡

### FR-2.1: Zettel-Inhalt anzeigen (Click) 🔴

**User Story:**
> Als Nutzer will ich durch Klick auf einen Zettel dessen Inhalt sehen, damit ich Informationen lesen kann.

**Akzeptanzkriterien:**
- [ ] Single-Click öffnet Detail-Ansicht
- [ ] Detail zeigt: Titel, Inhalt, Metadaten, verknüpfte Zettel
- [ ] Als Modal/Sidebar (nicht neues Fenster)
- [ ] "Schließen" Button / ESC-Taste
- [ ] Click auf verknüpften Zettel → öffnet diesen
- [ ] Markdown-Formatierung korrekt (falls Zettelstore nutzt)

**Technisch:**
- Modal-Component
- Markdown-Parser (marked.js)
- Canvas Click-Detection

**Priorität:** 🔴 Must-Have
**Story Points:** 3
**Ready for GitHub Issue:** ✅

---

### FR-2.2: Zettel manuell verschieben (Drag & Drop) 🟡

**User Story:**
> Als Nutzer will ich Zettel mit der Maus verschieben können, damit ich die Anordnung anpassen kann.

**Akzeptanzkriterien:**
- [ ] Mouse-Down startet Drag
- [ ] Zettel folgt Cursor smooth
- [ ] Visuelles Feedback (Cursor, Highlight)
- [ ] Mouse-Up beendet, Zettel bleibt
- [ ] Position sofort gespeichert
- [ ] Verbindungen bewegen sich mit
- [ ] Andere Zettel bewegen sich NICHT (Physik pausiert)
- [ ] Funktioniert bei Überlappung

**Technisch:**
- Canvas mouse events
- Collision detection
- Debouncing für Storage

**Priorität:** 🟡 Should-Have
**Story Points:** 5
**Ready for GitHub Issue:** ✅

---

### FR-2.3: Zoom & Pan Navigation 🟡

**User Story:**
> Als Nutzer will ich den Graphen zoomen und verschieben können, damit ich navigieren kann.

**Akzeptanzkriterien:**
- [ ] **Zoom:** Mouse Wheel, Zoom-Range 50%-200%, Zoom-Zentrum = Mausposition
- [ ] **Pan:** Drag auf leerem Canvas oder mittlere Maustaste
- [ ] **UI:** Zoom-Level angezeigt, "Fit to View" Button
- [ ] **Performance:** Flüssig (30+ fps)

**Technisch:**
- Canvas transform (scale, translate)
- RequestAnimationFrame

**Priorität:** 🟡 Should-Have
**Story Points:** 3
**Ready for GitHub Issue:** ✅

---

## Epic 3: Filter & Fokus 🟡🟢

### FR-3.1: Tag-basierte Filterung 🟡

**User Story:**
> Als Nutzer will ich nach Tags filtern können, damit ich nur Zettel zu einem Thema sehe.

**Akzeptanzkriterien:**
- [ ] Tag-Filter-Dropdown (alle Tags)
- [ ] Auswahl → nur Zettel mit Tag sichtbar
- [ ] Zettel ohne Tag ausgeblendet
- [ ] "Alle anzeigen" entfernt Filter
- [ ] Mehrfach-Auswahl möglich
- [ ] Filterung sofort
- [ ] Filter-State gespeichert

**Technisch:**
- Tag-Extraktion aus Metadaten
- Filter-Logic vor Rendering
- Multi-Select Dropdown

**Priorität:** 🟡 Should-Have
**Story Points:** 5
**Ready for GitHub Issue:** ✅

---

### FR-3.2: Semi-transparente externe Verbindungen 🟢

**User Story:**
> Als Nutzer will ich bei Tag-Filter auch verbundene Zettel außerhalb sehen (semi-transparent), damit ich Zusammenhänge erkenne.

**Akzeptanzkriterien:**
- [ ] Mit Tag: voll sichtbar (opacity 1.0)
- [ ] Ohne Tag aber verbunden: semi-transparent (opacity 0.3)
- [ ] Ohne Tag, nicht verbunden: komplett aus
- [ ] Linien innerhalb Filter: normal
- [ ] Linien zu semi-transparent: gestrichelt/heller
- [ ] Hover über semi-transparent → Tooltip
- [ ] Click auf semi-transparent → Detail-Ansicht

**Technisch:**
- Graph-Traversierung für connected nodes
- Opacity-Styling

**Priorität:** 🟢 Nice-to-Have
**Story Points:** 3
**Ready for GitHub Issue:** ✅

---

### FR-3.3: Hover-Highlighting verbundener Zettel 🟢

**User Story:**
> Als Nutzer will ich beim Hover sehen welche Zettel verbunden sind, damit ich Zusammenhänge schnell erkenne.

**Akzeptanzkriterien:**
- [ ] Hover über Zettel: dieser hervorgehoben
- [ ] Alle verbundenen hervorgehoben
- [ ] Andere gedimmt (opacity 0.3)
- [ ] Verbindungslinien dicker/farbig
- [ ] Effekt verschwindet bei Mouse-Out
- [ ] Funktioniert auch bei Tag-Filter
- [ ] Kein Lag

**Technisch:**
- Mousemove tracking
- Graph-Traversierung
- Temporary styling

**Priorität:** 🟢 Nice-to-Have
**Story Points:** 2
**Ready for GitHub Issue:** ✅

---

## Epic 4: Persistence 🔴🟡

### FR-4.1: Zettel-Positionen persistieren 🔴

**User Story:**
> Als Nutzer will ich dass manuell verschobene Zettel bleiben, damit ich beim nächsten Öffnen die Anordnung wiederfinde.

**Akzeptanzkriterien:**
- [ ] Nach Drag: Position (x,y) gespeichert
- [ ] Automatisch (kein "Save"-Button)
- [ ] Speicherung ≤1s nach Drag-Ende
- [ ] Beim Reload: Positionen geladen
- [ ] Zettel an gespeicherter Position
- [ ] Storage: LocalStorage/IndexedDB, JSON-Format
- [ ] Fehlertoleranz: Bei Crash wiederherstellbar
- [ ] "Reset Layout" löscht Positionen

**Technisch:**
- localStorage.setItem
- Debouncing für Writes
- Fallback bei vollem Storage

**Priorität:** 🔴 Must-Have
**Story Points:** 5
**Ready for GitHub Issue:** ✅

---

### FR-4.2: Graph-State persistieren 🟡

**User Story:**
> Als Nutzer will ich dass Zoom, Pan und Filter gespeichert werden, damit ich an gleicher Stelle weitermache.

**Akzeptanzkriterien:**
- [ ] Gespeichert: Zoom-Level, Pan-Position, Aktiver Tag-Filter
- [ ] Automatisch bei Änderung (mit Debouncing)
- [ ] Beim Reload: Graph mit gleichem Zoom, Pan, Filter
- [ ] "Reset View" setzt auf Default

**Technisch:**
- localStorage.setItem für State
- Debouncing (500ms)
- Separate Keys

**Priorität:** 🟡 Should-Have
**Story Points:** 3
**Ready for GitHub Issue:** ✅

---

## 🎯 Implementierungs-Roadmap

### Phase 1: MVP (Must-Have) - 6-8 Wochen

**Stories:** FR-1.1, FR-1.2, FR-1.3, FR-2.1, FR-4.1
**Story Points:** 24 SP
**Ziel:** Basis-Visualisierung funktioniert, nutzbar

**Definition of Done:**
- Alle 5 Must-Have Stories implementiert
- NFR-1 (Performance 200@30fps) erfüllt
- Manual Testing erfolgreich
- Demo-fähig

### Phase 2: Enhanced (Should-Have) - 3-4 Wochen

**Stories:** FR-2.2, FR-2.3, FR-3.1, FR-4.2
**Story Points:** 16 SP
**Ziel:** Vollständige, intuitive Anwendung

**Definition of Done:**
- Should-Have Features funktionieren
- Usability-Test mit 3 Personen positiv
- Browser-Testing (Chrome, Firefox, Safari)

### Phase 3: Polish (Nice-to-Have) - 1-2 Wochen

**Stories:** FR-3.2, FR-3.3
**Story Points:** 5 SP
**Ziel:** Final Touch, wenn Zeit

**Definition of Done:**
- Nice-to-Have Features implementiert
- Code-Review abgeschlossen
- Lighthouse Score >80

---

## ✅ GitHub Issue Template

Für jede User Story ein GitHub Issue erstellen mit diesem Format:

```markdown
## User Story

Als [Rolle] will ich [Funktion] damit [Nutzen].

## Akzeptanzkriterien

- [ ] Kriterium 1
- [ ] Kriterium 2
- [ ] ...

## Technische Hinweise

[Details zur Implementierung]

## Definition of Done

- [ ] Code implementiert
- [ ] Manual Test erfolgreich
- [ ] Code reviewed
- [ ] Merged in main

## Labels

- `feature`
- `must-have` / `should-have` / `nice-to-have`
- Epic: `graph-viz` / `interaction` / `filter` / `persistence`

## Story Points

[1, 2, 3, 5, 8]

## Milestone

Phase 1 / Phase 2 / Phase 3
```

---

**Nächste Schritte:**
1. Diese Stories als GitHub Issues anlegen
2. Labels & Milestones in GitHub einrichten
3. Planning Poker für finale Story Point-Bestätigung
4. Sprint Planning für Phase 1

---

**Siehe auch:**
- [REQUIREMENTS.md](../REQUIREMENTS.md) - Vollständiges Requirements-Dokument
- [Nicht-Funktionale-Anforderungen.md](Nicht-Funktionale-Anforderungen.md) - NFRs
- [Nicht-Anforderungen.md](Nicht-Anforderungen.md) - Scope-Abgrenzung
