# Tutorial 01: Zettelstore starten

**Zeit:** 15 Minuten
**Schwierigkeit:** 🟢 Sehr einfach
**Vorkenntnisse:** Keine!

---

## 🎯 Ziel

Am Ende dieses Tutorials:
- ✅ Wisst ihr was Zettelstore ist (praktisch, nicht theoretisch!)
- ✅ Habt Zettelstore gestartet
- ✅ Habt die Web-Oberfläche gesehen
- ✅ Habt durch vorhandene Zettel geklickt

---

## 📝 Was IST Zettelstore überhaupt?

**In einfachen Worten:**

Zettelstore ist wie eine persönliche Wikipedia, aber:
- Viel einfacher
- Für eure eigenen Notizen/Wissen
- Läuft auf eurem Computer (nicht im Internet)
- Speichert alles als einfache Textdateien

**Analogie:** Stellt euch vor:
- **Obsidian:** Kennt ihr schon - Notizen mit Verknüpfungen
- **Zettelstore:** Ähnlich, aber noch simpler + hat eine eingebaute API

---

## 🔧 Schritt 1: Zettelstore-Ordner finden

Ihr habt Zettelstore bereits heruntergeladen. Der liegt hier:

```
D:\CLI Projects\SWT\zettelstore\zettelstore-0.22.0-windows-amd64\
```

**Aufgabe 1.1:**
1. Windows Explorer öffnen
2. Zu diesem Ordner navigieren
3. Dort findet ihr: `zettelstore.exe`

📸 **Checkpoint:** Seht ihr die zettelstore.exe Datei? JA → weiter!

---

## 🚀 Schritt 2: Zettelstore zum ersten Mal starten

**Aufgabe 2.1:**
1. **Doppelklick** auf `zettelstore.exe`
2. Ein schwarzes Fenster (Konsole) öffnet sich
3. Ihr seht Text wie: `INFO: Web server listening on ... :23123`

**⚠️ WICHTIG:**
- Dieses Fenster NICHT schließen!
- Solange es offen ist, läuft Zettelstore
- Wenn ihr es schließt, stoppt Zettelstore

**Was passiert gerade?**
Zettelstore ist jetzt ein "Server" auf eurem Computer. Er wartet auf Anfragen.

📸 **Checkpoint:** Schwarzes Fenster offen? Steht da was von ":23123"? JA → weiter!

---

## 🌐 Schritt 3: Web-Oberfläche öffnen

Zettelstore hat eine Web-Oberfläche (läuft im Browser).

**Aufgabe 3.1:**
1. Browser öffnen (Chrome, Firefox, Edge - egal)
2. In die Adressleiste eingeben: `http://localhost:23123`
3. Enter drücken

**Was bedeutet das?**
- `localhost` = dein eigener Computer
- `23123` = Port-Nummer (wie eine Tür) auf der Zettelstore "lauscht"

**Was ihr jetzt sehen solltet:**
- Eine einfache Webseite
- Titel: "Home" oder ähnlich
- Eine Liste von Zetteln
- Menü mit "Home", "New", "Filters", etc.

📸 **Checkpoint:** Seht ihr eine Webseite mit Zetteln? JA → weiter!

---

## 👀 Schritt 4: Durch vorhandene Zettel klicken

Zettelstore kommt mit vorinstallierten Zetteln (zur Konfiguration und als Beispiele).

**Aufgabe 4.1:** Klickt euch durch mindestens 3 Zettel

1. Klickt auf irgendeinen Zettel-Titel in der Liste
2. Lest den Inhalt (muss nicht alles verstehen!)
3. Schaut euch die Metadaten oben an (Title, Tags, etc.)
4. Klickt auf "Back" oder auf einen anderen Link

**Aufgabe 4.2:** Findet den "Home" Zettel

1. Oben im Menü: "Home" klicken
2. Das ist der Startzettel

**Was ihr beobachten solltet:**
- Jeder Zettel hat eine **ID** (14 Zahlen, z.B. `00010000000000`)
- Jeder Zettel hat **Metadaten** (Title, Tags, Syntax, ...)
- Manche Zettel haben **Links** zu anderen Zetteln
- Wenn ihr auf einen Link klickt, kommt ihr zu einem anderen Zettel

📸 **Checkpoint:** Habt ihr durch 3+ Zettel geklickt? JA → weiter!

---

## 🔍 Schritt 5: Die Oberfläche verstehen

Lasst uns die Web-Oberfläche kurz erklären:

**Menü (oben):**
- **Home:** Zurück zum Startzettel
- **New:** Neuen Zettel erstellen (machen wir im nächsten Tutorial!)
- **Filters:** Zettel nach Kriterien filtern
- **Refresh:** Seite neu laden

**Zettel-Ansicht:**
- **Oben:** Metadaten (Title, Tags, etc.)
- **Mitte:** Inhalt des Zettels
- **Unten:** Links zu anderen Zetteln (falls vorhanden)

**Aufgabe 5.1:** Probiert die Filter-Funktion

1. Klickt auf "Filters" im Menü
2. Ihr seht verschiedene Filter-Optionen
3. Klickt z.B. auf "Tags" → seht welche Tags existieren
4. Klickt auf einen Tag → zeigt alle Zettel mit diesem Tag

---

## 🎓 Was ihr gelernt habt

✅ **Zettelstore ist ein lokaler Server** (läuft auf eurem PC)
✅ **Web-Oberfläche im Browser** (http://localhost:23123)
✅ **Zettel haben IDs und Metadaten**
✅ **Zettel können verknüpft sein**
✅ **Filter und Navigation funktionieren**

---

## 🧪 Mini-Experiment (5 Min)

Bevor wir zum nächsten Tutorial gehen, probiert das aus:

**Experiment 1:** Zettelstore stoppen und wieder starten

1. Geht zum schwarzen Konsolen-Fenster
2. Drückt `Strg + C` (stoppt Zettelstore)
3. Geht zum Browser → seht ihr noch die Seite? Klickt auf "Home"
4. ❌ Fehlermeldung! (Weil Zettelstore nicht mehr läuft)
5. Startet zettelstore.exe wieder
6. Browser → Seite neu laden (F5)
7. ✅ Funktioniert wieder!

**Was ihr gelernt habt:** Zettelstore muss laufen, damit die Web-Oberfläche funktioniert.

---

## ✅ Checkpoint: Bist du bereit?

Beantworte diese Fragen (ehrlich!):

- [ ] Kann ich Zettelstore starten?
- [ ] Kann ich die Web-Oberfläche öffnen?
- [ ] Habe ich durch mindestens 3 Zettel geklickt?
- [ ] Verstehe ich was Metadaten sind?
- [ ] Habe ich das Mini-Experiment gemacht?

**Alle ✅?** Dann weiter zu Tutorial 02!

**Noch ❌?** Mach dieses Tutorial nochmal von vorne.

---

## 🆘 Troubleshooting

### Problem 1: "Kann Seite nicht aufrufen"

**Lösung:**
- Ist zettelstore.exe gestartet? (Schwarzes Fenster offen?)
- Steht in der URL `http://localhost:23123` (NICHT https!)
- Firewall blockiert? (Windows Firewall Warnung → "Zugriff zulassen" klicken)

### Problem 2: "Port already in use"

**Lösung:**
- Zettelstore läuft schon! Sucht nach offenen zettelstore.exe Fenstern
- Oder: Anderes Programm nutzt Port 23123 (selten)

### Problem 3: "Keine Zettel sichtbar"

**Lösung:**
- Beim allerersten Start hat Zettelstore schon Default-Zettel
- Seite neu laden (F5)
- Zettelstore neu starten

---

## ➡️ Nächster Schritt

**Tutorial 02: Zettel erstellen und verknüpfen**

Jetzt wo ihr wisst wie Zettelstore aussieht, lernt ihr eigene Zettel zu erstellen!
