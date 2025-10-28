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

### ❌ Aufgabe 4: Strategischer Entwurf - NICHT BESTANDEN

**Professor-Bewertung:** **"Nicht bestanden"**

**Wörtliches Feedback:**
> "Schwer lesbarer Fließtext, ohne wirkliche Struktur. Im Unterricht hatte ich gesagt, dass eine Web-Anwendung auf Basis von HTTP/1 nie MVC sein kann. Bei den ADRs kann ich nicht erkennen, wie welche Alternative bei welchem Bewertungskriterium abgeschnitten hat. Ich kann weder nachvollziehen, wozu das Klassendiagramm dienen soll, noch wie der Zettelstore Daten an die Datenbank sendet, bzw diese aufruft. Wenn die Entscheidung zur Datenbank auf 'SQLite' lautet, warum wird noch 'Redis' erwähnt? Status: Nicht bestanden."

**Die 6 Hauptkritikpunkte:**

**❌ Kritik #1: MVC für Web-Apps ist FALSCH**
- Ihr habt geschrieben: "webbasierte Client-Server-Anwendung mit MVC-Struktur"
- **Professor hat im Unterricht gesagt:** "Web-App auf HTTP/1 kann NIE MVC sein!"
- MVC = Desktop-Pattern (monolithisch, gleicher Prozess)
- Web-App = Client-Server (verteilt, HTTP dazwischen)
- **Fundamentaler Konzeptfehler!** 🔴

**❌ Kritik #2: Unleserliche Dokumentation**
- Riesige Fließtext-Blöcke ohne Struktur
- Keine Listen, Überschriften, Absätze
- Beispiel: "Wahl des Architekturmodells" = ein einziger Textblock
- Schwer zu lesen, schwer zu scannen

**❌ Kritik #3: ADR-Bewertungen unklar**
- Nur Text statt Bewertungsmatrix-Tabelle
- Professor kann nicht sehen: "Welche Alternative ist bei Kriterium X besser?"
- Keine Scores/Punkte
- Nicht nachvollziehbar

**❌ Kritik #4: Klassendiagramm ohne erkennbaren Zweck**
- Diagramm wird einfach gezeigt (Screenshot)
- Kein Kontext: "Wozu dient dieses Diagramm?"
- Keine Legende: "Was bedeuten die Symbole?"
- Dann folgt allgemeiner Text über MVC

**❌ Kritik #5: Architektur unklar (Zettelstore ↔ DB)**
- Missverständnis in Dokumentation
- Es klingt so als ob Zettelstore eure SQLite-DB verwaltet
- **Wahrheit:** 2 GETRENNTE Datenspeicher!
  - Zettelstore (extern, .zettel Dateien)
  - Eure DB (lokal, nur Positionen)
- Keine Verbindung zwischen beiden!

**❌ Kritik #6: Inkonsistenzen (Redis-Erwähnung)**
- Entscheidung in ADR-02: SQLite
- Redis wird trotzdem irgendwo erwähnt
- Verworfene Alternativen dürfen nicht mehr auftauchen!
- Wirkt unprofessionell

**Was ihr hattet (formale Struktur war ok):**

**ADRs:**
- ✓ ADR-01: Systemintegration (Standalone vs. Extension)
- ✓ ADR-02: Datenbankwahl (SQLite vs. MySQL vs. PostgreSQL)
- ✓ Struktur vorhanden (Situation, Alternativen, Entscheidung, Konsequenzen)

**Diagramme:**
- ✓ Klassendiagramm (MVC)
- ✓ Systemaufbau (Komponentendiagramm)

**Dokumentation:**
- ✓ Wiki-Seiten vorhanden
- ✓ Textuelle Beschreibungen

**ABER: Inhaltlich fundamental falsch + schlecht dokumentiert!**

**Hauptproblem:**
Der MVC-Fehler ist **fundamental** - Professor hat das im Unterricht explizit gesagt und das Team hat nicht zugehört oder es nicht verstanden.

**Bewertung:** **0% (Nicht bestanden)** ❌

**Was zu tun ist:**
1. MVC-Terminologie komplett streichen ("Web-App mit MVC" ist FALSCH!)
2. Korrekt: "Client-Server Architecture / 3-Tier"
3. ADRs mit Bewertungstabellen ergänzen
4. Dokumentation strukturieren (nicht Fließtext!)
5. Diagramme mit Zweck/Kontext/Legende versehen
6. Architektur klarstellen (2 getrennte DBs!)
7. Inkonsistenzen bereinigen

**Detaillierte Analyse:** Siehe `04-Strategischer-Entwurf-ERKLAERT.md`

---

## 📈 GESAMTBEWERTUNG

| Aufgabe | Status | Prozent | Note (tatsächlich) |
|---------|--------|---------|---------------------|
| Aufgabe 1 | ✅ Erfüllt | 100% | 1.0 |
| Aufgabe 2 | ⚠️ Teilweise | 75% | 2.3 |
| Aufgabe 3 | ⚠️ Teilweise | 65% | 2.7 |
| Aufgabe 4 | ❌ **NICHT BESTANDEN** | 0% | **5.0** |
| **Gesamt** | **❌** | **~60%** | **~3.0** |

**Professor-Feedback für Aufgabe 4:**
Fundamentaler MVC-Fehler + unleserliche Dokumentation + unklare ADRs = **Nicht bestanden**

**Interpretation:**
- **Aufgabe 1:** Perfekt! ✅
- **Aufgabe 2-3:** Basis vorhanden, aber verbesserbar ⚠️
- **Aufgabe 4:** Fundamental falsch - durchgefallen! ❌
- **Hauptproblem:** MVC-Fehler (Professor hat das im Unterricht explizit gesagt!)
- **Weiteres Problem:** KI-generierte Arbeit ohne echtes Verständnis

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
