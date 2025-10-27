# Tutorial 04: Was ist eine REST API?

**Zeit:** 20 Minuten
**Schwierigkeit:** 🔵 Mittel
**Voraussetzung:** Tutorial 01-03 abgeschlossen

---

## 🎯 Ziel

Am Ende dieses Tutorials:
- ✅ Versteht ihr was eine API ist (einfache Erklärung!)
- ✅ Versteht ihr was REST bedeutet
- ✅ Kennt ihr HTTP-Grundlagen (GET, POST, etc.)
- ✅ Versteht ihr JSON-Format
- ✅ Wisst ihr warum APIs wichtig sind

---

## 🤔 Was ist eigentlich eine API?

### Analogie: Restaurant

Stellt euch ein Restaurant vor:

1. **Ihr (Kunde)** sitzt am Tisch
2. **Kellner** kommt und nimmt eure Bestellung auf
3. **Küche** bereitet das Essen zu
4. **Kellner** bringt euch das Essen

**In dieser Analogie:**
- **Ihr = eure Software** (z.B. ZettelWeb)
- **Kellner = API** (Schnittstelle)
- **Küche = Zettelstore** (Server/Dienst)

Die API ist der "Kellner" zwischen euch und dem System!

### Warum braucht man eine API?

**Ohne API:**
- Ihr müsstet direkt in die "Küche" (Zettelstore-Code) eingreifen
- Ihr müsstet wissen wie jedes Detail funktioniert
- Sehr kompliziert!

**Mit API:**
- Ihr "bestellt" nur was ihr wollt: "Gib mir alle Zettel mit Tag 'test'"
- Zettelstore kümmert sich um die Details
- Einfach!

---

## 🌐 Was bedeutet REST?

**REST** = **RE**presentational **S**tate **T**ransfer

Klingt kompliziert, ist aber ein einfaches Konzept:

### REST Prinzipien (vereinfacht):

1. **Ressourcen** = Dinge die man abrufen kann
   - Beispiel: Zettel, Liste von Zetteln, Tags

2. **URLs** = Adressen von Ressourcen
   - Beispiel: `/z/20251027123456` = Ein spezifischer Zettel

3. **HTTP-Methoden** = Was man mit Ressourcen machen will
   - `GET` = Holen
   - `POST` = Erstellen
   - `PUT` = Ändern
   - `DELETE` = Löschen

4. **Zustandslos** = Jede Anfrage ist unabhängig
   - Server merkt sich nichts zwischen Anfragen

### Beispiel:

```
GET /z/20251027123456
```

Bedeutet: "Gib mir den Zettel mit ID 20251027123456"

---

## 📡 HTTP-Grundlagen

**HTTP** = HyperText Transfer Protocol

Das ist die "Sprache" des Internets.

### HTTP-Methoden (Verben):

| Methode | Bedeutung | Restaurant-Analogie |
|---------|-----------|---------------------|
| **GET** | Daten abrufen | "Zeig mir die Speisekarte" |
| **POST** | Neu erstellen | "Ich bestelle ein Schnitzel" |
| **PUT** | Ändern | "Änder meine Bestellung zu Pasta" |
| **DELETE** | Löschen | "Storniere meine Bestellung" |

**Für unser Projekt:**
- Wir brauchen hauptsächlich **GET** (Zettel abrufen)
- Später ggf. POST/PUT (Zettel erstellen/ändern)

### HTTP-Anfrage Aufbau:

```
GET /z/20251027123456 HTTP/1.1
Host: localhost:23123
Accept: application/json
```

**Bestandteile:**
- Zeile 1: **Methode** (GET) + **Pfad** (/z/...) + **Protokoll**
- Zeile 2+: **Header** (Zusatzinformationen)

### HTTP-Antwort Aufbau:

```
HTTP/1.1 200 OK
Content-Type: application/json

{"id": "20251027123456", "title": "Mein Zettel", ...}
```

**Bestandteile:**
- Zeile 1: **Status** (200 = OK)
- Zeile 2+: **Header**
- Leerzeile
- **Body** (die eigentlichen Daten)

---

## 📦 JSON-Format

**JSON** = JavaScript Object Notation

Das ist das "Austauschformat" für Daten.

### Warum JSON?

- **Menschenlesbar** (im Gegensatz zu Binärformaten)
- **Maschinenlesbar** (einfach zu parsen)
- **Standardisiert**
- **Kompakt**

### JSON-Syntax:

**Objekt** (geschweifte Klammern):
```json
{
  "name": "Max",
  "alter": 25,
  "student": true
}
```

**Array** (eckige Klammern):
```json
[
  "Apfel",
  "Banane",
  "Orange"
]
```

**Kombiniert:**
```json
{
  "person": {
    "name": "Max",
    "alter": 25
  },
  "hobbies": ["Lesen", "Programmieren"]
}
```

### JSON-Datentypen:

- **String:** `"Text in Anführungszeichen"`
- **Number:** `42` oder `3.14`
- **Boolean:** `true` oder `false`
- **Null:** `null`
- **Object:** `{...}`
- **Array:** `[...]`

---

## 🔍 Beispiel: Zettelstore API

Schauen wir uns an wie Zettelstore JSON zurückgibt.

### Beispiel-Anfrage:

```
GET /z/20251027123456
Accept: application/json
```

### Beispiel-Antwort:

```json
{
  "id": "20251027123456",
  "meta": {
    "title": "Mein erster Zettel",
    "tags": "test, tutorial",
    "syntax": "zmk",
    "role": "zettel"
  },
  "content": "Das ist mein erster eigener Zettel..."
}
```

**Was bedeutet das?**
- **id:** Die Zettel-ID
- **meta:** Objekt mit Metadaten
  - **title:** Titel des Zettels
  - **tags:** Tags als String
  - **syntax:** Formatierung
  - **role:** Typ des Zettels
- **content:** Der Inhalt

---

## 🌐 APIs im Browser testen

**Wichtige Erkenntnis:** Euer Browser ist ein API-Client!

Wenn ihr eine URL aufruft, macht der Browser eine HTTP-Anfrage.

### Aufgabe: API im Browser testen

1. **Zettelstore starten**
2. **Browser öffnen**
3. **Diese URL eingeben:**

```
http://localhost:23123/z?q=
```

**Was passiert:**
- Der Browser macht einen `GET` Request
- Zettelstore antwortet mit JSON
- Browser zeigt das JSON an

**Was ihr seht:**
```json
{
  "list": [
    {
      "id": "20251027123456",
      "url": "/z/20251027123456",
      "meta": {
        "title": "Mein erster Zettel",
        ...
      }
    },
    ...
  ]
}
```

📸 **Checkpoint:** Seht ihr JSON im Browser? JA → weiter!

---

## 🔗 URL-Struktur verstehen

Zettelstore API URLs folgen einem Muster:

### Basis-URL:
```
http://localhost:23123
```

### Endpunkte (Endpoints):

| URL | Was macht das? |
|-----|----------------|
| `/z` | Liste aller Zettel |
| `/z/{id}` | Ein spezifischer Zettel |
| `/z?q=tag:test` | Zettel mit Tag "test" |
| `/z?q=` | Alle Zettel (leere Abfrage) |

### Query-Parameter:

Format: `?parameter=wert&parameter2=wert2`

Beispiele:
- `?q=tag:test` → Abfrage (query): "tag ist test"
- `?limit=10` → Maximal 10 Ergebnisse
- `?q=test&limit=5` → Suche "test", max 5 Ergebnisse

---

## 🛠️ API-Testing Tools

### Tool 1: Browser

**Vorteile:**
- Sofort verfügbar
- Gut für GET-Requests

**Nachteile:**
- Nur GET möglich
- Kein schönes Format

### Tool 2: Browser Developer Tools

**Aufgabe:** Network-Tab erkunden

1. Browser: F12 drücken (Developer Tools öffnen)
2. Tab "Network" auswählen
3. URL aufrufen: `http://localhost:23123/z?q=`
4. Im Network-Tab: Seht ihr die Request!

Dort seht ihr:
- **Request Headers** (was wurde gesendet)
- **Response Headers** (was kam zurück)
- **Response Body** (die Daten)

### Tool 3: Postman/Insomnia (optional)

Professionelle Tools für API-Testing. Für später!

---

## 💻 APIs mit JavaScript aufrufen

Jetzt kommt der wichtige Teil: APIs mit Code aufrufen!

### Die `fetch()` Funktion

JavaScript hat eine eingebaute Funktion: `fetch()`

**Syntax:**
```javascript
fetch(url)
  .then(response => response.json())
  .then(data => console.log(data));
```

### Schritt-für-Schritt:

1. `fetch(url)` → Macht HTTP-Request
2. `.then(response => ...)` → Wenn Antwort kommt
3. `response.json()` → Konvertiert zu JavaScript-Objekt
4. `.then(data => ...)` → Wenn Konvertierung fertig
5. `console.log(data)` → Ausgabe in Console

### Moderne Syntax (async/await):

```javascript
async function loadZettel() {
  const response = await fetch('http://localhost:23123/z?q=');
  const data = await response.json();
  console.log(data);
}

loadZettel();
```

Einfacher zu lesen!

---

## 🎓 Was ihr gelernt habt

✅ **API = Schnittstelle** zwischen eurer Software und Zettelstore
✅ **REST = Architekturstil** für APIs (Ressourcen + HTTP-Methoden)
✅ **HTTP-Methoden:** GET, POST, PUT, DELETE
✅ **JSON = Datenformat** für APIs
✅ **Browser = API-Client** (kann GET-Requests machen)
✅ **fetch() = JavaScript** Funktion für API-Aufrufe

**Das große Bild:**
```
ZettelWeb (JavaScript)
    ↓ fetch()
HTTP GET Request
    ↓
Zettelstore API
    ↓
JSON Response
    ↓ response.json()
JavaScript Object
    ↓
Eure Anwendung kann damit arbeiten!
```

---

## 🧪 Übungsaufgabe (10 Min)

### Aufgabe 1: URLs verstehen

Was machen diese URLs?
1. `http://localhost:23123/z/00000000000001`
2. `http://localhost:23123/z?q=tag:test`
3. `http://localhost:23123/z?q=syntax:zmk`

Probiert sie im Browser aus!

### Aufgabe 2: JSON lesen

Öffnet: `http://localhost:23123/z?q=&limit=1`

Fragen:
- Wie viele Zettel werden zurückgegeben?
- Was steht im `meta` Objekt?
- Was ist die `id` des Zettels?

---

## ✅ Checkpoint: Bist du bereit?

- [ ] Verstehe ich was eine API ist?
- [ ] Kenne ich HTTP-Methoden (GET, POST, etc.)?
- [ ] Verstehe ich JSON-Format?
- [ ] Kann ich API im Browser testen?
- [ ] Verstehe ich wie `fetch()` funktioniert?
- [ ] Habe ich die Übungsaufgaben gemacht?

**Alle ✅?** Weiter zu Tutorial 05!

---

## 🆘 Troubleshooting

### Problem: "JSON nicht lesbar im Browser"

**Lösung:**
- Browser-Extension installieren: "JSON Formatter"
- Oder: F12 → Console → `copy(JSON.stringify(data, null, 2))`

### Problem: "404 Not Found"

**Lösung:**
- Ist Zettelstore gestartet?
- URL korrekt? (Tippfehler?)
- Existiert die Zettel-ID?

---

## ➡️ Nächster Schritt

**Tutorial 05: Zettelstore API testen**

Jetzt wo ihr die Theorie kennt, testen wir die Zettelstore API praktisch!
