# Tutorial 02: Zettel erstellen und verknüpfen

**Zeit:** 20 Minuten
**Schwierigkeit:** 🟢 Einfach
**Voraussetzung:** Tutorial 01 abgeschlossen

---

## 🎯 Ziel

Am Ende dieses Tutorials:
- ✅ Habt ihr 3 eigene Zettel erstellt
- ✅ Versteht ihr Metadaten (Title, Tags, etc.)
- ✅ Könnt ihr Zettel miteinander verknüpfen
- ✅ Versteht ihr Zettel-IDs

---

## 📝 Vorbereitung

1. Zettelstore starten (`zettelstore.exe`)
2. Browser öffnen: `http://localhost:23123`

Bereit? Los geht's!

---

## 📄 Schritt 1: Ersten eigenen Zettel erstellen

**Aufgabe 1.1:** Neuen Zettel anlegen

1. Klickt oben im Menü auf **"New"**
2. Ein Formular erscheint mit vielen Feldern

**Was ihr seht:**
- **Title:** Titel des Zettels
- **Tags:** Schlagworte (kommagetrennt)
- **Syntax:** Formatierungssprache (lassen wir auf "zmk" = Zettelmarkup)
- **Content:** Der eigentliche Inhalt

**Aufgabe 1.2:** Ersten Zettel ausfüllen

Gebt folgendes ein:

```
Title: Mein erster Zettel
Tags: test, tutorial
Syntax: zmk (nicht ändern)

Content:
Das ist mein erster eigener Zettel im Zettelstore!

Ich lerne gerade wie Zettelstore funktioniert.
```

**Aufgabe 1.3:** Zettel speichern

1. Scrollt nach unten
2. Klickt auf **"Create"**
3. 🎉 Euer Zettel wird angezeigt!

📸 **Checkpoint:** Seht ihr euren Zettel? JA → weiter!

---

## 🔢 Schritt 2: Zettel-ID verstehen

Schaut euch die URL im Browser an:

```
http://localhost:23123/h/20251027123456
                           ^^^^^^^^^^^^^
                           Das ist die Zettel-ID!
```

**Was bedeutet die ID?**
- `20251027123456` = Zeitstempel
- Format: `YYYYMMDDHHmmSS`
- `2025` = Jahr
- `10` = Monat (Oktober)
- `27` = Tag
- `12` = Stunde
- `34` = Minute
- `56` = Sekunde

**Warum Zeitstempel?**
- Jede ID ist garantiert einzigartig
- Sortierung chronologisch möglich
- Einfach zu generieren

**Aufgabe 2.1:** Findet eure Zettel-ID

1. Schaut in die Browser-URL
2. Kopiert die 14-stellige Zahl (eure ID wird anders sein!)
3. Merkt euch: Das ist die ID von "Mein erster Zettel"

---

## 📝 Schritt 3: Zweiten Zettel erstellen

**Aufgabe 3.1:** Noch einen Zettel!

1. Klickt wieder auf "New"
2. Gebt ein:

```
Title: Zettelstore Features
Tags: zettelstore, features
Syntax: zmk

Content:
Zettelstore Features:

* Einfache Textdateien
* Metadaten-System
* Verknüpfungen zwischen Zetteln
* Web-Oberfläche
* REST API
```

3. "Create" klicken

📸 **Checkpoint:** Zweiter Zettel erstellt? JA → weiter!

---

## 🔗 Schritt 4: Zettel verknüpfen

Jetzt kommt's! Wir verknüpfen die beiden Zettel.

**Aufgabe 4.1:** Dritten Zettel mit Verknüpfung erstellen

1. Wieder auf "New" klicken
2. Gebt ein:

```
Title: Meine Zettel-Übersicht
Tags: übersicht, index
Syntax: zmk

Content:
Das sind meine wichtigsten Zettel:

* [[Mein erster Zettel]]
* [[Zettelstore Features]]

Später füge ich hier mehr hinzu.
```

3. "Create" klicken

**❗ WICHTIG:** Die `[[...]]` Syntax!
- `[[Titel]]` = Verknüpfung zu einem Zettel mit diesem Titel
- Wird automatisch aufgelöst

**Aufgabe 4.2:** Verknüpfungen testen

1. Schaut euch euren neuen Zettel an
2. Die Texte in `[[...]]` sollten jetzt **anklickbare Links** sein!
3. Klickt auf "Mein erster Zettel"
4. 🎉 Ihr springt zu eurem ersten Zettel!
5. Klickt "Back" im Browser
6. Klickt auf "Zettelstore Features"
7. 🎉 Funktioniert auch!

📸 **Checkpoint:** Funktionieren die Links? JA → weiter!

---

## 🏷️ Schritt 5: Mit Tags arbeiten

Tags = Schlagworte, um Zettel zu gruppieren.

**Aufgabe 5.1:** Zettel nach Tags filtern

1. Klickt im Menü auf "Filters"
2. Klickt auf "Tags"
3. Ihr seht alle Tags die existieren (auch eure!)
4. Klickt auf euren Tag "test"
5. Zeigt alle Zettel mit diesem Tag

**Aufgabe 5.2:** Tag hinzufügen

1. Geht zurück zu "Mein erster Zettel"
2. Oben rechts: Klickt auf "Edit" (oder "Bearbeiten")
3. Im Tags-Feld: Fügt einen weiteren Tag hinzu: `test, tutorial, learning`
4. "Update" klicken
5. Jetzt hat der Zettel 3 Tags!

---

## 📊 Schritt 6: Metadaten verstehen

Jeder Zettel hat Metadaten. Schaut euch einen eurer Zettel an.

**Was ihr oben seht:**

```
Title: Mein erster Zettel
Tags: test, tutorial, learning
Syntax: zmk
Role: zettel
```

**Was bedeutet das?**

| Metadatum | Bedeutung | Beispiel |
|-----------|-----------|----------|
| **title** | Titel des Zettels | "Mein erster Zettel" |
| **tags** | Schlagworte (kommagetrennt) | "test, tutorial" |
| **syntax** | Format des Inhalts | "zmk" = Zettelmarkup |
| **role** | Art des Zettels | "zettel" = normaler Zettel |

Es gibt noch mehr Metadaten (automatisch):
- **id:** Zettel-ID
- **created:** Erstellungszeitpunkt
- **modified:** Letzte Änderung
- **published:** Publikationszeitpunkt

**Aufgabe 6.1:** Metadaten anschauen

1. Geht zu einem eurer Zettel
2. Scrollt nach unten
3. Klickt auf "Info" (falls vorhanden) oder schaut oben nach
4. Seht ihr `created`, `modified`?

---

## ✍️ Schritt 7: Zettelmarkup-Formatierung

Zettelmarkup = Formatierungssprache (wie Markdown).

**Aufgabe 7.1:** Neuen Zettel mit Formatierung

```
Title: Formatierungs-Test
Tags: test, formatierung
Syntax: zmk

Content:
= Große Überschrift

== Kleinere Überschrift

Das ist **fett** und das ist //kursiv//.

* Aufzählungspunkt 1
* Aufzählungspunkt 2
* Aufzählungspunkt 3

Das ist ein [[Link zu einem anderen Zettel]].

Das ist eine URL: https://zettelstore.de
```

**Was passiert:**
- `=` und `==` = Überschriften
- `**text**` = fett
- `//text//` = kursiv
- `*` = Aufzählungspunkt
- `[[...]]` = Link zu Zettel
- URLs werden automatisch zu Links

📸 **Checkpoint:** Formatierung sichtbar? JA → weiter!

---

## 🎓 Was ihr gelernt habt

✅ **Zettel erstellen** mit "New"
✅ **Zettel-IDs** sind Zeitstempel (14 Ziffern)
✅ **Metadaten:** Title, Tags, Syntax, etc.
✅ **Verknüpfungen:** `[[Titel]]` Syntax
✅ **Tags** zum Gruppieren und Filtern
✅ **Zettelmarkup** für Formatierung

---

## 🧪 Übungsaufgabe (10 Min)

Erstellt folgende Zettel-Struktur:

**Zettel 1: "Programmiersprachen"**
- Tags: informatik, programmierung
- Inhalt: Liste mit `* JavaScript`, `* Python`, `* Go`
- Verknüpfung zu "JavaScript Basics"

**Zettel 2: "JavaScript Basics"**
- Tags: javascript, programmierung
- Inhalt: "JavaScript ist eine Programmiersprache für Web-Entwicklung."
- Verknüpfung zurück zu "Programmiersprachen"

**Zettel 3: "Index"**
- Tags: index
- Inhalt: Verknüpfungen zu beiden anderen Zetteln

**Testet:**
- Könnt ihr von Index zu den anderen Zetteln navigieren?
- Könnt ihr über Tags filtern?

---

## ✅ Checkpoint: Bist du bereit?

- [ ] Habe ich 3+ eigene Zettel erstellt?
- [ ] Verstehe ich Zettel-IDs?
- [ ] Kann ich Zettel verknüpfen mit `[[...]]`?
- [ ] Verstehe ich Metadaten (Title, Tags)?
- [ ] Habe ich die Übungsaufgabe gemacht?

**Alle ✅?** Weiter zu Tutorial 03!

---

## 🆘 Troubleshooting

### Problem: "Link funktioniert nicht"

**Lösung:**
- Titel exakt richtig geschrieben? (Case-sensitive!)
- Oder nutzt die Zettel-ID: `[[20251027123456]]`

### Problem: "Kann Zettel nicht finden"

**Lösung:**
- "Filters" → "All" klicken (zeigt alle Zettel)
- Oder Suche nutzen

---

## ➡️ Nächster Schritt

**Tutorial 03: Zettel-Dateien verstehen**

Jetzt wo ihr Zettel erstellen könnt, schauen wir uns an wo diese gespeichert werden!
