# 📖 GLOSSAR: Alle wichtigen Begriffe erklärt

**Zweck:** Wenn ihr einen Begriff nicht versteht, schlagt ihr hier nach!

Die Begriffe sind alphabetisch sortiert und einfach erklärt.

---

## A

### ADR (Architecture Decision Record)
**Was:** Dokument das eine Architektur-Entscheidung dokumentiert

**Warum:** In 6 Monaten wisst ihr nicht mehr WARUM ihr Entscheidung X getroffen habt. ADR hilft!

**Aufbau:**
1. Situation (Problem)
2. Bewertungskriterien
3. Alternativen
4. Bewertung
5. Entscheidung
6. Konsequenzen

**Beispiel:** "Warum SQLite statt PostgreSQL?"

**Analogie:** Wie ein Tagebuch-Eintrag: "Heute habe ich X entschieden weil Y und Z"

---

### API (Application Programming Interface)
**Was:** Schnittstelle zwischen zwei Software-Systemen

**Warum:** Software A will mit Software B reden → braucht API

**Beispiel ZettelWeb:**
- ZettelWeb (Software A) will Zettel abrufen
- Zettelstore (Software B) hat eine API
- ZettelWeb ruft API auf: "Gib mir alle Zettel"

**Analogie:** Restaurant
- Ihr = Software A
- Kellner = API
- Küche = Software B

Ihr sagt dem Kellner was ihr wollt → Kellner holt es aus der Küche

---

### Anforderung
**Was:** Festlegung was die Software können/sein soll

**Zwei Arten:**

1. **Funktionale Anforderung:**
   - Was soll die Software TUN?
   - Beispiel: "User kann Zettel verschieben"

2. **Nicht-funktionale Anforderung:**
   - WIE SOLL es sein? (Qualität)
   - Beispiel: "System soll schnell reagieren (<200ms)"

**Warum wichtig:** Ohne Anforderungen wisst ihr nicht WAS ihr bauen sollt!

---

### Architektur (Software-Architektur)
**Was:** Grob-Struktur der Software BEVOR man programmiert

**Was gehört dazu:**
- Welche Komponenten gibt es? (z.B. Model, View, Controller)
- Wie kommunizieren sie? (z.B. Funktionsaufrufe, API)
- Wo sind Daten? (z.B. Datenbank, Dateien)
- Warum diese Struktur? (Begründung)

**Analogie Hausbau:**
- Architektur = Bauplan (Zimmer, Stockwerke, Leitungen)
- Implementierung = Tatsächlich bauen

**Warum wichtig:**
- Plant man schlecht → später Probleme beim Programmieren
- Plant man gut → Programmieren wird einfacher

---

## F

### Funktionale Anforderung
**Was:** Beschreibt eine FUNKTION die die Software haben soll

**Format:** "Als [ROLLE] will ich [FUNKTION]"

**Beispiele:**
- ✅ "Als Nutzer will ich Zettel verschieben können"
- ✅ "Als System will ich Positionen speichern"
- ❌ "Das System soll schnell sein" (Das ist nicht-funktional!)

**Test:** Kann man es demonstrieren? JA → funktional

---

## G

### Git Repository
**Was:** Ordner der mit Git versioniert wird

**Warum:** Teamarbeit + Versionshistorie

**Für euer Projekt:**
- https://github.com/Aphelion-Z/zettelweb
- Enthält Code, Dokumente, Issues, Wiki

---

## I

### Issue (GitHub Issue)
**Was:** "Ticket" für eine Aufgabe/Anforderung/Bug

**Für euer Projekt:** User Stories als Issues

**Beispiel:**
```
Titel: Als Nutzer will ich Zettel verschieben können
Beschreibung: ...
Labels: feature, must-have
```

**Warum als Issues:** Gut verfolgbar, diskutierbar, zuweisbar

---

## J

### JSON (JavaScript Object Notation)
**Was:** Datenformat für APIs

**Beispiel:**
```json
{
  "id": "123",
  "title": "Mein Zettel",
  "tags": ["test", "demo"]
}
```

**Warum wichtig:** Zettelstore API gibt JSON zurück

---

## M

### Metadaten
**Was:** Daten ÜBER Daten

**Für Zettel:**
- title = Titel des Zettels
- tags = Schlagworte
- syntax = Formatierung
- created = Erstellungsdatum

**Warum:** Um Zettel zu beschreiben und zu finden

---

### MVC (Model-View-Controller)
**Was:** Architektur-Pattern mit 3 Komponenten

**Die drei Teile:**

1. **Model (Daten + Logik)**
   - Speichert Daten
   - Berechnet Dinge
   - Beispiel: Zettel laden, Positionen speichern

2. **View (Darstellung)**
   - Zeigt Daten an
   - UI/Interface
   - Beispiel: Zettel als Boxen rendern

3. **Controller (Steuerung)**
   - Vermittelt zwischen Model und View
   - Reagiert auf User-Input
   - Beispiel: User klickt → Model updaten → View neu rendern

**Restaurant-Analogie:**
- Model = Küche (bereitet Essen vor)
- View = Teller (präsentiert Essen)
- Controller = Kellner (vermittelt Bestellung)

**Warum MVC gut:**
- Trennung der Verantwortlichkeiten
- Model ändern ohne View zu ändern
- Einfacher zu testen

---

## N

### Nicht-funktionale Anforderung
**Was:** Beschreibt QUALITÄTS-Eigenschaft der Software

**Kategorien:**
- Performance (Geschwindigkeit)
- Skalierbarkeit (wie viele User/Daten)
- Security (Sicherheit)
- Usability (Benutzerfreundlichkeit)
- Wartbarkeit

**Beispiele:**
- ✅ "System soll 200 Zettel flüssig darstellen"
- ✅ "Reaktionszeit < 200ms"
- ✅ "Positionen innerhalb 3 Sekunden speichern"

**Test:** Kann man es MESSEN? JA → nicht-funktional

---

### Nicht-Anforderung
**Was:** Explizit festlegen was NICHT im Projekt ist

**Warum:** Scope begrenzen, Missverständnisse vermeiden

**Beispiel ZettelWeb:**
"Schriftarten wählbar" ist KEINE Anforderung

---

## P

### Projektauftrag
**Was:** Dokument das Projekt definiert

**Inhalt:**
- Projektziel
- Team (wer macht mit?)
- Zeitplan (wie lange?)
- Meilensteine
- Risiken

**Für euer Projekt:** README.md

**Warum:** Damit alle wissen worum es geht

---

## R

### REST API
**Was:** API-Stil basierend auf HTTP

**Prinzipien:**
- Ressourcen (z.B. Zettel)
- URLs (z.B. `/z/123`)
- HTTP-Methoden (GET, POST, PUT, DELETE)

**Beispiel:**
```
GET /z/20251027123456
→ Holt Zettel mit dieser ID
```

**Für euer Projekt:** Zettelstore hat REST API

---

## S

### SMART-Kriterien
**Was:** Anforderungen sollen SMART sein

- **S**pecific (Spezifisch): Klar formuliert
- **M**easurable (Messbar): Kann man testen
- **A**chievable (Erreichbar): Ist machbar
- **R**elevant (Relevant): Macht Sinn fürs Projekt
- **T**ime-bound (Zeitgebunden): Bis wann?

**Beispiel:**
- ❌ "System soll schnell sein" (nicht messbar!)
- ✅ "Reaktionszeit < 200ms" (messbar!)

---

### SQLite
**Was:** Datei-basierte Datenbank

**Warum für euer Projekt:**
- Einfach (keine Server-Installation)
- Portable (eine Datei)
- Ausreichend für lokale Anwendung

**Alternative:** PostgreSQL, MySQL (brauchen Server)

---

### Stakeholder
**Was:** Person/Gruppe die vom Projekt betroffen ist

**Für Software-Projekte:**
- User (nutzen die Software)
- Entwickler (bauen die Software)
- Auftraggeber (zahlen/wollen die Software)
- Betreiber (hosten/warten die Software)

**Für euer Projekt:**
- Ihr selbst (Entwickler + User)
- Prof. Stern (Auftraggeber/Bewerter)

---

## U

### UML (Unified Modeling Language)
**Was:** Sprache für Diagramme

**Typen:**
- Klassendiagramm (welche Klassen, Beziehungen)
- Sequenzdiagramm (Ablauf über Zeit)
- Komponentendiagramm (Systemaufbau)

**Für euer Projekt:**
- Klassendiagramm der MVC-Architektur
- Komponentendiagramm (Systemaufbau)

---

### User Story
**Was:** Anforderung aus User-Sicht

**Format:**
```
Als [ROLLE]
will ich [FUNKTIONALITÄT]
damit/weil [NUTZEN/GRUND]
```

**Beispiel:**
```
Als Nutzer
will ich Zettel verschieben können
damit ich sie nach Themen gruppieren kann
```

**Warum wichtig:** Fokus auf User-Bedürfnis (nicht Technik!)

**Schlechtes Beispiel:**
"Als System will ich Datenbank nutzen" → Zu technisch!

**Gutes Beispiel:**
"Als Nutzer will ich meine Anordnung speichern können" → User-Perspektive!

---

## Z

### Zettel
**Was:** Eine Notiz/Wissenseinheit im Zettelstore

**Bestandteile:**
- ID (eindeutige Kennung, z.B. 20251027123456)
- Metadaten (title, tags, etc.)
- Inhalt (der eigentliche Text)

**Gespeichert als:** Textdatei (`.zettel`)

---

### Zettelkasten
**Was:** System zum Verwalten von verknüpften Notizen

**Prinzip:** Kleine, atomare Notizen die miteinander verlinkt sind

**Bekannte Software:**
- Zettelstore
- Obsidian
- Zettlr

**Euer Projekt:** Visualisierung für Zettelstore-Zettelkasten

---

### Zettelstore
**Was:** Open-Source Software für Zettelkasten

**Was macht es:**
- Speichert Zettel als Textdateien
- Web-Oberfläche zum Verwalten
- REST API für externe Software

**Für euer Projekt:**
- Zettelstore = Datenspeicher
- ZettelWeb = Visualisierung

---

### Zettelmarkup (zmk)
**Was:** Formatierungssprache für Zettel (wie Markdown)

**Beispiel:**
```
= Überschrift

Das ist **fett** und //kursiv//.

* Aufzählungspunkt
* Noch einer

[[Link zu anderem Zettel]]
```

---

## 🔍 SCHNELLSUCHE

**Suche nach Kategorie:**

**Konzepte:**
- Anforderung, User Story, ADR, Architektur, MVC

**Technologien:**
- Zettelstore, SQLite, REST API, JSON, Git

**Dokumente:**
- Projektauftrag, Issue, Wiki, Repository

**Qualität:**
- SMART, Funktional/Nicht-funktional, Stakeholder

---

## 💡 WIE BENUTZEN?

1. **Beim Lesen:** Begriff unklar → hier nachschlagen
2. **Vor Übungen:** Relevante Begriffe nochmal lesen
3. **In Diskussionen:** Als Referenz nutzen
4. **Eigene Notizen:** Mit eigenen Worten aufschreiben

---

## ➡️ NÄCHSTER SCHRITT

**Wenn Glossar gelesen:**
→ Weiter zu `REPO-INVENTUR.md`

Dort seht ihr was in eurem Repository ist und wie es bewertet wird!
