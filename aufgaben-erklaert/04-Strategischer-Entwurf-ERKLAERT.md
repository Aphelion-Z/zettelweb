# 📝 AUFGABE 4: Strategischer Entwurf - Erklärt

**Status:** ⚠️ Gute Basis, aber Lücken und Widersprüche

---

## 🎯 WAS WURDE VERLANGT?

Lest nochmal die Original-Aufgabe:

> **Arbeitsanweisung:**
> Entwerfen Sie die Architektur Ihrer Software BEVOR Sie mit der Implementierung beginnen.
> Dokumentieren Sie Ihre Entscheidungen mit ADRs (Architecture Decision Records).
>
> **Aufgabe erfüllt wenn:**
> - Architektur-Muster gewählt und begründet ✓
> - UML-Diagramme zur Visualisierung ✓
> - Systemaufbau dokumentiert (mit Zettelstore) ✓
> - ADRs für wichtige Entscheidungen ✓
> - Wiki-Dokumentation ✓

---

## 🤔 WARUM DIESE AUFGABE?

### Was ist Strategischer Entwurf / Architektur?

**Einfach gesagt:** Der BAUPLAN für eure Software!

**Analogie Hausbau:**
```
Architekt zeichnet Bauplan
    ↓
Zeigt: Zimmer, Stockwerke, Leitungen, Statik
    ↓
Bauarbeiter bauen nach Plan
    ↓
Haus steht stabil!
```

**Ohne Bauplan:**
```
Bauarbeiter fangen einfach an
    ↓
Jeder macht was er denkt
    ↓
Wände passen nicht zusammen
    ↓
Haus fällt zusammen! 💥
```

### Problem ohne Architektur

**Szenario: Team fängt direkt mit Programmieren an**
```
Person A: "Ich mache die UI in HTML"
Person B: "Ich speichere alles in der Datenbank"
Person C: "Ich lade Daten von Zettelstore"

... 3 Wochen später ...

Person A: "Wo bekomme ich die Daten her?"
Person B: "Wie kommuniziere ich mit der UI?"
Person C: "Wer ruft meine Funktion auf?"

→ CHAOS! Alles muss neu gemacht werden 😱
```

### Mit Architektur

**Vorher planen:**
```
Team-Meeting:
"Wir nutzen MVC-Pattern"
    ↓
Model = Daten laden/speichern (Person C)
View = UI anzeigen (Person A)
Controller = Vermittler (Person B)
    ↓
Alle wissen wo ihr Code hingehört
    ↓
Code passt zusammen! ✅
```

### Warum ADRs (Architecture Decision Records)?

**Problem:** Entscheidungen vergessen

```
Heute: "Wir nutzen SQLite"
3 Monate später: "Warum nutzen wir SQLite?"
6 Monate später: "War das eine gute Idee?"
```

**Mit ADR:**
```
ADR-02: Wahl von SQLite
- Datum: 15.10.2025
- Entscheidung: SQLite statt PostgreSQL
- Begründung: Einfach, portable, kein Server
- Konsequenzen: Nicht multi-user-fähig
```

**Nutzen:**
- Neue Team-Mitglieder verstehen Entscheidungen
- Bei Problemen: Kann man nachvollziehen WARUM
- Bei Änderungen: Man weiß welche Konsequenzen es hatte

---

## ✅ WAS IHR GEMACHT HABT

### Architektur-Entscheidung: MVC

**Ihr habt gewählt:** Model-View-Controller Pattern

**Begründung (aus eurem Wiki):**
- Klare Trennung der Verantwortlichkeiten
- Model ändern ohne View zu ändern
- Einfacher zu testen

**Alternativen erwähnt:**
- SAO (?)
- Pipes & Filters

### ADR-01: Systemintegration

**Frage:** Standalone App oder Zettelstore-Extension?

**Entscheidung:** Standalone Web-App

**Begründung:**
- Keine Änderungen an Zettelstore-Code nötig
- Unabhängig von Zettelstore-Release-Zyklus
- Frontend-Technologie frei wählbar
- Team hat Frontend-Skills (JavaScript, HTML, CSS) aber nicht Go

**Konsequenzen:**
- Separate Anwendung muss deployed werden
- Kommunikation via REST API
- Eigene Datenbank für Positionen

### ADR-02: Datenbankwahl

**Frage:** SQLite, MySQL oder PostgreSQL?

**Bewertungskriterien:**
- Einfachheit
- Portabilität
- Performance
- Multi-User
- Setup-Aufwand
- Team-Kenntnisse

**Entscheidung:** SQLite

**Begründung:**
- Datei-basiert (keine Server-Installation)
- Portable (eine Datei)
- Ausreichend für lokale Anwendung
- Einfaches Setup

**Konsequenzen:**
- Nicht geeignet für Multi-User
- Migration zu Server-DB nötig falls Kollaboration gewünscht

### Diagramme

**1. Klassendiagramm (MVC)**
- Model: `Zettel`, `Tag`, `ZettelCluster`
- View: Rendering-Klassen
- Controller: Event-Handler

**2. Systemaufbau (Komponentendiagramm)**
- Browser (View + Controller)
- NetzWeb Backend (Model)
- Zettelstore Service
- Database (SQLite)

**Was GUT ist:** ✅
- ADRs sehr gut strukturiert!
- Bewertungskriterien klar definiert
- Alternativen fair verglichen
- Konsequenzen benannt (auch negative!)
- MVC-Wahl nachvollziehbar begründet
- Diagramme vorhanden

---

## 🔍 DETAILLIERTE BEWERTUNG

### ✅ ADR-01 & ADR-02: SEHR GUT!

**Was perfekt ist:**
- Struktur: Situation → Alternativen → Bewertung → Entscheidung → Konsequenzen
- Begründungen nachvollziehbar
- Alternativen objektiv bewertet
- Konsequenzen ehrlich benannt (auch Nachteile!)

**Beispiel ADR-02:**
```
Pro SQLite:
+ Einfach
+ Portable

Contra SQLite:
- Kein Multi-User

→ Entscheidung: SQLite weil Kontext = lokale App
→ Konsequenz: Falls später Multi-User → Migration nötig
```

**Das ist exzellente Dokumentation!** 👍

### ⚠️ Problem 1: Zu wenige ADRs

**Ihr habt 2 ADRs. Was FEHLT:**

#### Fehlender ADR-03: Frontend-Technologie

**Entscheidung zu treffen:**
- Vanilla JavaScript vs. Framework (React, Vue, Svelte)?
- Canvas vs. SVG für Graphen?
- CSS Framework (Bootstrap, Tailwind)?

**Möglicher ADR:**
```markdown
# ADR-03: Wahl der Frontend-Technologie

## Situation
Wir müssen entscheiden mit welchen Frontend-Technologien
wir die Visualisierung umsetzen.

## Alternativen

### Alternative 1: Vanilla JavaScript + Canvas
Pro:
- Keine Framework-Dependencies
- Canvas performant für viele Objekte
- Team kennt JavaScript

Contra:
- Mehr Boilerplate-Code
- Canvas-API komplex

### Alternative 2: React + SVG
Pro:
- Deklarative UI
- Component-Struktur
- SVG-Elemente inspizierbar
- Großes Ökosystem

Contra:
- Lernaufwand
- Overhead für einfache App
- SVG langsamer bei vielen Elementen

### Alternative 3: D3.js + SVG
Pro:
- Spezialisiert auf Daten-Visualisierung
- Force-directed Layout eingebaut
- Große Community

Contra:
- Steilere Lernkurve
- Overkill für unseren Use Case

## Bewertung
| Kriterium | Vanilla+Canvas | React+SVG | D3.js |
|-----------|----------------|-----------|-------|
| Performance | ++ | - | o |
| Lernaufwand | + | - | -- |
| Wartbarkeit | o | ++ | + |
| Zeitaufwand | + | o | - |

## Entscheidung
Vanilla JavaScript + Canvas

## Begründung
- Team hat begrenztes Framework-Wissen
- Performance wichtig (200+ Zettel)
- Zeitrahmen begrenzt (ein Semester)
- Anforderungen überschaubar

## Konsequenzen
+ Schneller Start
+ Gute Performance
- Mehr Code für UI-Management
- Weniger Struktur (muss selbst geschaffen werden)
```

#### Fehlender ADR-04: Graph-Layout-Algorithmus

**Entscheidung zu treffen:**
- Force-directed Layout?
- Hierarchisches Layout?
- Grid-basiert?
- Manuell mit Drag & Drop?

#### Fehlender ADR-05: State Management

**Entscheidung zu treffen:**
- Wo wird der App-State gespeichert?
- Wer ist "Source of Truth"?
- Wie werden Updates propagiert?

### ⚠️ Problem 2: Widerspruch Backend vs. No Backend

**ADR-01 sagt:**
> "JavaScript im Browser"
> "Standalone Web-App"
> "Keine Server-Komponente nötig"

**Systemaufbau-Diagramm zeigt:**
```
Browser
  ↓
NetzWeb Backend
  ↓
Zettelstore
```

**WIDERSPRUCH! 🤔**

**Was stimmt jetzt?**

**Option A: Wirklich nur Frontend (Browser)**
```
Browser (HTML/JS/CSS)
  ↓ REST API
Zettelstore
  ↓
Zettel-Dateien

Browser (JavaScript)
  ↓ Local Storage / IndexedDB
Positions-Datenbank
```

**Option B: Mit Backend**
```
Browser (nur UI)
  ↓ HTTPS
Node.js Backend
  ↓ REST API          ↓ SQL
Zettelstore        SQLite DB
```

**Ihr müsst euch entscheiden!**

Basierend auf ADR-01 sollte es **Option A** sein (kein Backend).
Dann ist das Systemdiagramm falsch und muss korrigiert werden.

### ⚠️ Problem 3: Klassendiagramm zu abstrakt

**Was ihr habt:**
- Klassendiagramm als Screenshot
- Klassen: `Zettel`, `Tag`, `ZettelCluster`, etc.

**Was FEHLT:**
- Attribute der Klassen (welche Daten speichert `Zettel`?)
- Methoden der Klassen (welche Funktionen hat `Zettel`?)
- Beziehungstypen unklar (Vererbung? Assoziation? Komposition?)
- Kardinalitäten (1:n? n:m?)

**Beispiel wie es besser wäre:**

```
┌─────────────────────────┐
│      Zettel             │
├─────────────────────────┤
│ - id: String            │
│ - title: String         │
│ - content: String       │
│ - tags: Tag[]           │
│ - x: Number             │
│ - y: Number             │
├─────────────────────────┤
│ + loadFromAPI()         │
│ + savePosition()        │
│ + getConnectedZettel()  │
│ + hasTag(tag): Boolean  │
└─────────────────────────┘
        │ 1
        │ enthält
        │ 0..*
        ▼
┌─────────────────────────┐
│         Tag             │
├─────────────────────────┤
│ - name: String          │
│ - color: String         │
├─────────────────────────┤
│ + matchesFilter()       │
└─────────────────────────┘
```

### ⚠️ Problem 4: Fehlende Implementierungs-Details

**Frage:** Wie wird die Architektur in Code umgesetzt?

**Unklar:**
- Ordnerstruktur? (`src/model/`, `src/view/`, `src/controller/`?)
- Dateinamen? (`Zettel.js`, `ZettelView.js`, `ZettelController.js`?)
- Wo ist die `main.js`? Wer initialisiert was?
- Wie kommunizieren die Schichten? (Events? Callbacks? Observables?)

**Besser wäre:**

```markdown
## Implementierungsplan

### Ordnerstruktur
```
src/
├── model/
│   ├── Zettel.js
│   ├── Tag.js
│   ├── ZettelCluster.js
│   └── Database.js
├── view/
│   ├── CanvasRenderer.js
│   ├── ZettelView.js
│   └── UIComponents.js
├── controller/
│   ├── MainController.js
│   ├── DragController.js
│   └── FilterController.js
└── main.js
```

### Initialisierung (main.js)
```javascript
// 1. Model initialisieren
const model = new ZettelModel()
await model.loadFromZettelstore()

// 2. View erstellen
const view = new CanvasRenderer('canvas-id')

// 3. Controller verbindet Model + View
const controller = new MainController(model, view)
controller.init()
```

### Kommunikation
- Model → View: Event System
- View → Controller: Event Listener
- Controller → Model: Direkte Methodenaufrufe
```

### ❌ Problem 5: Keine Test-Strategie

**Völlig fehlend:**
- Wie testet man die Architektur?
- Unit Tests? Integration Tests?
- Wie testet man Model unabhängig von View?

**Sollte in Architektur-Doku stehen:**

```markdown
## Test-Strategie

### Unit Tests
- Model-Layer: Tests ohne UI
  - Zettel laden
  - Clustering-Algorithmus
  - Tag-Filterung
- View-Layer: Mock-Daten rendern

### Integration Tests
- Controller verbindet Model + View korrekt
- Drag & Drop aktualisiert Model und View

### E2E Tests
- User-Szenarien durchspielen
- Performance-Tests (200 Zettel)
```

---

## 📚 WAS IST EINE GUTE ARCHITEKTUR?

### Die 5 Qualitäten

**1. Separation of Concerns (Trennung der Verantwortlichkeiten)**
- Jede Komponente macht EINE Sache
- Keine Vermischung
- ✅ Gut: Model lädt Daten, View zeigt sie an
- ❌ Schlecht: View lädt UND zeigt Daten an

**2. Low Coupling (Geringe Kopplung)**
- Komponenten sind wenig voneinander abhängig
- Änderung in A bricht nicht B
- ✅ Gut: View kennt Model nicht direkt (via Controller)
- ❌ Schlecht: View greift direkt auf Model zu

**3. High Cohesion (Hohe Kohäsion)**
- Zusammengehöriges ist zusammen
- Nicht zusammengehöriges ist getrennt
- ✅ Gut: Alle Render-Funktionen in `CanvasRenderer`
- ❌ Schlecht: Render-Funktionen über 10 Dateien verteilt

**4. Testability (Testbarkeit)**
- Komponenten lassen sich isoliert testen
- ✅ Gut: Model-Funktionen ohne UI testbar
- ❌ Schlecht: Alles hängt am DOM

**5. Evolvability (Erweiterbarkeit)**
- Neue Features leicht hinzuzufügen
- Änderungen haben lokale Auswirkung
- ✅ Gut: Neue Visualisierung = neue View-Klasse
- ❌ Schlecht: Neue Feature erfordert Änderungen überall

### MVC: Warum ist das gut?

**Model-View-Controller = bewährtes Pattern**

**Restaurant-Analogie:**
```
Gast (User)
  ↓ Bestellung
Kellner (Controller)
  ↓ gibt Bestellung weiter
Küche (Model)
  ↓ bereitet Essen zu
  ↓ Essen fertig
Kellner (Controller)
  ↓ bringt Essen
Teller (View)
  ↓ präsentiert Essen
Gast (User)
```

**Vorteile:**
- **Austauschbar:** Neue View ohne Model zu ändern
- **Testbar:** Model ohne View testen
- **Verständlich:** Jeder weiß wo Code hingehört
- **Parallel entwickelbar:** Person A macht Model, Person B macht View

**Für ZettelWeb konkret:**

```javascript
// MODEL: Daten und Logik
class ZettelModel {
  loadZettel() { /* API-Call zu Zettelstore */ }
  savePosition(id, x, y) { /* DB-Update */ }
  filterByTag(tag) { /* Logik */ }
}

// VIEW: Darstellung
class ZettelView {
  renderZettel(zettel) { /* Canvas zeichnen */ }
  highlightZettel(id) { /* Farbe ändern */ }
  showConnections(connections) { /* Linien zeichnen */ }
}

// CONTROLLER: Vermittler
class ZettelController {
  constructor(model, view) {
    this.model = model
    this.view = view
    this.setupEventListeners()
  }

  onDragEnd(id, x, y) {
    this.model.savePosition(id, x, y)
    this.view.renderZettel(this.model.getZettel())
  }
}
```

### Wie wählt man eine Architektur?

**Schritt 1: Anforderungen verstehen**
- Was muss die Software können?
- Welche Qualitäten sind wichtig? (Performance? Wartbarkeit?)

**Schritt 2: Optionen sammeln**
- Welche Patterns gibt es?
- MVC, MVP, MVVM, Flux, Redux, ...
- SAO (Pipes & Filters?), Layered Architecture, ...

**Schritt 3: Kriterien definieren**
- Was ist uns wichtig?
- Performance, Testbarkeit, Lernkurve, ...

**Schritt 4: Bewerten**
- Jede Option gegen Kriterien bewerten
- Tabelle erstellen (wie in euren ADRs!)

**Schritt 5: Entscheiden**
- Beste Option wählen
- ADR schreiben (dokumentieren!)

---

## 🎓 WIE HÄTTE ICH DAS MACHEN SOLLEN?

### Schritt 1: Architektur-Workshop

**Team-Meeting (2-3 Stunden):**

**Teil 1: Anforderungen Review**
- User Stories durchgehen
- Wichtigste Features identifizieren
- Performance-Anforderungen beachten

**Teil 2: Patterns Brainstorming**
- Welche Patterns kennen wir?
- Welche könnten passen?
- Mindestens 3 Optionen sammeln

**Teil 3: Kriterien definieren**
```
Was ist uns wichtig?
1. Lernkurve (wir sind Studenten!)
2. Testbarkeit
3. Performance (200 Zettel)
4. Wartbarkeit (ein Semester)
5. Erweiterbarkeit
```

**Teil 4: Bewertungsmatrix**
```
| Pattern | Lernkurve | Testbarkeit | Performance | Wartbarkeit |
|---------|-----------|-------------|-------------|-------------|
| MVC     | +++       | ++          | ++          | ++          |
| Flux    | -         | +++         | ++          | +++         |
| Vanilla | +++       | -           | +++         | -           |
```

**Teil 5: Entscheidung**
- Diskussion
- Abstimmung
- ADR schreiben!

### Schritt 2: System-Architektur

**Komponenten identifizieren:**
```
Was brauchen wir?

Externe Systeme:
- Zettelstore (gegeben)

Unsere Komponenten:
- Frontend (Browser)
- Datenbank (für Positionen)
- Evtl. Backend? (entscheiden!)
```

**Entscheidung: Backend ja/nein?**
- ADR schreiben (wie ADR-01!)
- Konsequenzen durchdenken

**Diagramm zeichnen:**
- Komponenten als Boxen
- Pfeile = Kommunikation
- Labels = Protokolle (REST, SQL, etc.)

### Schritt 3: Detaillierte Architektur

**Für MVC:**

**Model-Klassen identifizieren:**
```
Was sind unsere Daten-Objekte?
- Zettel (von Zettelstore)
- Position (x, y Koordinaten)
- Tag (Gruppierung)
- Connection (Verbindungen zwischen Zetteln)
```

**View-Komponenten identifizieren:**
```
Was wird angezeigt?
- Canvas (Hauptansicht)
- Zettel-Boxen
- Verbindungslinien
- Filter-UI
- Zoom-Controls
```

**Controller-Funktionen identifizieren:**
```
Welche User-Interaktionen gibt es?
- Drag & Drop
- Zoom & Pan
- Klick auf Zettel
- Filter anwenden
```

**Klassendiagramm zeichnen:**
- Tool nutzen (draw.io, PlantUML, Lucidchart)
- Klassen mit Attributen UND Methoden
- Beziehungen einzeichnen
- Beschriftungen hinzufügen

### Schritt 4: ADRs schreiben

**Für jede wichtige Entscheidung ein ADR:**

1. **ADR-01: System Integration** ✅ (habt ihr!)
2. **ADR-02: Datenbank** ✅ (habt ihr!)
3. **ADR-03: Frontend-Tech** ❌ (fehlt)
4. **ADR-04: Graph-Layout** ❌ (fehlt)
5. **ADR-05: State Management** ❌ (fehlt)

**Template nutzen:**
```markdown
# ADR-XX: Titel der Entscheidung

## Situation
Welches Problem muss gelöst werden?

## Alternativen
### Option 1
Pro: ...
Contra: ...

### Option 2
Pro: ...
Contra: ...

## Bewertungskriterien
- Kriterium 1
- Kriterium 2

## Bewertung
Tabelle mit Alternativen vs. Kriterien

## Entscheidung
Was haben wir gewählt?

## Begründung
Warum diese Option?

## Konsequenzen
Was bedeutet das?
+ Vorteile
- Nachteile
```

### Schritt 5: Implementierungs-Planung

**Ordnerstruktur definieren:**
```
Wo kommt welcher Code hin?
```

**Dateinamen festlegen:**
```
Wie heißen die Dateien?
```

**Entry Point definieren:**
```
Wo fängt die App an? (main.js)
```

**Dependencies dokumentieren:**
```
Welche Libraries brauchen wir?
```

### Schritt 6: Test-Strategie

**Überlegen:**
- Was muss getestet werden?
- Wie testen wir es?
- Welche Tools nutzen wir?

**Dokumentieren:**
```markdown
## Test-Strategie

### Unit Tests (Jest)
- Model-Layer: 80% Coverage
- Kritische Funktionen: 100%

### Integration Tests
- API-Calls mocken
- DB-Zugriffe mocken

### E2E Tests (Playwright)
- 3 zentrale User-Flows
```

### Schritt 7: Review

**Team-Review:**
- Alle lesen die Architektur-Doku
- Fragen stellen
- Unklarheiten beseitigen

**Checkliste:**
- [ ] Alle Komponenten identifiziert?
- [ ] Alle Schnittstellen definiert?
- [ ] ADRs für alle wichtigen Entscheidungen?
- [ ] Diagramme verständlich?
- [ ] Implementierung machbar?
- [ ] Widersprüche aufgelöst?

---

## 💡 VERBESSERUNGSVORSCHLÄGE FÜR EURE ARCHITEKTUR

### Sofort machen:

**1. Widerspruch Backend auflösen**

**Option A: Diagramm korrigieren (empfohlen)**
```
VORHER:
Browser → NetzWeb Backend → Zettelstore

NACHHER:
Browser (HTML/JS/CSS)
  ↓ REST API (HTTPS/JSON)
Zettelstore
  ↓ Dateisystem
Zettel-Dateien

Browser (JavaScript)
  ↓ localStorage/IndexedDB
Position Data
```

**Option B: ADR-01 überarbeiten**
- Falls ihr doch ein Backend wollt
- Begründung hinzufügen WARUM
- Konsequenzen neu bewerten

**2. Fehlende ADRs schreiben**

Mindestens **ADR-03: Frontend-Technologie**
- Vanilla JS vs. Framework
- Canvas vs. SVG
- Begründung

**3. Klassendiagramm präzisieren**

```markdown
Für jede Klasse dokumentieren:
- Attribute (mit Typ!)
- Methoden (mit Parametern!)
- Beziehungen (mit Kardinalität!)
```

### Nice-to-Have:

**4. Implementierungs-Plan hinzufügen**
```markdown
## Umsetzung der Architektur

### Ordnerstruktur
[siehe oben]

### Initialisierung
[Code-Beispiel]

### Kommunikation zwischen Schichten
[Diagramm + Beschreibung]
```

**5. Sequenzdiagramme**

Für wichtige Abläufe:
```
Beispiel: "Nutzer verschiebt Zettel"

User → View: MouseDown auf Zettel
View → Controller: dragStart(zettelId)
Controller → Model: getZettel(id)
Model → Controller: zettel
User → View: MouseMove
View → Controller: dragMove(x, y)
Controller → View: updatePosition(id, x, y)
User → View: MouseUp
View → Controller: dragEnd(id, x, y)
Controller → Model: savePosition(id, x, y)
Model → DB: INSERT position
```

**6. Test-Strategie dokumentieren**

**7. Performance-Strategie**
```markdown
## Performance-Optimierungen

### Für 200+ Zettel:
- Canvas statt DOM-Elemente
- Render-Loop mit RequestAnimationFrame
- Spatial Hashing für Collision Detection
- Debouncing bei Drag-Events
```

---

## 🧪 ÜBUNG: ADR schreiben

### Übung 1: ADR-03 erstellen

**Aufgabe:** Schreibt einen ADR für "Frontend-Technologie"

**Vorgabe:**
- Situation: Framework oder Vanilla JS?
- Alternativen: Vanilla, React, Vue
- Kriterien: Lernkurve, Performance, Zeitaufwand
- Entscheidung treffen!

<details>
<summary>💡 Musterlösung</summary>

```markdown
# ADR-03: Wahl der Frontend-Technologie

## Situation
Für die Visualisierung der Zettel müssen wir entscheiden
ob wir ein Framework nutzen oder mit Vanilla JavaScript arbeiten.

## Alternativen

### Alternative 1: Vanilla JavaScript
**Pro:**
- Keine Dependencies
- Volle Kontrolle
- Performance
- Team kennt JavaScript

**Contra:**
- Mehr Boilerplate
- State Management selbst bauen
- Weniger Struktur

### Alternative 2: React
**Pro:**
- Komponentenstruktur
- Große Community
- Viele Libraries

**Contra:**
- Lernkurve
- Overhead
- Bundle-Size

### Alternative 3: Vue
**Pro:**
- Einfacher als React
- Gute Performance
- Progressive Framework

**Contra:**
- Team-Kenntnisse fehlen
- Kleinere Community als React

## Bewertungskriterien
1. Lernkurve (wichtig: begrenzter Zeitrahmen)
2. Performance (200+ Zettel)
3. Entwicklungsgeschwindigkeit
4. Team-Kenntnisse
5. Bundle-Size

## Bewertung
| Kriterium | Vanilla | React | Vue |
|-----------|---------|-------|-----|
| Lernkurve | ++      | -     | o   |
| Performance | +++   | +     | ++  |
| Dev-Speed | +       | ++    | ++  |
| Team-Know | +++     | +     | -   |
| Bundle-Size | +++   | -     | o   |
| **SUMME** | **13**  | **4** | **5** |

## Entscheidung
**Vanilla JavaScript** mit Canvas

## Begründung
- Team hat solide JavaScript-Kenntnisse aber wenig Framework-Erfahrung
- Lernaufwand für Framework zu hoch bei begrenzter Zeit
- Performance kritisch (200+ Zettel)
- Anforderungen überschaubar (keine komplexe State-Logik)
- Canvas-Performance besser als DOM-Manipulation

## Konsequenzen

**Vorteile:**
+ Schneller Start (keine Lernphase)
+ Optimale Performance
+ Keine Build-Pipeline nötig
+ Kleine Bundle-Size

**Nachteile:**
- Mehr Code für State Management
- Weniger Struktur-Vorgaben (muss selbst geschaffen werden)
- UI-Updates manuell implementieren
- Schwieriger zu warten

**Mitigation:**
- Klare Code-Conventions definieren
- MVC-Pattern strikt einhalten
- Code-Reviews etablieren
```
</details>

### Übung 2: Sequenzdiagramm

**Aufgabe:** Zeichnet ein Sequenzdiagramm für "Zettel laden beim Start"

**Beteiligte:**
- User
- View
- Controller
- Model
- Zettelstore API

<details>
<summary>💡 Musterlösung (Text-Format)</summary>

```
User startet App
  ↓
View: init()
  ↓
Controller: init()
  ↓
Controller → Model: loadAllZettel()
  ↓
Model → ZettelstoreAPI: GET /z
  ↓
ZettelstoreAPI → Model: JSON (alle Zettel)
  ↓
Model → Database: SELECT positions
  ↓
Database → Model: position data
  ↓
Model: mergeZettelWithPositions()
  ↓
Model → Controller: zettelData
  ↓
Controller → View: render(zettelData)
  ↓
View: drawZettelOnCanvas()
  ↓
User sieht Zettel
```
</details>

### Übung 3: Ordnerstruktur

**Aufgabe:** Entwerft eine vollständige Ordnerstruktur für euer Projekt

**Vorgaben:**
- MVC-Pattern
- Tests
- Assets (CSS, Bilder)
- Config

<details>
<summary>💡 Musterlösung</summary>

```
zettelweb/
├── src/
│   ├── model/
│   │   ├── Zettel.js
│   │   ├── Tag.js
│   │   ├── ZettelCluster.js
│   │   ├── Database.js
│   │   └── ZettelstoreAPI.js
│   ├── view/
│   │   ├── CanvasRenderer.js
│   │   ├── ZettelRenderer.js
│   │   ├── ConnectionRenderer.js
│   │   ├── UIComponents.js
│   │   └── FilterUI.js
│   ├── controller/
│   │   ├── MainController.js
│   │   ├── DragController.js
│   │   ├── ZoomController.js
│   │   └── FilterController.js
│   ├── utils/
│   │   ├── EventEmitter.js
│   │   ├── Logger.js
│   │   └── Math.js
│   └── main.js
├── tests/
│   ├── model/
│   │   ├── Zettel.test.js
│   │   └── ZettelCluster.test.js
│   ├── controller/
│   └── integration/
├── assets/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   └── fonts/
├── config/
│   ├── app.config.js
│   └── api.config.js
├── docs/
│   └── architecture/
│       ├── ADR-01-System.md
│       ├── ADR-02-Database.md
│       └── class-diagram.png
├── index.html
├── package.json
├── .gitignore
└── README.md
```
</details>

---

## ✅ CHECKLISTE

Habt ihr verstanden:
- [ ] Was Softwarearchitektur ist? (Zweck?)
- [ ] Warum man Architektur VOR dem Programmieren entwirft?
- [ ] Was MVC ist? (Model, View, Controller)
- [ ] Warum MVC gut ist? (Vorteile?)
- [ ] Was ADRs sind? (Architecture Decision Records)
- [ ] Wie man einen ADR schreibt? (Struktur?)
- [ ] Was in euren ADRs gut ist?
- [ ] Welche ADRs fehlen?
- [ ] Wo der Widerspruch in eurem System ist?
- [ ] Wie man von Architektur zu Code kommt?

**Alle ✅?** Dann seid ihr bereit!

---

## ➡️ NÄCHSTER SCHRITT

**Ihr habt jetzt:**
- ✅ Aufgabe 1 verstanden (Infrastruktur)
- ✅ Aufgabe 2 verstanden (Projektauftrag)
- ✅ Aufgabe 3 verstanden (Anforderungen)
- ✅ Aufgabe 4 verstanden (Architektur)

**Next Level:**
→ Vertiefungs-Guides lesen (`/guides` Ordner - wenn erstellt)
→ Übungen machen (`/uebungen` Ordner - wenn erstellt)
→ Tutorials durcharbeiten (`/tutorials` Ordner)

**Oder direkt:** Eure Dokumente verbessern!
- Issues überarbeiten
- Fehlende ADRs schreiben
- Widersprüche auflösen
