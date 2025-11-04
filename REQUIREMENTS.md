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

**Beschreibung:**

Dies ist das **absolute Kernfeature** von ZettelWeb und der Hauptgrund, warum diese Anwendung existiert. Während Zettelstore Zettel als einfache, chronologische Liste darstellt, visualisiert ZettelWeb die gesamte Zettel-Sammlung als lebendigen, interaktiven Graphen mit physik-basiertem Layout.

**Warum ist das wichtig?**

Bei einer Zettelkasten-Methode mit 50, 100 oder mehr Zetteln verliert man in einer reinen Listen-Ansicht schnell die Übersicht über die Struktur des eigenen Wissens. Man sieht nicht:
- Welche Zettel sind zentrale "Hub"-Zettel mit vielen Verbindungen?
- Welche Themen-Cluster existieren in meinem Zettelkasten?
- Welche Zettel sind isoliert und könnten besser vernetzt werden?
- Wie hängen verschiedene Gedankenstränge zusammen?

Der force-directed Graph macht diese Struktur **sofort sichtbar**. Das menschliche Gehirn ist extrem gut darin, räumliche Muster zu erkennen - genau das nutzt diese Visualisierung aus.

**Wie funktioniert es technisch?**

Das System verwendet ein **physikalisches Simulations-Modell** zur automatischen Positionierung der Zettel:

- **Anziehungskraft (Spring Force):** Zettel, die durch Links verbunden sind, ziehen sich gegenseitig an, als wären sie durch Federn verbunden. Je näher zwei verlinkte Zettel beieinander sind, desto "entspannter" ist die Feder.

- **Abstoßungskraft (Repulsion/Charge Force):** Alle Zettel stoßen sich gegenseitig ab, ähnlich wie gleichnamige elektrische Ladungen. Das verhindert, dass unverbundene Zettel übereinander liegen.

- **Zentrierung:** Eine schwache Kraft zieht alle Zettel leicht zum Zentrum des Bildschirms, damit der Graph nicht "davon schwebt".

- **Simulation:** Diese Kräfte wirken in jeder Animation-Frame, bis sich ein stabiles Equilibrium einstellt (üblicherweise nach 3-5 Sekunden).

**Resultat:** Stark vernetzte Zettel landen automatisch zentral im Graph, Themen-Cluster gruppieren sich natürlich, isolierte Zettel driften an den Rand.

**Was gehört NICHT dazu?**

- **KEIN manuelles Grid/Tree-Layout:** Die Positionen werden ausschließlich durch die Physik-Simulation bestimmt (manuelles Feintuning ist nur via Drag & Drop in FR-2.2 möglich).
- **KEINE alternativen Layout-Algorithmen:** Kein hierarchisches, radiales oder Circular Layout - nur force-directed.
- **KEINE 3D-Visualisierung:** Der Graph bleibt 2-dimensional. 3D würde Navigation erschweren und ist für Zettelkasten-Strukturen nicht nötig.

**Kontext zur Vision:**

Dieses Feature basiert direkt auf den Vision-PDFs, wo explizit beschrieben wurde:
> "Die Position und Entfernung der jeweiligen Zettel [...] soll den Verbindungen und Zetteln selbst passen [...] je nachdem welcher Zettel wie viele Verbindungen mit welchen Zetteln hat"

Die Physik-basierten Werte (Anziehung, Abstoßung, Koordinaten) waren Kern der ursprünglichen Idee.

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

**Beschreibung:**

Während FR-1.1 die Zettel selbst darstellt, sorgt diese Anforderung dafür, dass die **Beziehungen** zwischen Zetteln visuell erkennbar werden. In einem Zettelkasten-System sind Verbindungen genauso wichtig wie die Zettel selbst - sie repräsentieren den Zusammenhang von Gedanken und Wissens-Strukturen.

**Warum ist das wichtig?**

Die Kraft eines Zettelkastens liegt nicht in einzelnen isolierten Notizen, sondern in deren Vernetzung. Luhmanns Zettelkasten wurde so wertvoll, weil Zettel systematisch aufeinander verwiesen. In der Graph-Visualisierung müssen diese Links daher klar sichtbar sein:
- **Welche Zettel sind direkt miteinander verbunden?**
- **Wie dicht ist ein Themen-Cluster vernetzt?**
- **Welche Zettel sind Brücken zwischen verschiedenen Themenbereichen?**

Ohne sichtbare Verbindungen wäre der Graph nur eine Sammlung von Punkten ohne erkennbare Struktur.

**Wie funktioniert es?**

Für jeden Link zwischen zwei Zetteln (z.B. Zettel A verlinkt auf Zettel B) wird eine **durchgezogene Linie** gezeichnet:

1. **Start-/Endpunkt:** Die Linie beginnt am Rand von Zettel A und endet am Rand von Zettel B (nicht im Zentrum, sonst würden Linien unter den Zetteln verschwinden).

2. **Collision Detection:** Das System berechnet die Schnittpunkte der Linie mit den Zettel-Grenzen, sodass die Linie genau dort endet wo der Zettel beginnt.

3. **Bidirektionale Links:** Wenn Zettel A auf B verweist UND B auf A, wird trotzdem nur EINE Linie gezeichnet (keine doppelten Linien).

4. **Styling:** Linienfarbe und -dicke sind konfigurierbar (z.B. graue, semi-transparente Linien als Standard, damit sie den Graphen nicht überladen).

**Was gehört NICHT dazu?**

- **KEINE gerichteten Pfeile:** Linien sind einfache Striche ohne Pfeilspitzen (die Richtung des Links ist im Detail-View sichtbar, nicht im Graph selbst).
- **KEINE Linien-Labels:** Keine Beschriftungen auf den Linien (z.B. "ist verwandt mit" - das würde den Graph überladen).
- **KEINE Curved/Bezier-Linien:** Nur gerade Linien für Performance und Klarheit (curved lines würden bei 200+ Zetteln zu viel CPU-Last erzeugen).

**Technische Überlegung:**

Bei 200 Zetteln mit durchschnittlich 1.5 Links pro Zettel entstehen ~300 Linien. Diese müssen in jedem Frame (30-60x pro Sekunde) neu gerendert werden, daher ist Performance kritisch:
- Canvas `lineTo()` ist schneller als SVG `<line>` Elemente
- Linien nur im sichtbaren Viewport rendern (Viewport Culling)

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

**Beschreibung:**

Diese Anforderung definiert den **gesamten Startprozess** von ZettelWeb - vom Öffnen der URL bis zum sichtbaren, interaktiven Graphen. Sie orchestriert das Zusammenspiel von API-Zugriff, Daten-Verarbeitung, Position-Wiederherstellung und Initial-Rendering.

**Warum ist das wichtig?**

Der erste Eindruck entscheidet: Wenn ein Nutzer ZettelWeb öffnet und 10 Sekunden auf einen weißen Bildschirm starrt, wird er frustriert sein und die Anwendung verlassen. Eine gute User Experience erfordert:
- **Unmittelbares Feedback:** Loading-Indicator zeigt, dass etwas passiert
- **Schneller Time-to-Interactive:** <3 Sekunden bis der Graph sichtbar ist
- **Fehlertoleranz:** Klare Fehlermeldungen wenn Zettelstore nicht erreichbar ist
- **Smart Loading:** Gespeicherte Positionen wiederherstellen statt jedes Mal neu zu simulieren

Diese Anforderung ist der "Kleber" zwischen allen anderen Features - ohne einen funktionierenden Load-Prozess würde nichts anderes funktionieren.

**Wie funktioniert der Load-Prozess?**

Der Ablauf beim App-Start ist sequentiell:

1. **URL aufgerufen:** Browser lädt HTML/CSS/JavaScript
2. **App initialisiert:** JavaScript startet, Canvas-Element wird vorbereitet
3. **Loading-Indicator:** Spinner wird angezeigt ("Laden...")
4. **API-Call:** `fetch('http://zettelstore:23123/z')` holt alle Zettel-Daten
5. **Daten parsen:** JSON wird in Zettel-Objekte + Link-Liste umgewandelt
6. **Position-Check:** LocalStorage prüfen - gibt es gespeicherte Positionen?
   - **JA:** Positionen laden und direkt rendern (sofort fertig, keine Simulation!)
   - **NEIN:** Force-Simulation starten (Zettel bewegen sich 3-5 Sekunden)
7. **Graph rendern:** Canvas wird zum ersten Mal gezeichnet
8. **Loading entfernen:** Spinner verschwindet, Graph ist interaktiv

**Time-to-Interactive (TTI):** Maximal 3 Sekunden von Schritt 3 bis Schritt 8.

**Was gehört NICHT dazu?**

- **KEIN manueller "Load"-Button:** Die App lädt automatisch, nicht erst nach User-Aktion.
- **KEINE Pagination:** Alle Zettel werden auf einmal geladen (keine "Lade mehr..."-Buttons).
- **KEIN Progressive Loading:** Kein Rendering von erst 50, dann 100, dann 200 Zetteln - sondern alle gleichzeitig.

**Fehlerbehandlung:**

Wenn der Zettelstore nicht erreichbar ist (z.B. nicht gestartet, falsche URL, Netzwerkfehler):
- **User-freundliche Nachricht:** "Zettelstore ist nicht erreichbar. Bitte starten Sie Zettelstore und versuchen Sie es erneut."
- **Retry-Option:** Button "Nochmal versuchen" ruft den Load-Prozess erneut auf
- **Technische Details (optional):** In Developer Console: Genaue Fehlermeldung + Zettelstore-URL

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

**Beschreibung:**

Der Graph zeigt die **Struktur** des Zettelkastens, aber um wirklich mit den Zetteln zu arbeiten, muss der Nutzer die **Inhalte** lesen können. Diese Anforderung macht ZettelWeb zu einer echten Read-Only-Visualisierung des Zettelkastens, nicht nur zu einem abstrakten Netzwerk-Diagramm.

**Warum ist das wichtig?**

Ein Graph ohne Inhalts-Anzeige wäre wie ein Stadtplan ohne Straßennamen - man sieht die Struktur, aber kann nichts Konkretes damit anfangen. Der Nutzer muss:
- **Zettel lesen können,** um zu entscheiden ob ein Zettel relevant ist
- **Metadaten sehen** (Tags, Datum) für Kontext
- **Verknüpfte Zettel finden,** um von einem Gedanken zum nächsten zu springen
- **Markdown-Formatierung erkennen** (Überschriften, Listen, Links) für bessere Lesbarkeit

Dies ist die Brücke zwischen "Graph ansehen" und "Wissensarbeit leisten".

**Wie funktioniert es?**

1. **Click-Detection:** Wenn der Nutzer auf einen Punkt im Canvas klickt, berechnet das System welcher Zettel (falls vorhanden) getroffen wurde (Hit-Testing).

2. **Zettel-Daten laden:** Für den geklickten Zettel wird ein API-Call zu Zettelstore gemacht: `GET /z/{zettel-id}` um den vollständigen Inhalt zu holen.

3. **Detail-View rendern:** Ein Modal oder Sidebar erscheint mit:
   - **Titel:** Groß und prominent (z.B. H1)
   - **Inhalt:** Vollständiger Zettel-Text, Markdown → HTML gerendert
   - **Metadaten:** Tags als Chips, Erstellungsdatum, Zettel-ID
   - **Verknüpfungen:** Liste aller verlinkten Zettel als anklickbare Links
   - **Schließen-Button:** X-Icon oben rechts

4. **Navigation:** Klick auf einen verlinkten Zettel in der Liste lädt diesen Zettel im gleichen Modal (kein neues Fenster öffnen).

**Was gehört NICHT dazu?**

- **KEIN Bearbeiten:** Zettel-Inhalt ist Read-Only! Keine Textfelder, kein "Speichern"-Button. (Siehe Nicht-Anforderung #3: ZettelWeb ist reine Visualisierung)
- **KEIN neues Fenster:** Detail-View öffnet sich als Overlay, nicht als Browser-Tab
- **KEINE Zettel-Erstellung:** Kein "Neuer Zettel"-Button

**Technische Überlegung:**

Markdown-Rendering (z.B. via marked.js) muss **XSS-sicher** sein - Zettel-Inhalte könnten `<script>` Tags enthalten. Daher: Sanitizing aktivieren!

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

**Beschreibung:**

Während FR-1.1 Zettel automatisch durch Physik-Simulation positioniert, gibt diese Anforderung dem Nutzer die **Kontrolle zurück**. Sie ermöglicht manuelles Feintuning des automatischen Layouts - das Beste aus beiden Welten.

**Warum ist das wichtig?**

Die automatische Force-Directed-Positionierung ist gut, aber nicht perfekt:
- **Manchmal überlappen Zettel** trotz Abstoßungskraft leicht
- **Manchmal möchte der Nutzer eine bestimmte Anordnung** (z.B. wichtige Zettel oben links)
- **Manchmal stabilisiert sich die Simulation suboptimal** (lokales statt globales Optimum)

Drag & Drop gibt dem Nutzer die Möglichkeit, diese Probleme zu beheben und den Graphen nach persönlichen Vorlieben anzupassen - ohne die automatische Positionierung komplett zu verlieren.

**Wie funktioniert es?**

Der Drag-Prozess läuft in drei Phasen:

1. **Mouse-Down (Drag Start):**
   - Hit-Testing: Welcher Zettel wurde geklickt?
   - Physik-Simulation **pausieren** (sonst würde der Zettel zurück "schnappen")
   - Visuelles Feedback: Cursor wird zu "grab" (Hand-Symbol)

2. **Mouse-Move (Dragging):**
   - Zettel folgt Maus-Position in jedem Frame
   - **Verbindungslinien werden live aktualisiert** (bewegen sich mit)
   - Andere Zettel bleiben wo sie sind (keine Domino-Effekt)

3. **Mouse-Up (Drag End):**
   - Zettel bleibt an neuer Position "fixiert"
   - Position wird **sofort in LocalStorage gespeichert**
   - Cursor zurück zu "default"

**Performance-Trick:** Position wird erst nach Drag-Ende gespeichert, nicht bei jedem Pixel-Movement (Debouncing!).

**Was gehört NICHT dazu?**

- **KEINE automatische Anpassung anderer Zettel:** Nur der gedraggede Zettel bewegt sich, andere bleiben statisch (kein "Push away"-Verhalten)
- **KEINE Multi-Selection:** Nur ein Zettel auf einmal draggen, nicht mehrere gleichzeitig
- **KEIN Touch-Support:** Nur Maus, keine Touch-Gesten (siehe Nicht-Anforderung #7: Desktop-First)

**Beziehung zu FR-4.1:**

Diese Funktion ist eng mit FR-4.1 (Position-Persistierung) verbunden - ohne Speicherung wäre Drag & Drop sinnlos, da beim Reload alles zurückspringen würde.

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

**Beschreibung:**

Bei 200+ Zetteln auf einem Bildschirm ist es unmöglich, alle Details gleichzeitig zu sehen. Diese Anforderung macht den Graphen zu einem navigierbaren Raum - ähnlich wie Google Maps, aber für Wissen. Zoom & Pan sind essenzielle Navigation-Tools für große Graphen.

**Warum ist das wichtig?**

Ein statischer, nicht-zoombarer Graph wäre extrem limitiert:
- **Bei 200 Zetteln:** Zettel-Titel wären mikroskopisch klein und unleserlich
- **Ohne Pan:** Nur der Zentrale Bereich des Graphen wäre sichtbar, Rand-Zettel unerreichbar
- **Ohne Zoom:** Kein Wechsel zwischen Überblick (alle Cluster sehen) und Detail (einzelnen Zettel lesen)

Zoom & Pan ermöglichen die "Zoom-in/Zoom-out"-Exploration: Erst Überblick gewinnen, dann in interessante Bereiche zoomen.

**Wie funktioniert es?**

**Zoom:**
- **Eingabe:** Mouse Wheel (hoch = Zoom In, runter = Zoom Out)
- **Zoom-Faktor:** Jeder Wheel-Tick ändert Zoom um ~10% (z.B. 100% → 110% → 121%)
- **Zoom-Zentrum:** Die Position unter dem Maus-Cursor bleibt fix (nicht Canvas-Mitte!) - das fühlt sich natürlich an
- **Grenzen:** 50% (halbe Größe, mehr Überblick) bis 200% (doppelte Größe, Details)

**Pan:**
- **Eingabe:** Drag auf leerem Canvas (Hintergrund, nicht auf Zettel) ODER mittlere Maustaste + Drag
- **Mechanik:** Canvas wird verschoben, Zettel bleiben relativ zueinander an gleicher Position
- **Smooth:** Transformation wird per RequestAnimationFrame gerendert, keine Sprünge

**UI-Feedback:**
- Zoom-Level-Anzeige: "125%" in Ecke des Bildschirms
- "Fit to View"-Button: Berechnet optimalen Zoom sodass alle Zettel sichtbar sind + zentriert den Graphen

**Was gehört NICHT dazu?**

- **KEINE Zoom-Buttons:** Nur Mouse Wheel, keine +/- Buttons (kann in v2.0 ergänzt werden)
- **KEINE Minimap:** Keine kleine Übersichtskarte in der Ecke (wäre Nice-to-Have für v2.0)
- **KEIN Zoom auf einzelnen Zettel:** Zoom betrifft immer ganzen Graph, nicht nur einen Zettel

**Performance-Kritisch:**

Zoom/Pan passiert kontinuierlich (bei Wheel-Scroll oder Drag), daher muss Rendering extrem schnell sein. Canvas transform ist hier performanter als Neuberechnung aller Koordinaten.

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

**Beschreibung:**

Bei einem großen Zettelkasten mit vielfältigen Themen (Projekt, Philosophie, Rezepte, Code-Snippets, etc.) wird der Graph schnell überladen. Tag-basierte Filterung ermöglicht **fokussiertes Arbeiten** - der Nutzer blendet alles aus außer dem aktuellen Interessensgebiet.

**Warum ist das wichtig?**

Ein ungefilteter Graph mit 200 Zetteln aus 10 verschiedenen Themenbereichen ist **kognitiv überwältigend**:
- Zu viele visuelle Stimuli → Nutzer findet wichtige Informationen nicht
- Irrelevante Zettel lenken ab ("Warum sehe ich Rezepte wenn ich an meinem Projekt arbeite?")
- Struktur eines spezifischen Themas ist schwer erkennbar

Filterung macht aus einem allgemeinen Wissens-Netz ein **themen-spezifisches Arbeits-Werkzeug**. Wie ein Suchscheinwerfer, der nur einen Bereich beleuchtet.

**Wie funktioniert es?**

1. **Tag-Extraktion:** System sammelt alle Tags aus allen Zetteln (z.B. `#projekt`, `#philosophie`, `#code`)

2. **Filter-UI:** Dropdown/Multi-Select in der Toolbar zeigt alle verfügbaren Tags

3. **Filter-Anwendung:**
   - User wählt z.B. `#projekt`
   - **Sichtbar:** Nur Zettel die `#projekt` haben (opacity 1.0)
   - **Ausgeblendet:** Alle anderen Zettel (opacity 0 oder entfernt)
   - **Verbindungen:** Nur Linien zwischen sichtbaren Zetteln werden gezeichnet

4. **Mehrfach-Filter:** User kann `#projekt` UND `#wichtig` wählen → nur Zettel die BEIDE Tags haben

5. **Filter entfernen:** "Alle anzeigen" → Graph kehrt zu ungefiltert zurück

**Was gehört NICHT dazu?**

- **KEINE Volltext-Suche:** Nur Tag-Filter, nicht Suche im Zettel-Inhalt (das wäre FR-3.X in v2.0)
- **KEINE negativen Filter:** Kein "Zeige alles AUSSER #rezepte" (nur positive Auswahl)
- **KEINE Tag-Kombinationen (OR):** Nur UND-Verknüpfung (`#a UND #b`), nicht ODER (`#a ODER #b`)

**Beziehung zu FR-3.2:**

FR-3.2 erweitert diese Anforderung um semi-transparente Darstellung von verbundenen Zetteln außerhalb des Filters - das vermeidet "tote Enden" im gefilterten Graphen.

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

**Beschreibung:**

Dies ist das **innovativste UX-Feature** von ZettelWeb - eine Idee aus den ursprünglichen Vision-PDFs, die in kommerziellen Graph-Tools oft fehlt. Es löst ein fundamentales Problem von Filterung: **Kontext-Verlust**. Wenn man nur gefilterte Zettel sieht, verliert man Verbindungen zu verwandten Themen.

**Warum ist das wichtig?**

Stell dir vor, du filterst nach `#projekt`, aber ein wichtiger Zettel hat Tag `#architektur` und ist mit deinem Projekt verbunden. Normale Filterung würde diesen Zettel komplett ausblenden - du würdest eine "tote Ende"-Verbindung sehen, ohne zu wissen wohin sie führt.

Semi-transparente Darstellung gibt **kontextuellen Hinweis**:
- "Hier gibt es etwas Verbundenes, auch wenn es außerhalb meines Filters liegt"
- Nutzer kann entscheiden: "Interessant, lass mich draufklicken" oder "Okay, ignorieren"

Dies ist besonders wertvoll für **interdisziplinäres Denken** - Verbindungen zwischen Themen sind oft die interessantesten Einsichten.

**Wie funktioniert es?**

Wenn Tag-Filter aktiv ist (z.B. `#projekt`), durchläuft das System alle Zettel in 3 Kategorien:

1. **Kategorie 1 (voll sichtbar):**
   - Zettel hat den Filter-Tag → Opacity 1.0, normale Darstellung

2. **Kategorie 2 (semi-transparent):**
   - Zettel hat NICHT den Filter-Tag
   - ABER: Zettel ist mit mindestens einem Kategorie-1-Zettel verbunden
   - → Opacity 0.3, Titel erkennbar aber gedimmt

3. **Kategorie 3 (ausgeblendet):**
   - Zettel hat NICHT den Filter-Tag
   - UND: Keine Verbindung zu Kategorie-1-Zetteln
   - → Opacity 0 oder komplett entfernt

**Verbindungslinien:**
- Innerhalb Kategorie 1: Normale Linien
- Zwischen Kategorie 1 ↔ 2: Gestrichelte oder hellere Linien (visueller Hinweis "externes Element")

**Was gehört NICHT dazu?**

- **KEINE transitive Verbindung:** Nur direkte Nachbarn werden semi-transparent, nicht "Nachbarn von Nachbarn"
- **KEINE Kategorie-Anzeige:** Keine visuelle Markierung "Dies ist ein semi-transparenter Zettel" außer der Opacity
- **KEIN Dimming von Linien:** Linien zu semi-transparenten Zetteln sind sichtbar, nur anders gestylt

**Vision-Ursprung:**

Direktes Zitat aus "Zettelweb Idee.pdf":
> "Wenn ein Zettel bei der „Tag"-Darstellung trotzdem eine Verknüpfung zu einem anderen Zettel hat, welcher NICHT das gleiche „Tag" verwendet, könnte dieser trotzdem angezeigt werden, jedoch stark ausgegraut/ semitransparent"

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

**Beschreibung:**

Dieses Feature bietet **sofortiges visuelles Feedback** beim Explorieren des Graphen. Statt jeden Zettel anzuklicken um Verbindungen zu sehen, reicht ein Hover um die direkte Nachbarschaft zu erkennen - wie ein "Spotlight" auf Teile des Netzwerks.

**Warum ist das wichtig?**

Bei 200 Zetteln und 300+ Verbindungen ist der Graph visuell dicht. Linien überkreuzen sich, es ist schwer zu sagen "Welche Zettel sind eigentlich mit diesem hier verbunden?".

Hover-Highlighting macht Verbindungen **instantly erkennbar**:
- Keine mentale Linie-Verfolgung nötig ("Geht diese Linie zu dem Zettel... oder dem da?")
- Schnelle Exploration ("Aha, dieser Zettel ist mit 5 anderen verbunden, interessant!")
- Kein Klick erforderlich (nicht-invasiv, sofortiges Feedback)

Dies ist besonders nützlich in **dicht vernetzten Bereichen** des Graphen, wo viele Linien sich kreuzen.

**Wie funktioniert es?**

Der Hover-Effekt ist ein **temporärer visueller State** (keine Daten-Änderung):

1. **Mousemove-Tracking:** System erkennt wenn Maus über einen Zettel ist (Hit-Testing)

2. **Highlight aktivieren:**
   - **Gehoverter Zettel:** Visuell hervorheben (z.B. dickerer Rand, andere Farbe, leicht größer)
   - **Verbundene Zettel:** Ebenfalls hervorheben (gleicher Stil oder leicht anders)
   - **Alle anderen Zettel:** Dimmen (Opacity 0.3) um Fokus zu schaffen
   - **Verbindungslinien zum gehover-ten Zettel:** Dicker oder farbig machen

3. **Mouse-Out:** Sofort zurück zu normalem State (alle Zettel wieder gleich sichtbar)

**Performance:** Da Hover kontinuierlich passiert (Maus bewegt sich ständig), muss das Re-Rendering extrem schnell sein (keine Lag-Spikes!).

**Was gehört NICHT dazu?**

- **KEINE Transitive Hervorhebung:** Nur direkte Nachbarn (1-Hop), nicht "Nachbarn von Nachbarn" (2-Hops)
- **KEIN Hover-Lock:** Kein "Klick um Highlight zu fixieren" - Effekt verschwindet immer bei Mouse-Out
- **KEINE Hover-Delay:** Effekt erscheint sofort, kein 500ms Tooltip-Delay

**Kombination mit FR-3.2:**

Wenn Tag-Filter + Semi-Transparenz aktiv ist, funktioniert Hover trotzdem - auch semi-transparente Zettel können gehover-t werden.

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

**Beschreibung:**

Diese Anforderung ist der **Grund, warum manuelles Drag & Drop überhaupt Sinn macht**. Ohne Persistierung würde jeder Browser-Reload oder App-Neustart alle mühsam arrangierten Positionen zerstören - ein extrem frustrierendes Erlebnis.

**Warum ist das kritisch?**

Stell dir vor:
- User verbringt 10 Minuten damit, den Graphen nach persönlichen Vorlieben anzuordnen
- Wichtige Projekt-Zettel oben links, Referenzen unten rechts, etc.
- Browser-Refresh → **POOF**, alles zurück zur Physik-Simulation-Position
- User muss alles neu arrangieren → Kompletter Arbeitsverlust

Mit Persistierung wird der Graph zu einem **persönlichen Workspace**, der über Sessions hinweg erhalten bleibt - wie ein Desktop, wo Icons bleiben wo man sie hingelegt hat.

**Wie funktioniert es?**

Die Persistierung arbeitet in zwei Richtungen: **Speichern** und **Laden**.

**1. Speichern (nach Drag & Drop):**

Nach jedem erfolgreichen Drag (FR-2.2) wird die neue Position gespeichert:

```javascript
// Pseudo-Code
function onDragEnd(zettelId, newX, newY) {
  positions[zettelId] = { x: newX, y: newY };
  saveToStorage(positions); // Debounced!
}
```

**Storage-Format (JSON in LocalStorage):**
```json
{
  "version": "1.0",
  "positions": {
    "20251027134512": { "x": 450.5, "y": 320.8 },
    "20251028091234": { "x": 120.0, "y": 500.3 }
  }
}
```

**2. Laden (bei App-Start in FR-1.3):**

Beim Initial Load (FR-1.3) prüft das System LocalStorage:
- **Gespeicherte Positionen gefunden:** Zettel werden direkt an gespeicherte Positionen platziert, Force-Simulation läuft NICHT
- **Keine Positionen:** Force-Simulation positioniert alle Zettel automatisch

**Performance:** Debouncing ist kritisch - nicht nach jedem Pixel speichern, sondern erst nach Drag-Ende (sonst würde LocalStorage bei jedem Frame geschrieben = langsam!)

**Was gehört NICHT dazu?**

- **KEINE Cloud-Speicherung:** Nur Browser-lokal, nicht über Geräte hinweg sync-bar (siehe Nicht-Anforderung #2)
- **KEIN Versions-Konflikt-Handling:** Bei mehreren Browser-Tabs überschreibt letzter Drag einfach (keine Merge-Strategie)
- **KEIN Export/Import:** Keine Möglichkeit Positionen als Datei zu exportieren (v2.0 Feature)

**Crash-Sicherheit:**

LocalStorage ist **persistent by default** - selbst bei Browser-Crash bleiben Daten erhalten (im Gegensatz zu sessionStorage). Allerdings:
- **Cache-Löschen:** User kann Browser-Cache löschen → Positionen weg (akzeptable Einschränkung)
- **Inkognito-Modus:** Positionen werden NICHT gespeichert (LocalStorage ist flüchtig)

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

**Beschreibung:**

Während FR-4.1 die räumliche Anordnung der Zettel speichert, bewahrt FR-4.2 die **View-Einstellungen** - wie der Nutzer den Graphen betrachtet und welche Filter aktiv sind. Zusammen ergeben beide ein **vollständiges Workspace-Restore**.

**Warum ist das wichtig?**

Ohne View-State-Persistierung würde nach jedem Reload:
- **Zoom zurück auf 100%** → User muss wieder rein/raus zoomen
- **Canvas zurück zu (0, 0)** → User muss wieder zur interessanten Stelle panen
- **Filter deaktiviert** → User muss Tag-Filter wieder setzen

Das ist **subtil frustrierend** - wie wenn dein Text-Editor bei jedem Öffnen zurück zu Zeile 1 scrollt statt zur letzten Arbeitsposition.

**Use-Case:** User arbeitet an einem Projekt-Cluster (gezoomt auf 150%, gepanned zu Projekt-Bereich, gefiltert nach `#projekt`). Schließt Browser. Am nächsten Tag: Öffnet ZettelWeb und sieht **exakt den gleichen View** - kann sofort weiterarbeiten.

**Wie funktioniert es?**

Drei unabhängige State-Komponenten werden gespeichert:

**1. Zoom-Level:**
- Aktueller Zoom-Faktor (z.B. 1.5 für 150%)
- Wird bei jedem Zoom-Event aktualisiert (mit Debouncing)

**2. Pan-Position:**
- Canvas-Offset (x, y)
- Wird bei jedem Pan-Event aktualisiert (mit Debouncing)

**3. Aktiver Filter:**
- Liste der aktuell ausgewählten Tags (z.B. `["#projekt", "#wichtig"]`)
- Wird bei Filter-Änderung sofort gespeichert

**Storage-Format (JSON in LocalStorage, separater Key von FR-4.1):**
```json
{
  "version": "1.0",
  "zoom": 1.5,
  "pan": { "x": 100, "y": 200 },
  "filter": ["#projekt", "#wichtig"]
}
```

**Debouncing:** Zoom/Pan passieren kontinuierlich (jeder Mouse-Move beim Pan), daher ist Debouncing essentiell - z.B. 500ms nach letzter Änderung speichern.

**Was gehört NICHT dazu?**

- **KEINE History/Undo:** Kein "Gehe zurück zu vorherigem View-State"
- **KEINE Multiple Saved Views:** Nur EIN gespeicherter State, keine "View A, View B, View C"-Slots
- **KEIN Auto-Reset:** State bleibt gespeichert bis User explizit "Reset View" drückt

**Beziehung zu FR-4.1:**

FR-4.1 und FR-4.2 sind komplementär:
- FR-4.1: **WO** sind die Zettel? (Positionen)
- FR-4.2: **WIE** betrachte ich sie? (Zoom, Pan, Filter)

Zusammen: Vollständiges Workspace-Restore.

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

**Kontext & Begründung:**

Performance ist **DAS kritische Qualitätsmerkmal** für ZettelWeb - wenn der Graph ruckelt oder einfriert, ist die gesamte Anwendung unbrauchbar. Dies ist kein "Nice-to-Have", sondern eine **fundamentale Anforderung**.

**Warum ist das so kritisch?**

1. **Real-Time-Interaktion:** Nutzer manipulieren den Graphen kontinuierlich (Drag, Zoom, Pan). Bei <30fps fühlt sich die App "laggy" und träge an - extrem frustrierend.

2. **Großer Daten-Umfang:** 200 Zettel × 1.5 Links/Zettel = ~300 Objekte die in jedem Frame (30-60x pro Sekunde!) neu gerendert werden müssen. Ohne Optimierung: sofortiger Performance-Kollaps.

3. **Physik-Simulation:** Force-Directed Layout ist rechenintensiv - jeder Zettel übt Kräfte auf alle anderen aus (O(n²) naiv, O(n log n) optimiert). Läuft in jedem Frame während Simulation.

4. **User-Erwartung:** Moderne Web-Apps (Google Maps, Figma, etc.) haben 60fps gesetzt als Standard. Alles darunter fühlt sich "kaputt" an.

**Was passiert bei schlechter Performance?**

- **<20 fps:** Graph fühlt sich "ruckelig" an, Drag & Drop ungenau
- **<10 fps:** Praktisch unbenutzbar, extreme Frustration
- **Freezes >1s:** User denkt App ist abgestürzt

**Performance ist nicht negotiable** - ohne flüssiges Rendering kann ZettelWeb seine Kern-Funktion (interaktiver Graph) nicht erfüllen.

**Technische Herausforderungen:**

Die 200-Zettel-Anforderung ist **absichtlich ambitioniert** - es zwingt das Team zu echter Optimierung:
- Canvas statt SVG (viel schneller bei vielen Objekten)
- Barnes-Hut statt naiver O(n²) Force-Berechnung
- Viewport Culling (off-screen Objekte nicht rendern)
- RequestAnimationFrame (Browser-optimiert)

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

**Kontext & Begründung:**

Browser-Kompatibilität sichert dass ZettelWeb **für die breite Masse** nutzbar ist, nicht nur für Entwickler mit neuesten Chrome-Versionen. Dies ist essentiell für eine öffentliche Web-Anwendung.

**Warum wichtig?**

- **Diverse Nutzer-Basis:** Manche nutzen Firefox (Privacy), manche Safari (macOS), manche Edge (Corporate). Wenn ZettelWeb nur in einem Browser läuft, schließt das viele potenzielle Nutzer aus.

- **Langlebigkeit:** Browser-Updates brechen manchmal Features. Unterstützung für "letzte 2 Major-Versionen" gibt Buffer bei Breaking Changes.

- **Testing-Realität:** Das Team kann nicht alle Browser gleichzeitig entwickeln. Chrome ist Lead-Plattform, aber Firefox/Safari müssen funktionieren.

**Risiken bei Inkompatibilität:**

- User öffnet ZettelWeb in Safari → weißer Bildschirm → "App ist kaputt" → verlässt sie
- Subtile Rendering-Unterschiede (Canvas, CSS) führen zu Bugs in bestimmten Browsern
- Feature-Detection fehlt → App crasht wenn API nicht verfügbar

**Warum "moderne Browser only"?**

Alte Browser (IE11, Chrome <80) erfordern Polyfills, Transpiling, massive Mehrarbeit. ZettelWeb nutzt:
- ES6+ (Arrow Functions, async/await, Modules)
- Canvas 2D API (standard seit Jahren)
- Fetch API (ersetzt XMLHttpRequest)

Diese Features sind in modernen Browsern nativ - kein Babel/Webpack-Overhead nötig.

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

**Kontext & Begründung:**

Eine Graph-Visualisierung kann technisch perfekt sein, aber wenn Nutzer nicht verstehen **wie** man sie bedient, ist sie wertlos. Usability entscheidet ob ZettelWeb **tatsächlich genutzt** wird oder nach 5 Minuten frustriert geschlossen wird.

**Warum ist Intuitivität kritisch?**

- **Keine dedizierte Schulung:** ZettelWeb ist ein persönliches Tool, keine Enterprise-Software. Nutzer erwarten dass es "einfach funktioniert", ohne 30-seitiges Manual zu lesen.

- **Vertraute Patterns:** Zoom mit Mouse Wheel, Drag mit Maus - das sind universelle Interaktionen die jeder kennt (von Google Maps, Figma, etc.). Wenn ZettelWeb diese Standards bricht, verwirrt es Nutzer.

- **Discovery durch Exploration:** Nutzer sollten Features entdecken können durch "herumspielen", nicht durch Dokumentation-Lesen. Hover-States, visuelles Feedback, Tooltips helfen dabei.

**Negativbeispiel (schlechte Usability):**

Stell dir vor:
- Zoom funktioniert nur per Tastatur-Shortcut (Strg + +/-)
- Kein Cursor-Feedback beim Hover über Zettel
- Drag funktioniert nur mit Rechtsklick
- Keine sichtbaren Buttons, alles versteckt in Menüs

→ User würde ZettelWeb für "kaputt" halten und aufgeben.

**Ziel-Usability:**

Ein neuer User soll innerhalb **5 Minuten** ohne Hilfe:
- Den Graphen zoomen & panen
- Einen Zettel anklicken und lesen
- Einen Zettel verschieben
- Nach einem Tag filtern

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

**Kontext & Begründung:**

Persistierungs-Zuverlässigkeit ist die **Vertrauensgrundlage** zwischen User und ZettelWeb. Wenn Nutzer 30 Minuten investiert um den Graphen zu arrangieren, und diese Arbeit dann verloren geht, ist das **Vertrauensbruch** - User wird die App nie wieder nutzen.

**Warum ist das Must-Have?**

Data Loss ist einer der **schlimmsten UX-Fehler** überhaupt:
- **Frustration:** "Ich hab das doch gerade erst arrangiert!"
- **Zeitverschwendung:** Arbeit muss wiederholt werden
- **Vertrauensverlust:** "Diese App ist unzuverlässig"

Im Gegensatz zu Performance-Problemen (ärgerlich aber tolerierbar) ist Datenverlust **inakzeptabel** - ein einziges Mal reicht um User dauerhaft zu verlieren.

**Kritische Szenarien:**

1. **Browser-Crash während Drag:** System muss letzte gespeicherte Positionen behalten (nicht alle löschen)
2. **Storage voll:** Graceful Degradation statt Silent Failure
3. **Korrupte Daten:** JSON-Parsing sollte nicht die gesamte App crashen

**Warum LocalStorage (nicht Server)?**

LocalStorage ist **synchron und sofort persistent** - selbst bei Browser-Crash bleiben Daten erhalten. Ein Server würde:
- Netzwerk-Latenz einführen (>100ms Speicher-Delay)
- Fehleranfällig bei Offline-Nutzung
- Unnötig komplex (Backend nötig)

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

**Kontext & Begründung:**

Der **erste Eindruck zählt**. Wenn ZettelWeb 20 Sekunden zum Laden braucht, denkt der User "Diese App ist langsam/kaputt" und verlässt sie - bevor er überhaupt ein Feature gesehen hat.

**Warum ist Initial Load Time kritisch?**

- **Psychologie:** User erwarten moderne Web-Apps in <3 Sekunden. Alles darüber fühlt sich "träge" an.

- **Perceived Performance:** Selbst wenn tatsächliche Load-Zeit 5s ist, fühlt es sich besser an mit Loading-Spinner als mit weißem Bildschirm.

- **Konkurrenz:** Andere Graph-Tools (Obsidian Graph View, Roam Research) laden sehr schnell. ZettelWeb muss mithalten.

**Performance-Budget Breakdown (5s TTI):**

```
0-1s:   HTML/CSS/JS Download + Parse
1-2s:   API-Call zu Zettelstore (/z Endpoint)
2-3s:   Daten-Parsing + Graph-Struktur-Aufbau
3-5s:   Force-Simulation Initial Run + Canvas Render
```

**Warum "Should-Have" nicht "Must-Have"?**

Initial Load ist wichtig, aber nicht showstopper:
- Nutzer laden die App nur 1x pro Session
- Nachdem sie geladen ist, läuft sie flüssig (NFR-1 ist kritischer)
- 6-7 Sekunden wären langsam aber akzeptabel

Aber: <5s ist professioneller Standard und sollte erreicht werden.

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

**Kontext & Begründung:**

Code-Qualität ist ein **Investment in die Zukunft**. Guter Code heute spart Stunden (oder Tage) an Debugging/Refactoring morgen. In einem Team-Projekt ist Wartbarkeit besonders kritisch - jedes Team-Mitglied muss fremden Code verstehen können.

**Warum ist das wichtig (trotz "Nice-to-Have")?**

- **Team-Zusammenarbeit:** 7 Entwickler arbeiten am Code. Wenn jeder in eigenem Stil schreibt (keine Konventionen), wird die Codebase zum Chaos.

- **Bug-Fixes:** Wenn ein Bug gefunden wird (z.B. Woche vor Abgabe), muss man Code schnell verstehen und fixen können. Bei unleserlichem Code: Panik.

- **Erweiterbarkeit:** Phase 2 & 3 Features bauen auf Phase 1 Code auf. Wenn Phase 1 ein Spaghetti-Mess ist, wird Phase 2 unmöglich.

- **Prüfung:** Professor/Tutor wird Code reviewen. Guter Code = bessere Note.

**Warum "Nice-to-Have" statt "Must-Have"?**

Code-Qualität ist **nicht funktionskritisch**:
- Schlechter aber funktionierender Code > perfekter aber unfertiger Code
- In Zeitdruck: Features gehen vor Refactoring
- Aber: Gewisse Mindest-Qualität ist nötig (daher ESLint, Dokumentation)

**Real-World Szenario:**

Team-Mitglied A schreibt Force-Simulation-Code.
Team-Mitglied B muss 2 Wochen später einen Bug fixen.
- **Guter Code:** B liest JSDoc, versteht Funktion, fixed Bug in 30 min
- **Schlechter Code:** B verbringt 3 Stunden Code zu verstehen, introduced neuen Bug

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
