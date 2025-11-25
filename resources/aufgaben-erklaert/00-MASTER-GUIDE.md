# 🎯 MASTER GUIDE: Aufgaben 1-4 komplett verstehen

**Ziel dieses Ordners:** Ihr versteht ALLE 4 Aufgaben, alle Begriffe, und wisst ob eure Arbeit gut ist!

---

## ⚠️ WARUM IST DAS WICHTIG?

Ihr habt Issues und Wiki-Seiten erstellt, aber:
- ❌ Versteht nicht wirklich was ein "User Story" ist
- ❌ Wisst nicht was ein "ADR" ist und warum man das macht
- ❌ Versteht MVC nur theoretisch
- ❌ Wisst nicht OB eure Arbeit gut ist
- ❌ Könntet die Aufgaben nicht selbst wiederholen

**Nach diesem Guide:**
- ✅ Versteht ihr jede Aufgabe und WARUM sie wichtig ist
- ✅ Wisst ihr alle Begriffe (User Story, ADR, MVC, etc.)
- ✅ Könnt ihr eure Arbeit selbst bewerten
- ✅ Könnt ihr die Aufgaben eigenständig machen

---

## 📚 ÜBERSICHT: Was ist in diesem Ordner?

```
aufgaben-erklaert/
├── 00-MASTER-GUIDE.md              ← Du bist hier!
├── 00-GLOSSAR.md                   ← Alle Begriffe erklärt
├── 01-Infrastruktur-ERKLAERT.md    ← Aufgabe 1 analysiert
├── 02-Projektauftrag-ERKLAERT.md   ← Aufgabe 2 analysiert
├── 03-Anforderungsanalyse-ERKLAERT.md  ← Aufgabe 3 analysiert
├── 04-Strategischer-Entwurf-ERKLAERT.md ← Aufgabe 4 analysiert
└── REPO-INVENTUR.md                ← Was ist in eurem Repo?
```

---

## 🗺️ ROADMAP: In welcher Reihenfolge lesen?

### Phase 1: Grundlagen (Tag 1) - 2-3 Stunden

**Schritt 1:** `00-GLOSSAR.md` lesen
- Alle wichtigen Begriffe verstehen
- Bei Unklarheiten zurückkommen

**Schritt 2:** `REPO-INVENTUR.md` lesen
- Was ist in eurem Repository?
- Erste Bewertung

### Phase 2: Aufgaben verstehen (Tag 2-3) - 4-6 Stunden

**Schritt 3:** `01-Infrastruktur-ERKLAERT.md`
- Einfachste Aufgabe zuerst
- Verstehen was verlangt war

**Schritt 4:** `02-Projektauftrag-ERKLAERT.md`
- Was ist ein Projektauftrag?
- Euer README bewerten

**Schritt 5:** `03-Anforderungsanalyse-ERKLAERT.md`
- User Stories verstehen
- Eure 12 Issues durchgehen

**Schritt 6:** `04-Strategischer-Entwurf-ERKLAERT.md`
- Architektur, MVC, ADR verstehen
- Eure Architektur-Dokumente bewerten

### Phase 3: Vertiefen (Tag 4-5) - 3-4 Stunden

**Schritt 7:** Guides lesen (`/guides` Ordner)
- Wie macht man es richtig?
- Techniken lernen

**Schritt 8:** Übungen machen (`/uebungen` Ordner)
- Selbst anwenden
- Festigen

---

## 📋 DIE 4 AUFGABEN - Übersicht

### Aufgabe 1: Infrastruktur ⚙️
**Was?** Git-Repository einrichten + `zettel` Ordner erstellen
**Warum?** Teamarbeit ermöglichen
**Status:** ✅ Ihr habt das erfüllt!

### Aufgabe 2: Projektauftrag 📝
**Was?** README mit Projekt-Infos (Ziele, Team, Zeitplan, etc.)
**Warum?** Alle wissen worum es geht
**Status:** ⚠️ Teilweise - siehe Analyse

### Aufgabe 3: Anforderungsanalyse 📊
**Was?** Issues mit User Stories + Nicht-Anforderungen Wiki-Seite
**Warum?** Festlegen WAS gebaut werden soll (bevor man baut!)
**Status:** ⚠️ Teilweise - siehe Analyse

### Aufgabe 4: Strategischer Entwurf 🏗️
**Was?** Architektur-Dokumentation (MVC, ADRs, Diagramme)
**Warum?** Festlegen WIE es gebaut werden soll (Struktur)
**Status:** ⚠️ Teilweise - siehe Analyse

---

## 🎓 WICHTIGSTE KONZEPTE

### Was sind Anforderungen?
**Einfach:** Was soll die Software können?

**Zwei Arten:**
1. **Funktional:** "Als User will ich X machen können"
2. **Nicht-funktional:** "Das System soll schnell sein"

**Beispiel ZettelWeb:**
- Funktional: "Zettel verschieben können"
- Nicht-funktional: "200+ Zettel flüssig darstellen"

### Was ist eine Architektur?
**Einfach:** Grob-Bauplan BEVOR man programmiert

**Analogie Haus:**
- Architektur = Bauplan (Zimmer, Stockwerke, Leitungen)
- Code = Tatsächliches Bauen

**Für Software:**
- Welche Komponenten gibt es? (Model, View, Controller)
- Wie reden sie miteinander? (API, Funktionsaufrufe)
- Wo sind die Daten? (Datenbank, Dateien)

### Was ist MVC?
**M**odel **V**iew **C**ontroller = Architektur-Pattern

**Restaurant-Analogie:**
- **Model** = Küche (bereitet Daten vor)
- **View** = Teller/Präsentation (zeigt Daten)
- **Controller** = Kellner (vermittelt)

**Für ZettelWeb:**
- **Model:** Zettel laden, Positionen speichern
- **View:** Zettel als Boxen anzeigen
- **Controller:** User klickt → Model aktualisieren → View neu rendern

---

## ✅ CHECKLISTE: Verstehe ich jetzt alles?

Arbeitet diese Liste durch. Ehrlich ankreuzen!

### Nach Glossar + Repo-Inventur:
- [ ] Ich weiß was eine User Story ist
- [ ] Ich weiß was ein ADR ist
- [ ] Ich weiß was MVC bedeutet
- [ ] Ich weiß was funktionale Anforderungen sind
- [ ] Ich habe einen Überblick über unser Repository

### Nach Aufgaben-Analysen:
- [ ] Ich verstehe Aufgabe 1 (Infrastruktur)
- [ ] Ich verstehe Aufgabe 2 (Projektauftrag)
- [ ] Ich verstehe Aufgabe 3 (Anforderungsanalyse)
- [ ] Ich verstehe Aufgabe 4 (Strategischer Entwurf)
- [ ] Ich kann unsere Arbeit selbst bewerten

### Nach Guides:
- [ ] Ich kann User Stories schreiben
- [ ] Ich kann ADRs schreiben
- [ ] Ich kann Anforderungen finden
- [ ] Ich verstehe wie man Architektur entwirft

### Nach Übungen:
- [ ] Ich habe User Stories selbst geschrieben
- [ ] Ich habe einen ADR selbst geschrieben
- [ ] Ich habe unsere Issues selbst bewertet
- [ ] Ich habe Übungsprojekte gemacht

**ALLE ✅?** Dann seid ihr bereit für die Coding-Tutorials!

---

## 🔄 DER GROSSE ZUSAMMENHANG

```
Vorlesung (Theorie)
    ↓
Aufgabe 1: Infrastruktur
    ↓ (Git Repo einrichten)
Aufgabe 2: Projektauftrag
    ↓ (Was wollen wir bauen?)
Aufgabe 3: Anforderungen
    ↓ (WAS soll es können?)
Aufgabe 4: Architektur
    ↓ (WIE bauen wir es?)
[JETZT]
    ↓
Implementierung (Programmieren)
    ↓
Testing
    ↓
Fertig!
```

**Ihr seid hier:** Zwischen Architektur und Implementierung

**Problem:** Ihr habt Aufgabe 3+4 erledigt, aber nicht verstanden

**Lösung:** Diese Guides! 📚

---

## 💡 TIPPS

### Tipp 1: Nicht überspringen!
Arbeitet die Dokumente in Reihenfolge durch. Jedes baut auf dem vorherigen auf.

### Tipp 2: Aktiv machen!
Nur lesen reicht nicht. Bei Übungen wirklich selbst machen!

### Tipp 3: Diskutieren!
In der Gruppe: Jeder liest, dann gemeinsam diskutieren.

### Tipp 4: Notizen machen!
Wichtige Erkenntnisse aufschreiben. Eigene Beispiele überlegen.

### Tipp 5: Fragen stellen!
Claude Code fragen wenn etwas unklar ist.

---

## 🆘 WENN IHR NICHT WEITERKOMMT

1. **Glossar** nochmal checken (Begriff unklar?)
2. **Beispiele** anschauen (konkrete Anwendung)
3. **Übungen** machen (Learning by Doing)
4. **Claude Code** fragen

**Format:**
```
Ich lese gerade [Dokument] und verstehe [Begriff/Konzept] nicht.
Kannst du das anders/einfacher erklären?
```

---

## 🎯 ZIEL ERREICHT WENN...

✅ Ihr könnt jemandem erklären was User Stories sind
✅ Ihr könnt ein ADR für eine fiktive Entscheidung schreiben
✅ Ihr wisst warum ihr MVC gewählt habt
✅ Ihr könnt eure Issues selbst bewerten und verbessern
✅ Ihr versteht alle Dokumente in eurem Repository
✅ Ihr könntet Aufgabe 3+4 nochmal machen (ohne LLM!)

---

## ➡️ NÄCHSTER SCHRITT

**Öffne jetzt:** `00-GLOSSAR.md`

Dort werden alle wichtigen Begriffe erklärt. Das ist die Basis für alles weitere!

**Let's go! 🚀**
