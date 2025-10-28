# 📝 AUFGABE 3: Anforderungsanalyse - Erklärt

**Status:** ⚠️ Strukturell ok, aber inhaltlich verbesserbar

---

## 🎯 WAS WURDE VERLANGT?

Lest nochmal die Original-Aufgabe:

> **Arbeitsanweisung:**
> Analysieren Sie die Anforderungen an Ihr Projekt und dokumentieren Sie diese.
> Nutzen Sie dafür GitHub Issues für funktionale Anforderungen (User Stories).
>
> **Aufgabe erfüllt wenn:**
> - Funktionale Anforderungen als Issues (User Story Format) ✓
> - Nicht-funktionale Anforderungen dokumentiert ✓
> - Nicht-Anforderungen explizit festgehalten ✓
> - SMART-Kriterien beachtet ⚠️

---

## 🤔 WARUM DIESE AUFGABE?

### Was ist Anforderungsanalyse?

**Einfach gesagt:** BEVOR man programmiert, muss man wissen WAS man bauen soll!

**Problem ohne Anforderungsanalyse:**
```
Team fängt an zu programmieren
    ↓
Person A baut Feature X
Person B baut Feature Y (widerspricht X)
    ↓
Kunde sagt: "Das wollte ich nicht!"
    ↓
Alles neu machen 💸💸💸
```

**Mit Anforderungsanalyse:**
```
Team schreibt auf WAS gebaut werden soll
    ↓
Alle sind sich einig
    ↓
Programmierung startet
    ↓
Am Ende passt es! ✅
```

### Analogie: Hausbau

**Ohne Anforderungen:**
- Bauarbeiter fängt einfach an zu bauen
- Jeder macht was er denkt
- Am Ende: Haus hat 3 Türen aber keine Fenster

**Mit Anforderungen:**
- Architekt fragt: "Wie viele Zimmer? Wo soll die Küche hin?"
- Alles wird aufgeschrieben
- Bauarbeiter wissen genau was zu tun ist
- Am Ende: Haus wie gewünscht!

### Warum User Stories?

**User Story = Anforderung aus NUTZER-Sicht**

**Format:**
```
Als [ROLLE]
will ich [FUNKTIONALITÄT]
damit/weil [NUTZEN]
```

**Warum dieses Format?**
1. **Fokus auf Nutzer** (nicht Technik!)
2. **Verständlich** für alle (auch nicht-Techniker)
3. **Testbar** (man kann demonstrieren ob es funktioniert)
4. **Priorisierbar** (welche Features sind wichtiger?)

---

## ✅ WAS IHR GEMACHT HABT

**13 Issues erstellt** auf GitHub

### Funktionale Anforderungen (User Stories): 8 Issues

**Issue #1:** Als Nutzer will ich durch das hinzufügen von "Tags" Zettel unterschiedlich gruppieren können
**Issue #2:** Als Nutzer will ich durch das hinzufügen von "Tags" Zettel unterschiedlich gruppieren können *(DUPLIKAT!)*
**Issue #3:** Als Nutzer will ich, dass zwischen zusammenhängenden Zetteln Linienverbindungen angezeigt werden
**Issue #4:** Als Nutzer will ich, dass beim Überfahren eines Zettels dieser und seine direkt verbundenen Zettel hervorgehoben werden
**Issue #5:** Als System will ich die aktuellen Koordinaten jedes verschobenen Zettels in einer Datenbank speichern *(Falsche Rolle!)*
**Issue #6:** Als Nutzer will ich, dass beim verschieben eines Zettels alle direkt verbundenen Zettel mit einer schnurartigen Animation elastisch nachgezogen werden
**Issue #7:** Als Nutzer will ich Zettel-Cluster erstellen und erweitern können
**Issue #8:** Als Nutzer will ich die Ansicht zoomen und verschieben können

### Nicht-funktionale Anforderungen (System Requirements): 5 Issues

**Issue #11:** Das System soll mind. 200 Zettel flüssig darstellen (30+ fps, <200ms Reaktionszeit)
**Issue #12:** Das System soll Positionsänderungen innerhalb von 3 Sekunden speichern
**Issue #13:** Das System soll bei Skalierung von 200 auf 300 Zettel <20% Performance-Einbuße haben

*(Issues #9-10 nicht in der Zusammenfassung erwähnt, vermutlich weitere Features)*

### Nicht-Anforderungen (Wiki-Seite)

**Dokumentiert:**
- Schriftarten/Schriftgröße sollen NICHT anpassbar sein

**Was GUT ist:** ✅
- Issues existieren
- Format meist korrekt ("Als Nutzer will ich...")
- Mix aus funktionalen und nicht-funktionalen Anforderungen
- Nicht-funktionale haben messbare Kriterien (SMART!)
- Nicht-Anforderungen-Seite existiert

**Was PROBLEMATISCH ist:** ❌

---

## 🔍 DETAILLIERTE BEWERTUNG: Issue für Issue

### ❌ Issue #1 & #2: DUPLIKAT

**Problem:**
Beide Issues haben EXAKT denselben Titel!

**Titel:** "Als Nutzer will ich durch das hinzufügen von 'Tags' Zettel unterschiedlich gruppieren können"

**Was tun:**
- Ein Issue löschen (oder schließen)
- Das andere Issue behalten und präzisieren

**Besser:**
```markdown
Titel: Als Nutzer will ich Zettel mit Tags gruppieren können

Beschreibung:
Als Nutzer will ich Zettel mit Tags versehen können,
damit ich sie thematisch gruppieren kann.

Akzeptanzkriterien:
- [ ] Ich kann einem Zettel einen Tag zuweisen
- [ ] Ich kann einem Zettel mehrere Tags zuweisen
- [ ] Zettel mit gleichem Tag werden visuell gruppiert (z.B. gleiche Farbe)
- [ ] Ich kann Tags filtern (nur Zettel mit Tag X anzeigen)

Priorität: Must-Have
Story Points: 5
```

---

### ❌ Issue #5: Falsche Rolle "Als System"

**Originaltitel:** "Als System will ich die aktuellen Koordinaten jedes verschobenen Zettels in einer Datenbank speichern"

**Problem:**
"System" ist KEINE Nutzer-Rolle! User Stories sollen aus NUTZER-Perspektive geschrieben sein.

**Warum falsch?**
- User Stories beschreiben den NUTZEN für den Nutzer
- Technische Details (Datenbank) interessieren Nutzer nicht
- Das "System" hat keine Wünsche - nur Nutzer haben Wünsche!

**Wie es richtig wäre:**

**Option 1: Als funktionale User Story**
```markdown
Titel: Als Nutzer will ich meine Zettel-Anordnung speichern können

Beschreibung:
Als Nutzer will ich, dass meine Zettel-Anordnung automatisch
gespeichert wird, damit ich beim nächsten Öffnen die gleiche
Anordnung wiederfinde.

Akzeptanzkriterien:
- [ ] Wenn ich einen Zettel verschiebe, wird die Position gespeichert
- [ ] Beim erneuten Laden erscheint der Zettel an der gleichen Position
- [ ] Speicherung erfolgt automatisch (kein "Speichern"-Button nötig)
- [ ] Speicherung ist persistent (auch nach Neustart)
```

**Option 2: Als nicht-funktionale Anforderung**
```markdown
Titel: Persistente Speicherung von Zettel-Positionen

Beschreibung:
Das System soll Zettel-Positionen persistent in einer
Datenbank speichern.

Kriterien:
- SQLite-Datenbank
- Speicherung nach jedem Drag-Event
- Maximale Speicherzeit: 3 Sekunden
```

**Regel:** Wenn es um TECHNIK geht → nicht-funktionale Anforderung!

---

### ⚠️ Issue #6: Zu vage/technisch

**Titel:** "Als Nutzer will ich, dass beim verschieben eines Zettels alle direkt verbundenen Zettel mit einer schnurartigen Animation elastisch nachgezogen werden"

**Probleme:**
1. **"Schnurartige Animation"** - Was bedeutet das konkret?
2. **"Elastisch nachgezogen"** - Wie elastisch? Wann?
3. Zu technisch formuliert (Animation-Detail)
4. Schwer testbar (subjektiv)

**Besser:**
```markdown
Titel: Als Nutzer will ich sehen wie verbundene Zettel auf Bewegung reagieren

Beschreibung:
Als Nutzer will ich, dass wenn ich einen Zettel verschiebe,
die damit verbundenen Zettel visuell nachfolgen, damit ich
die Verbindungen besser erkenne.

Akzeptanzkriterien:
- [ ] Verbundene Zettel bewegen sich mit (verzögert)
- [ ] Verbindungslinien bleiben sichtbar während der Bewegung
- [ ] Animation ist flüssig (mind. 30fps)
- [ ] Animation endet nach max. 2 Sekunden

Akzeptanztest:
Gegeben: Zettel A ist mit Zettel B verbunden
Wenn: Ich Zettel A verschiebe
Dann: Zettel B folgt mit sichtbarer Animation

Design-Hinweis:
Team entscheidet über konkreten Animations-Stil (elastisch, linear, etc.)
```

**Lernen:** User Stories beschreiben WAS, nicht WIE!

---

### ⚠️ Issue #7: Zu vage

**Titel:** "Als Nutzer will ich Zettel-Cluster erstellen und erweitern können"

**Probleme:**
1. Was ist ein "Cluster" konkret? (Gruppe? Kategorie?)
2. Wie "erstelle" ich einen Cluster?
3. Was bedeutet "erweitern"?

**Besser: In mehrere User Stories aufteilen**

**Story 1: Cluster erstellen**
```markdown
Als Nutzer will ich mehrere Zettel zu einer Gruppe zusammenfassen
können, damit ich zusammengehörige Themen organisieren kann.

Akzeptanzkriterien:
- [ ] Ich kann mehrere Zettel auswählen (Strg+Klick)
- [ ] Ich kann "Gruppe erstellen" Button klicken
- [ ] Gruppe bekommt einen Namen
- [ ] Gruppierte Zettel haben visuellen Rahmen
```

**Story 2: Cluster erweitern**
```markdown
Als Nutzer will ich weitere Zettel zu einer bestehenden Gruppe
hinzufügen können, damit ich die Gruppierung anpassen kann.

Akzeptanzkriterien:
- [ ] Ich kann einen Zettel auf eine Gruppe ziehen
- [ ] Zettel wird Teil der Gruppe
- [ ] Zettel erhält die Gruppen-Formatierung
```

**Regel:** Eine User Story = eine Funktionalität!

---

### ✅ Issue #3: GUT!

**Titel:** "Als Nutzer will ich, dass zwischen zusammenhängenden Zetteln Linienverbindungen angezeigt werden"

**Was gut ist:**
- Klare Rolle (Nutzer)
- Klare Funktionalität (Linien anzeigen)
- Testbar (sieht man die Linien?)

**Noch besser mit Akzeptanzkriterien:**
```markdown
Als Nutzer will ich, dass zwischen zusammenhängenden Zetteln
Linienverbindungen angezeigt werden, damit ich Zusammenhänge
sofort erkenne.

Akzeptanzkriterien:
- [ ] Linien verbinden Zettel die miteinander verlinkt sind
- [ ] Linien sind klar sichtbar (Farbe, Dicke einstellbar)
- [ ] Linien überlappen Zettel nicht (gehen bis zum Rand)
- [ ] Hover über Linie hebt beide verbundenen Zettel hervor

Priorität: Must-Have
Story Points: 3
```

---

### ✅ Issue #11: Nicht-funktionale Anforderung GUT!

**Titel:** "Das System soll mind. 200 Zettel flüssig darstellen (30+ fps, <200ms Reaktionszeit)"

**Was GUT ist:**
- **Messbar** (30fps, 200ms)
- **Spezifisch** (200 Zettel)
- **Testbar** (kann man messen!)
- **Realistisch** (ist machbar)

**Das ist SMART!** ✅

---

### ⚠️ Nicht-Anforderungen: Zu dünn

**Was ihr habt:**
- "Schriftarten/Schriftgröße ändern" ist keine Anforderung

**Was fehlt:**
Mehr explizite Ausschlüsse!

**Beispiele für Nicht-Anforderungen:**
```markdown
## Nicht-Anforderungen

Diese Features sind NICHT Teil des Projekts:

### Kollaboration
- Kein Multi-User-Modus
- Keine gleichzeitigen Bearbeitungen
- Keine Echtzeit-Synchronisation zwischen Nutzern

### Cloud/Sync
- Keine Cloud-Speicherung
- Keine Synchronisation über mehrere Geräte
- Keine Online-Backup-Funktion

### Zettel-Bearbeitung
- Keine Zettel-Erstellung in der Visualisierung
  (nur in Zettelstore)
- Keine Zettel-Inhalt-Bearbeitung
  (nur Anzeige und Positionierung)

### Export/Import
- Kein Export als PDF/Bild
- Kein Import aus anderen Zettelkasten-Systemen

### Erweiterte Visualisierungen
- Keine 3D-Visualisierung
- Keine Zeitleisten-Ansicht
- Keine Mind-Map-Ansicht
```

**Warum wichtig:**
- Klärt Erwartungen
- Verhindert Feature Creep
- Hilft bei Scope-Management

---

## 📚 WIE SCHREIBT MAN GUTE USER STORIES?

### Die INVEST-Kriterien

Eine gute User Story ist **INVEST**:

**I - Independent (Unabhängig)**
- Story kann alleine umgesetzt werden
- Nicht abhängig von anderen Stories
- ❌ Schlecht: "Story 1: Backend API" + "Story 2: Frontend nutzt API"
- ✅ Gut: "Als Nutzer will ich Zettel laden können" (umfasst alles)

**N - Negotiable (Verhandelbar)**
- Details sind noch offen
- Team kann entscheiden WIE es umgesetzt wird
- ❌ Schlecht: "Als Nutzer will ich einen roten Button mit Arial-Schrift"
- ✅ Gut: "Als Nutzer will ich Zettel löschen können"

**V - Valuable (Wertvoll)**
- Bringt Nutzen für Stakeholder
- ❌ Schlecht: "Als Entwickler will ich Code refactoren"
- ✅ Gut: "Als Nutzer will ich schnelle Antwortzeiten haben"

**E - Estimable (Schätzbar)**
- Team kann Aufwand einschätzen
- Nicht zu vage
- ❌ Schlecht: "Als Nutzer will ich ein gutes System"
- ✅ Gut: "Als Nutzer will ich nach Tags filtern können"

**S - Small (Klein)**
- In wenigen Tagen umsetzbar
- Nicht zu groß
- ❌ Schlecht: "Als Nutzer will ich ein komplettes Zettelkasten-System"
- ✅ Gut: "Als Nutzer will ich einen Zettel verschieben können"

**T - Testable (Testbar)**
- Kann man prüfen ob es funktioniert?
- ❌ Schlecht: "Als Nutzer will ich ein schönes Interface"
- ✅ Gut: "Als Nutzer will ich max. 3 Klicks brauchen um einen Zettel zu öffnen"

### Template für User Stories

```markdown
Titel: Als [ROLLE] will ich [AKTION] können

## Beschreibung
Als [ROLLE]
will ich [FUNKTIONALITÄT]
damit/weil [NUTZEN/GRUND]

## Akzeptanzkriterien
- [ ] Kriterium 1 (testbar!)
- [ ] Kriterium 2
- [ ] Kriterium 3

## Akzeptanztest (Optional)
**Gegeben:** Ausgangssituation
**Wenn:** Aktion
**Dann:** Erwartetes Ergebnis

## Technische Hinweise (Optional)
- Notizen für Entwickler
- Keine Vorgaben, nur Vorschläge

## Priorität
Must-Have / Should-Have / Nice-to-Have

## Aufwand (Story Points)
1-13 Punkte (Fibonacci-Skala)
```

### Beispiele: Schlecht vs. Gut

#### Beispiel 1: Suche

**❌ Schlecht:**
```
Als System will ich eine Suchfunktion haben
```

**Probleme:**
- "System" ist keine Rolle
- Zu vage
- Kein Nutzen erklärt
- Nicht testbar

**✅ Gut:**
```markdown
Titel: Als Nutzer will ich nach Zettel-Inhalten suchen können

## Beschreibung
Als Nutzer will ich Zettel nach Schlagworten durchsuchen können,
damit ich schnell relevante Notizen finde.

## Akzeptanzkriterien
- [ ] Suchfeld in der Oberfläche sichtbar
- [ ] Suche findet Zettel mit Begriff im Titel
- [ ] Suche findet Zettel mit Begriff im Inhalt
- [ ] Suche findet Zettel mit Begriff in Tags
- [ ] Suchergebnisse werden hervorgehoben
- [ ] Suche reagiert innerhalb 500ms

## Priorität: Must-Have
## Story Points: 5
```

#### Beispiel 2: Performance

**❌ Schlecht:**
```
Das System soll schnell sein
```

**Probleme:**
- Nicht messbar (was ist "schnell"?)
- Nicht testbar
- Zu allgemein

**✅ Gut:**
```markdown
Titel: Flüssige Darstellung von 200+ Zetteln

## Beschreibung
Das System soll mindestens 200 Zettel gleichzeitig
flüssig darstellen können, damit Nutzer auch bei großen
Zettelkästen komfortabel arbeiten können.

## Kriterien
- Bildrate: mind. 30 fps bei 200 Zetteln
- Reaktionszeit auf Drag: max. 200ms
- Zoom/Pan: keine sichtbare Verzögerung
- Maximaler RAM-Verbrauch: 500 MB

## Testverfahren
Performance-Test mit Testdaten (200 Zettel,
500 Verbindungen)

## Priorität: Must-Have
```

---

## 🎓 WIE HÄTTE ICH DAS MACHEN SOLLEN?

### Schritt 1: Requirements Gathering (Anforderungen sammeln)

**Methoden:**
1. **Brainstorming im Team**
   - "Was soll die Software können?"
   - Alle Ideen sammeln (noch nicht bewerten!)

2. **Stakeholder fragen**
   - Prof. Stern: Was erwartet er?
   - Potenzielle Nutzer: Was würden sie brauchen?

3. **Bestehende Systeme analysieren**
   - Was kann Zettelstore selbst?
   - Was machen Obsidian, Roam Research, etc.?
   - Was fehlt dort?

4. **Use Cases durchspielen**
   - "Ich öffne die App... was will ich als erstes tun?"
   - "Ich habe 200 Zettel... wie navigiere ich?"

### Schritt 2: Anforderungen strukturieren

**Kategorien bilden:**
```
Kern-Features (Must-Have):
- Zettel laden und anzeigen
- Zettel positionieren (Drag & Drop)
- Verbindungen visualisieren
- Positionen speichern

Erweiterte Features (Should-Have):
- Tags/Gruppierung
- Suche/Filter
- Zoom/Pan

Nice-to-Have:
- Animationen
- Farb-Anpassungen
- Tastatur-Shortcuts
```

### Schritt 3: User Stories formulieren

**Für jedes Feature:**
1. Rolle identifizieren (Nutzer? Admin? System?)
2. Funktionalität beschreiben
3. Nutzen erklären (WARUM will ich das?)
4. Akzeptanzkriterien definieren (WANN ist es fertig?)

**Checklist pro User Story:**
- [ ] INVEST-Kriterien erfüllt?
- [ ] Akzeptanzkriterien vorhanden?
- [ ] Priorität festgelegt?
- [ ] Testbar?

### Schritt 4: Issues erstellen

**Pro User Story ein GitHub Issue:**
1. Titel = User Story Titel
2. Beschreibung = komplette User Story (mit Akzeptanzkriterien)
3. Labels vergeben:
   - `feature` / `enhancement` / `bug`
   - `must-have` / `should-have` / `nice-to-have`
   - `frontend` / `backend` / `database`
4. Milestone zuweisen (welcher Meilenstein?)
5. Story Points schätzen (im Team!)

### Schritt 5: Nicht-funktionale Anforderungen

**Kategorien:**
- Performance (Geschwindigkeit)
- Skalierbarkeit (wie viele Daten?)
- Usability (Bedienbarkeit)
- Wartbarkeit (Code-Qualität)
- Security (Sicherheit)

**Für jede Kategorie:**
- Messbare Kriterien definieren
- Testverfahren überlegen

### Schritt 6: Nicht-Anforderungen

**Fragen:**
- Was könnte man denken dass es dabei ist?
- Was ist explizit NICHT geplant?
- Wo ist der Scope?

**In Wiki-Seite dokumentieren**

### Schritt 7: Review im Team

**Checkliste:**
- [ ] Alle Features erfasst?
- [ ] Prioritäten klar?
- [ ] Machbar im Zeitrahmen?
- [ ] Verständlich für alle?
- [ ] Lücken oder Widersprüche?

---

## 💡 VERBESSERUNGSVORSCHLÄGE FÜR EURE ISSUES

### Sofort machen:

**1. Issue #2 schließen (Duplikat)**
```
Kommentar: "Duplikat von #1" → Issue schließen
```

**2. Issue #5 umformulieren**
```markdown
VORHER:
Als System will ich die aktuellen Koordinaten [...] speichern

NACHHER:
Als Nutzer will ich, dass meine Zettel-Anordnung automatisch
gespeichert wird, damit ich sie beim nächsten Öffnen wiederfinde.
```

**3. Akzeptanzkriterien zu allen Issues hinzufügen**
```markdown
Jedes Issue sollte haben:

## Akzeptanzkriterien
- [ ] Kriterium 1
- [ ] Kriterium 2
- [ ] ...

## Priorität
Must-Have / Should-Have / Nice-to-Have

## Aufwand
Story Points (1, 2, 3, 5, 8, 13)
```

### Nice-to-Have:

**4. Mehr Nicht-Anforderungen dokumentieren**
- Siehe Liste oben (Kollaboration, Cloud, etc.)

**5. Issues priorisieren**
- Labels hinzufügen: `must-have`, `should-have`, `nice-to-have`
- Meilensteine zuweisen

**6. Story Points schätzen**
- Team-Meeting: Planning Poker
- Fibonacci-Skala: 1, 2, 3, 5, 8, 13

**7. Vage Issues präzisieren**
- Issue #7 (Cluster) → mehrere Issues
- Issue #6 (Animation) → konkreter formulieren

---

## 🧪 ÜBUNG: User Stories schreiben

### Übung 1: User Story für "Zoom-Funktion"

**Aufgabe:** Schreibt eine vollständige User Story für die Zoom-Funktion.

**Hilfestellung:**
- Rolle: Nutzer
- Funktionalität: Ansicht zoomen
- Nutzen: Warum will ich zoomen?
- Akzeptanzkriterien: 3-5 Kriterien

<details>
<summary>💡 Musterlösung</summary>

```markdown
Titel: Als Nutzer will ich die Ansicht zoomen können

## Beschreibung
Als Nutzer will ich in die Zettel-Ansicht hinein- und
herauszoomen können, damit ich bei vielen Zetteln die
Übersicht behalte und bei Bedarf Details erkenne.

## Akzeptanzkriterien
- [ ] Ich kann mit Mausrad zoomen (rein/raus)
- [ ] Ich kann mit Pinch-Geste zoomen (Touchpad)
- [ ] Zoom-Stufen: 50% bis 200%
- [ ] Zoom-Zentrum ist Mausposition
- [ ] Zoom ist flüssig (keine Ruckler)
- [ ] Aktuelle Zoom-Stufe wird angezeigt

## Priorität: Should-Have
## Story Points: 3
```
</details>

### Übung 2: User Story verbessern

**Gegeben: Schlechte User Story**
```
Als System will ich Daten in JSON speichern
```

**Aufgabe:** Verbessert diese User Story!

<details>
<summary>💡 Musterlösung</summary>

**Problem-Analyse:**
- "System" ist keine User-Rolle
- Zu technisch (JSON)
- Kein Nutzen erklärt
- → Umformulieren als nicht-funktionale Anforderung

**Besser:**
```markdown
Titel: Austauschbares Datenformat für Export/Import

## Beschreibung
Das System soll Daten in einem standardisierten Format (JSON)
exportieren können, damit Nutzer ihre Daten sichern und
zwischen Installationen übertragen können.

## Kriterien
- Export-Funktion erstellt JSON-Datei
- JSON enthält alle Zettel-Positionen und Eigenschaften
- Import-Funktion liest JSON-Datei
- Format ist dokumentiert
- Abwärtskompatibel (alte Exporte funktionieren)

## Priorität: Nice-to-Have
```

**Alternative:** Als User Story
```markdown
Titel: Als Nutzer will ich meine Anordnung exportieren können

## Beschreibung
Als Nutzer will ich meine gesamte Zettel-Anordnung in eine
Datei exportieren können, damit ich ein Backup habe oder
die Anordnung auf einem anderen Rechner nutzen kann.

## Akzeptanzkriterien
- [ ] "Exportieren"-Button in der UI
- [ ] Export erstellt .json Datei
- [ ] Datei enthält alle Positionen und Verbindungen
- [ ] "Importieren"-Funktion lädt Datei wieder
- [ ] Import stellt Anordnung wieder her

## Priorität: Nice-to-Have
## Story Points: 5
```
</details>

### Übung 3: Akzeptanzkriterien finden

**Gegeben: User Story ohne Kriterien**
```markdown
Als Nutzer will ich Zettel mit der Maus verschieben können
```

**Aufgabe:** Findet 5 Akzeptanzkriterien!

<details>
<summary>💡 Musterlösung</summary>

```markdown
## Akzeptanzkriterien
- [ ] Ich kann einen Zettel mit Linksklick greifen
- [ ] Der Zettel folgt der Maus während ich die Taste halte
- [ ] Der Zettel wird beim Loslassen an neuer Position platziert
- [ ] Die neue Position wird automatisch gespeichert
- [ ] Verbindungslinien bewegen sich mit dem Zettel
- [ ] Andere Zettel werden nicht verschoben
- [ ] Drag funktioniert auch bei überlappenden Zetteln
```
</details>

---

## ✅ CHECKLISTE

Habt ihr verstanden:
- [ ] Was Anforderungsanalyse ist? (Zweck?)
- [ ] Warum man das VOR dem Programmieren macht?
- [ ] Was User Stories sind? (Format?)
- [ ] Was INVEST-Kriterien sind?
- [ ] Was Akzeptanzkriterien sind?
- [ ] Unterschied funktional vs. nicht-funktional?
- [ ] Warum "Als System" falsch ist?
- [ ] Was in euren Issues problematisch ist?
- [ ] Wie ihr sie verbessern würdet?

**Alle ✅?** Dann weiter zu Aufgabe 4!

---

## ➡️ NÄCHSTER SCHRITT

**Weiter zu:** `04-Strategischer-Entwurf-ERKLAERT.md`

Dort geht's um eure Architektur (MVC, ADRs, Diagramme)!
