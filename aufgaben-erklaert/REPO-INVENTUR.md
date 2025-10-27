# 📦 REPOSITORY-INVENTUR: Was ist in eurem Repo?

**Ziel:** Überblick über eure abgegebene Arbeit + erste Bewertung

---

## 🗂️ WAS IST ALLES DA?

### Dateistruktur

```
zettelweb-code/
├── README.md                    ← Projektauftrag (Aufgabe 2)
├── zettel/                      ← Zettel-Ordner (Aufgabe 1)
│   └── .gitkeep
├── wiki/                        ← Architektur-Doku (Aufgabe 4)
│   ├── Nicht-Anforderungen.md
│   ├── Strategischer-Entwurf.md
│   ├── Strategischer-Entwurf/
│   │   ├── ADR-01-SYSTEMINTEGRATION.md
│   │   ├── ADR-02-Wahl-von-SQLite.md
│   │   ├── Klassendiagramm-MVC.md
│   │   └── Systemaufbau.md
│   └── uploads/                 ← Screenshots/Diagramme
├── tutorials/                   ← Lern-Tutorials (neu)
└── CLAUDE.md                    ← Hilfe für Claude Code
```

### GitHub Issues (Aufgabe 3)

**13 Issues erstellt:**
1. Als Nutzer will ich durch das hinzufügen von "Tags" Zettel unterschiedlich gruppieren können
2. Als Nutzer will ich, dass zwischen zusammenhängenden Zetteln Linienverbindungen angezeigt werden
3. Als Nutzer will ich, dass beim Überfahren eines Zettels dieser und seine direkt verbundenen Zettel hervorgehoben werden
4. Als Nutzer will ich, dass beim verschieben eines Zettels alle direkt verbundenen Zettel mit einer schnurartigen Animation elastisch nachgezogen werden
5. Als System will ich die aktuellen Koordinaten jedes verschobenen Zettels in einer Datenbank speichern
6-13. [Weitere Issues...]

**Alle Status:** OPEN (noch nicht bearbeitet)

---

## 📊 BEWERTUNG PRO AUFGABE

### ✅ Aufgabe 1: Infrastruktur - ERFÜLLT

**Was wurde verlangt:**
- Git-Repository einrichten ✓
- "zettel" Ordner erstellen ✓
- URL abgeben ✓
- Prof. Stern Zugriff geben ✓

**Was ihr habt:**
- ✓ GitHub Repository: https://github.com/Aphelion-Z/zettelweb
- ✓ `zettel/` Ordner vorhanden
- ✓ Alle Teammitglieder haben Zugriff

**Bewertung:** **100% erfüllt** ✅

**Verbesserungspotential:** Keine - perfekt erledigt!

---

### ⚠️ Aufgabe 2: Projektauftrag - TEILWEISE ERFÜLLT

**Was wurde verlangt:**
- README.md als Projektauftrag ✓
- Struktur aus "Projektmanagement" (WIN2) ✓
- Sofort einsehbar beim Öffnen des Repos ✓

**Was ihr habt:**

**Vorhanden in README.md:**
- ✓ Projektname ("ZettelWeb Gruppe 7")
- ✓ Kurzbeschreibung
- ✓ Ziele (6 Punkte)
- ✓ Personal- und Zeitaufwand (7 Personen, 125h)
- ✓ Meilensteine (7 Stück)
- ✓ Risiken (3 Punkte)
- ✓ Unterschriften (Team-Mitglieder)

**Was GUT ist:**
- Struktur vorhanden
- Alle Pflichtelemente da
- Ziele sind konkret

**Was FEHLT/verbesserbar:**
- ❌ Projekthintergrund/Kontext fehlt ("Warum machen wir das?")
- ❌ Erfolgskriterien nicht definiert ("Wann ist es erfolgreich?")
- ⚠️ Meilensteine zu grob (keine konkreten Deadlines)
- ⚠️ Risiken ohne Gegenmaßnahmen
- ⚠️ Keine Ressourcen/Budget erwähnt (falls relevant)

**Bewertung:** **75% erfüllt** ⚠️

**Verbesserungsvorschlag:** Siehe `02-Projektauftrag-ERKLAERT.md`

---

### ⚠️ Aufgabe 3: Anforderungsanalyse - TEILWEISE ERFÜLLT

**Was wurde verlangt:**
- Issues mit funktionalen Anforderungen (User Stories) ✓
- Satzschablone: "Als ROLLE will ich FUNKTIONALITÄT, weil BEGRÜNDUNG" ✓
- Nicht-funktionale Anforderungen (System-Requirements) ✓
- Wiki-Seite "Nicht-Anforderungen" ✓
- SMART-Kriterien beachtet ⚠️

**Was ihr habt:**

**Issues (Gesamt: 13 Stück):**

**FUNKTIONALE (User Stories):** 8 Issues
- ✓ Format meist korrekt ("Als Nutzer will ich...")
- ✓ Konkrete Features beschrieben
- Beispiele:
  - Issue #2: "Als Nutzer will ich Tags hinzufügen"
  - Issue #3: "Als Nutzer will ich Linienverbindungen sehen"

**NICHT-FUNKTIONALE (System-Requirements):** 5 Issues
- ✓ Format korrekt ("Das System soll...")
- ✓ Messbare Kriterien
- Beispiele:
  - Issue #11: "200 Zettel mit 30fps, <200ms Reaktionszeit"
  - Issue #12: "Speichern innerhalb 3 Sekunden"

**Nicht-Anforderungen.md:**
- ✓ Wiki-Seite vorhanden
- ✓ Explizit ausgeschlossen: "Schriftarten/Schriftgröße ändern"
- ⚠️ Nur 1 Nicht-Anforderung (könnte mehr sein)

**Was GUT ist:**
- Satzschablonen konsequent genutzt
- Mix aus funktional/nicht-funktional
- Nicht-funktionale haben messbare Kriterien (SMART!)
- Gute Abdeckung der Projekt-Idee

**Was PROBLEMATISCH ist:**

**Issue #1 & #2 sind identisch!**
- Titel: "Als Nutzer will ich durch das hinzufügen von 'Tags' Zettel unterschiedlich gruppieren können"
- → Duplikat, sollte gelöscht werden

**Issue #5: "Als System will ich..."**
- ⚠️ "System" ist keine User-Rolle!
- Besser: "Als Nutzer will ich, dass meine Zettel-Positionen automatisch gespeichert werden"
- Oder: Als nicht-funktionale Anforderung formulieren

**Manche Issues zu vage:**
- Issue #7: "Cluster erstellen/erweitern" - WAS genau bedeutet das?
- Issue #4: "schnurartige Animation" - zu technisch, schwer testbar

**Fehlende Details:**
- Bei keinem Issue sind Akzeptanzkriterien angegeben
- Keine Prioritäten (must-have, nice-to-have)
- Keine Story Points / Aufwandsschätzung

**Nicht-Anforderungen zu dünn:**
- Nur 1 Punkt
- Könnten mehr sein (z.B. "Keine Kollaboration", "Keine Cloud-Sync", etc.)

**Bewertung:** **65% erfüllt** ⚠️

**Verbesserungsvorschlag:** Siehe `03-Anforderungsanalyse-ERKLAERT.md`

---

### ⚠️ Aufgabe 4: Strategischer Entwurf - TEILWEISE ERFÜLLT

**Was wurde verlangt:**
- Architektur zur inneren Struktur festlegen ✓
- Mit Architekturbausteine (Patterns) ✓
- UML-Diagramme zur Erläuterung ✓
- Systemaufbau (Gesamtsystem mit Zettelstore) ✓
- ADRs für Entwurfsentscheidungen ✓
- Wiki-Dokumentation ✓

**Was ihr habt:**

**Architektur-Entscheidung:**
- ✓ MVC (Model-View-Controller) gewählt
- ✓ Begründung vorhanden ("Wahl des Architekturmodells + Begründung")
- ✓ Alternativen erwähnt (SAO, Pipes&Filters)

**ADRs (Architecture Decision Records):**
1. **ADR-01: Systemintegration**
   - ✓ Struktur korrekt (Situation, Alternativen, Bewertung, Entscheidung, Konsequenzen)
   - ✓ 2 Alternativen verglichen (Standalone vs. Zettelstore-Extension)
   - ✓ Bewertungskriterien definiert
   - ✓ Entscheidung: Standalone Web-App
   - ✓ Konsequenzen benannt

2. **ADR-02: Datenbankwahl**
   - ✓ Struktur korrekt
   - ✓ 3 Alternativen (SQLite, MySQL, PostgreSQL)
   - ✓ Bewertungskriterien (6 Stück)
   - ✓ Entscheidung: SQLite
   - ✓ Konsequenzen benannt

**Diagramme:**
1. **Klassendiagramm (MVC)**
   - ✓ Vorhanden (Screenshot)
   - ✓ Model, View, Controller klar getrennt
   - ✓ Klassen benannt (Zettel, Tag, ZettelCluster, ...)
   - ✓ Beziehungen eingezeichnet

2. **Systemaufbau (Komponentendiagramm)**
   - ✓ Vorhanden (Screenshot)
   - ✓ Zeigt: Browser, NetzWeb Backend, Zettelstore, DB
   - ✓ Kommunikation (HTTPS/JSON, REST)

**Textuelle Beschreibung:**
- ✓ Ausführliche Erklärung des MVC-Modells
- ✓ Erklärung der Klassen und deren Verantwortlichkeiten
- ✓ Datenfluss beschrieben

**Was GUT ist:**
- ADRs sehr gut strukturiert!
- Bewertungskriterien vorhanden
- Alternativen werden fair verglichen
- Konsequenzen sind benannt (auch negative!)
- Diagramme unterstützen Text
- MVC-Wahl ist nachvollziehbar begründet

**Was FEHLT/verbesserbar:**

**ADRs:**
- ⚠️ Nur 2 ADRs - es fehlen weitere Entscheidungen:
  - Frontend-Technologie (HTML/CSS/JS, aber welches Framework?)
  - Wie wird Drag & Drop umgesetzt? (Library?)
  - Wie werden Verbindungslinien gezeichnet? (Canvas vs SVG?)

**Klassendiagramm:**
- ⚠️ Screenshot schwer lesbar
- ⚠️ Keine Attribute/Methoden bei Klassen sichtbar
- ⚠️ Beziehungstypen unklar (Assoziation, Vererbung, ...)

**Systemaufbau:**
- ⚠️ "NetzWeb Backend" - wird das wirklich gebaut? Oder nur Frontend?
  - ADR-01 sagt "JavaScript im Browser" → dann kein Backend?
  - **Widerspruch zwischen ADR-01 und Systemaufbau-Diagramm!**

**Architektur vs. Implementierung:**
- ❓ Wie sieht die Ordnerstruktur aus? (src/, model/, view/, controller/?)
- ❓ Welche Dateien gehören zu Model/View/Controller?
- ❓ Wie wird die Architektur in Code umgesetzt?

**Testbarkeit:**
- ❌ Nicht erwähnt wie man die Architektur testen will
- ❌ Keine Test-Strategie

**Bewertung:** **70% erfüllt** ⚠️

**Verbesserungsvorschlag:** Siehe `04-Strategischer-Entwurf-ERKLAERT.md`

---

## 📈 GESAMTBEWERTUNG

| Aufgabe | Status | Prozent | Note (geschätzt) |
|---------|--------|---------|------------------|
| Aufgabe 1 | ✅ Erfüllt | 100% | 1.0 |
| Aufgabe 2 | ⚠️ Teilweise | 75% | 2.3 |
| Aufgabe 3 | ⚠️ Teilweise | 65% | 2.7 |
| Aufgabe 4 | ⚠️ Teilweise | 70% | 2.5 |
| **Gesamt** | **⚠️** | **~70%** | **~2.5** |

**Interpretation:**
- **Basis ist da!** Ihr habt alle Aufgaben bearbeitet
- **Aber:** Vieles ist oberflächlich oder unklar
- **Problem:** LLM-generiert ohne Verständnis?

---

## 🎯 WAS BEDEUTET DAS?

### Positiv ✅
- Ihr habt formal alle Aufgaben abgegeben
- Struktur und Format meist korrekt
- Grundlegende Inhalte vorhanden

### Negativ ❌
- Verständnis fehlt (habt ihr via LLM generiert?)
- Details fehlen oder sind widersprüchlich
- Keine Tiefe bei der Begründung

### Kritisch ⚠️
- **Könnt ihr das selbst wiederholen?** (Ohne LLM?)
- **Versteht ihr eure eigenen Dokumente?**
- **Könnt ihr Fragen dazu beantworten?**

---

## 🔄 WAS JETZT?

**Phase 1: Verstehen** (Diese Guides!)
- Lest die Aufgaben-Analysen (01-04)
- Lernt die Begriffe (Glossar)
- Versteht WARUM ihr was gemacht habt

**Phase 2: Verbessern** (Optional, aber empfohlen)
- Issues überarbeiten (Duplikate löschen, Details hinzufügen)
- Weitere ADRs schreiben
- Widersprüche auflösen

**Phase 3: Umsetzen** (Coding-Tutorials)
- Dann erst programmieren
- Architektur in Code umsetzen
- Issues abarbeiten

---

## ➡️ NÄCHSTER SCHRITT

**Wenn Inventur gelesen:**
→ Weiter zu `01-Infrastruktur-ERKLAERT.md`

Dort wird Aufgabe 1 im Detail erklärt!
