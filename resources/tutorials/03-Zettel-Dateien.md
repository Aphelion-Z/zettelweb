# Tutorial 03: Zettel-Dateien verstehen

**Zeit:** 15 Minuten
**Schwierigkeit:** 🟢 Einfach
**Voraussetzung:** Tutorial 01 + 02 abgeschlossen

---

## 🎯 Ziel

Am Ende dieses Tutorials:
- ✅ Wisst ihr WO Zettel gespeichert werden
- ✅ Versteht ihr das Dateiformat
- ✅ Könnt ihr Zettel-Dateien mit Texteditor öffnen
- ✅ Könnt ihr Zettel manuell erstellen (ohne Web-UI!)
- ✅ Versteht ihr das "Geheimnis" hinter Zettelstore

---

## 🔍 Das große Geheimnis

**Die Wahrheit über Zettelstore:**

Zettelstore ist keine komplexe Datenbank. Es ist viel simpler!

**Zettel = einfache Textdateien auf eurer Festplatte!**

Das war's. Das ist das ganze "Geheimnis". 🎩

Zettelstore:
- Liest Textdateien
- Zeigt sie in der Web-UI an
- Stellt sie über API bereit

**Warum ist das wichtig?**
- Ihr könnt Zettel mit jedem Texteditor bearbeiten
- Kein Vendor Lock-in (nicht abhängig von Zettelstore)
- Einfache Backups (Ordner kopieren = fertig)
- Langlebigkeit (Textdateien funktionieren auch in 50 Jahren)

---

## 📂 Schritt 1: Zettel-Ordner finden

**Wo werden Zettel gespeichert?**

Standard-Speicherort beim ersten Start:

```
C:\Users\<DeinBenutzername>\zettel\
```

ODER (falls ihr Zettelstore aus einem bestimmten Ordner gestartet habt):

```
D:\CLI Projects\SWT\zettelstore\zettelstore-0.22.0-windows-amd64\zettel\
```

**Aufgabe 1.1:** Zettel-Ordner finden

1. Windows Explorer öffnen
2. Navigiert zu einem der Pfade oben
3. Findet den Ordner `zettel` oder `zettel.old` oder ähnlich
4. Öffnet diesen Ordner

**Was ihr seht:**
- Viele Dateien mit `.zettel` Endung
- Dateinamen sind die Zettel-IDs! (z.B. `20251027123456.zettel`)

📸 **Checkpoint:** Seht ihr `.zettel` Dateien? JA → weiter!

**⚠️ Falls ihr den Ordner nicht findet:**

Fragt Zettelstore:
1. Zettelstore läuft?
2. Browser: `http://localhost:23123`
3. Im Menü: Sucht nach "Configuration" oder "Info"
4. Dort steht wo der Zettel-Ordner ist

---

## 📄 Schritt 2: Zettel-Datei öffnen

**Aufgabe 2.1:** Einen eurer Zettel mit Texteditor öffnen

1. Im `zettel` Ordner: Sucht nach einer Datei die ihr heute erstellt habt
2. Rechtsklick auf die `.zettel` Datei
3. "Öffnen mit" → "Notepad" (oder Editor eurer Wahl)

**Was ihr seht:**

```
title: Mein erster Zettel
tags: test, tutorial, learning
syntax: zmk
role: zettel

Das ist mein erster eigener Zettel im Zettelstore!

Ich lerne gerade wie Zettelstore funktioniert.
```

**Die Struktur:**

```
METADATEN (Schlüssel: Wert)
METADATEN (Schlüssel: Wert)
METADATEN (Schlüssel: Wert)

[Leerzeile]

INHALT
INHALT
INHALT
```

**So einfach!**

---

## 🧩 Schritt 3: Dateiformat verstehen

**Format-Regeln:**

1. **Erste Zeilen = Metadaten**
   - Format: `schlüssel: wert`
   - Ein Metadatum pro Zeile
   - Kleinschreibung für Schlüssel

2. **Leerzeile = Trenner**
   - Zwischen Metadaten und Inhalt
   - Genau EINE Leerzeile

3. **Rest = Inhalt**
   - Alles nach der Leerzeile
   - Formatiert in Zettelmarkup (oder anderer Syntax)

**Beispiel annotiert:**

```
title: Formatierungs-Test          ← Metadatum 1
tags: test, formatierung            ← Metadatum 2
syntax: zmk                         ← Metadatum 3
role: zettel                        ← Metadatum 4
                                    ← LEERZEILE (wichtig!)
= Große Überschrift                 ← INHALT beginnt hier

Das ist **fett**.
```

---

## ✏️ Schritt 4: Zettel manuell bearbeiten

Jetzt kommt's: Ihr könnt Zettel direkt im Texteditor ändern!

**Aufgabe 4.1:** Zettel im Editor ändern

1. Öffnet einen eurer Zettel im Texteditor (wie in Schritt 2)
2. Ändert etwas am Inhalt (z.B. fügt eine Zeile hinzu)
3. **Speichern** (Strg+S)
4. Geht zum Browser (Zettelstore Web-UI)
5. Zettel neu laden (F5 oder "Refresh" klicken)
6. 🎉 Eure Änderung ist sichtbar!

**Was ihr gelernt habt:** Zettelstore liest die Datei jedes Mal neu wenn ihr sie anfragt. Keine Magie!

---

## 🆕 Schritt 5: Zettel manuell erstellen

Jetzt die Königsdisziplin: Zettel ohne Web-UI erstellen!

**Aufgabe 5.1:** Neuen Zettel als Textdatei erstellen

1. Öffnet Notepad/Editor
2. Erstellt folgende Datei:

```
title: Manuell erstellter Zettel
tags: test, manuell
syntax: zmk
role: zettel

Diesen Zettel habe ich ohne die Web-UI erstellt!

Ich habe ihn direkt als Textdatei geschrieben.

Das ist **sehr mächtig**!
```

3. **Wichtig:** Speichert die Datei mit einer Zeitstempel-ID:
   - Dateiname: `20251027150000.zettel` (passt die Zeit an!)
   - Speicherort: In den `zettel` Ordner
   - Format: "Alle Dateien" (nicht .txt!)

4. Geht zur Zettelstore Web-UI
5. Klickt auf "Filters" → "All"
6. 🎉 Euer manuell erstellter Zettel erscheint in der Liste!

📸 **Checkpoint:** Seht ihr euren manuell erstellten Zettel? JA → super!

---

## 🔢 Schritt 6: Zeitstempel-IDs generieren

**Wie erstellt man eine gültige ID?**

Format: `YYYYMMDDHHmmSS`

**Beispiel:** Heute ist 27. Oktober 2025, 15:30:45 Uhr
- Jahr: 2025
- Monat: 10
- Tag: 27
- Stunde: 15
- Minute: 30
- Sekunde: 45
- → ID: `20251027153045`

**Trick für die Sekunden:**
- Meist reicht `00` für die Sekunden
- Nur wichtig wenn ihr mehrere Zettel pro Minute erstellt

**Aufgabe 6.1:** Eigene ID generieren

Schaut auf die Uhr und erstellt eine ID:
- Jetzt ist: ______ (Uhrzeit)
- ID wäre: ______________

---

## 🗂️ Schritt 7: Dateistruktur erkunden

**Aufgabe 7.1:** Alle Zettel-Dateien anschauen

1. Im `zettel` Ordner: Liste anschauen
2. Sortiert nach "Änderungsdatum"
3. Die neuesten Dateien = eure Zettel!
4. Ältere Dateien = Zettelstore System-Zettel

**System-Zettel:** IDs mit vielen Nullen
- `00000000000001` = Version-Zettel
- `00000000000100` = Start-Zettel
- `00010000000000` = Konfiguration
- Etc.

**Eure Zettel:** Realistische Zeitstempel
- `20251027123456` = euer Zettel von heute 12:34:56 Uhr

---

## 🎓 Was ihr gelernt habt

✅ **Zettel = Textdateien** (`.zettel` Endung)
✅ **Format:** Metadaten → Leerzeile → Inhalt
✅ **Speicherort:** `~/zettel/` Ordner
✅ **Dateiname:** Zettel-ID (Zeitstempel)
✅ **Bearbeitbar** mit jedem Texteditor
✅ **Manuell erstellbar** ohne Zettelstore

**Das große Bild:**
- Zettelstore = schöne Verpackung um Textdateien
- Ihr seid NICHT abhängig von Zettelstore
- Daten sind portable und langlebig

---

## 🧪 Übungsaufgabe (10 Min)

**Aufgabe:** Erstellt 3 Zettel, alle drei Methoden!

1. **Zettel A:** Über Web-UI (wie in Tutorial 02)
2. **Zettel B:** Web-UI erstellen, dann im Texteditor bearbeiten
3. **Zettel C:** Komplett manuell als Textdatei erstellen

**Testet:**
- Sind alle 3 Zettel in der Web-UI sichtbar?
- Könnt ihr alle 3 als Textdateien öffnen?
- Versteht ihr den Zusammenhang?

---

## ✅ Checkpoint: Bist du bereit?

- [ ] Habe ich den `zettel` Ordner gefunden?
- [ ] Habe ich eine `.zettel` Datei im Texteditor geöffnet?
- [ ] Verstehe ich das Format (Metadaten + Leerzeile + Inhalt)?
- [ ] Habe ich einen Zettel manuell bearbeitet?
- [ ] Habe ich einen Zettel manuell erstellt?
- [ ] Habe ich die Übungsaufgabe gemacht?

**Alle ✅?** Weiter zu Tutorial 04!

---

## 💡 Pro-Tipp

**Backups sind super einfach:**

1. Zettelstore stoppen
2. `zettel` Ordner kopieren → `zettel_backup_2025-10-27`
3. Fertig!

**Versionskontrolle mit Git:**

Ihr könnt den `zettel` Ordner auch unter Git stellen!
```bash
cd ~/zettel
git init
git add .
git commit -m "Backup"
```

Dann habt ihr History von allen Änderungen!

---

## 🆘 Troubleshooting

### Problem: "Manuell erstellter Zettel erscheint nicht"

**Lösung:**
- Dateiname korrekt? (14 Ziffern + `.zettel`)
- Gespeichert im richtigen `zettel` Ordner?
- Zettelstore neu starten (Strg+C, dann wieder starten)
- Web-UI neu laden (F5)

### Problem: "Datei hat falsche Endung"

**Lösung:**
- Windows versteckt Endungen standardmäßig!
- Explorer → Ansicht → "Dateinamenerweiterungen" anhaken
- Datei umbenennen: `.txt` entfernen, `.zettel` hinzufügen

### Problem: "Leerzeile fehlt"

**Lösung:**
- Nach Metadaten: ENTER drücken (eine Leerzeile einfügen)
- Dann erst Inhalt

---

## ➡️ Nächster Schritt

**Tutorial 04: Was ist eine REST API?**

Jetzt wisst ihr wie Zettelstore intern funktioniert. Als nächstes lernt ihr wie man programmatisch (mit Code) auf Zettel zugreift - über die API!

Das ist der Sprung von "Zettelstore benutzen" zu "Software für Zettelstore entwickeln"!
