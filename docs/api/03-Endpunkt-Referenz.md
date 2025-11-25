# Zettelstore API - Vollständige Endpunkt-Referenz

Diese Referenz dokumentiert alle verfügbaren API-Endpunkte mit Methoden, Parametern, Beispielen und Responses.

---

## 🔐 Authentifizierung (`/a`)

### POST /a - Benutzer Authentifizieren

**Beschreibung:** Authentifizierung eines Benutzers und Erhalt eines Access-Tokens.

**Handler:** `internal/web/adapter/api/login.go::MakePostLoginHandler`

**Authentifizierung:** Keine (Credentials in Request)

#### Request

**Methoden für Credentials:**

1. **HTTP Basic Auth** (empfohlen):
```bash
curl -X POST -u USERNAME:PASSWORD http://127.0.0.1:23123/a
```

2. **URL-embedded**:
```bash
curl -X POST http://USERNAME:PASSWORD@127.0.0.1:23123/a
```

3. **Form-Daten**:
```bash
curl -X POST -d 'username=USERNAME&password=PASSWORD' http://127.0.0.1:23123/a
```

#### Response

**Erfolg (200 OK):**
```lisp
("Bearer" "eyJhbGciOiJIUzUxMiJ9..." 600)
```

**Elemente:**
- `"Bearer"` - Auth-Schema
- `"eyJ..."` - JWT Access-Token
- `600` - Token-Lebensdauer in Sekunden

**Fehler:**
- `400 Bad Request` - Ungültige Anfrage
- `401 Unauthorized` - Falsche Credentials
- `403 Forbidden` - Authentifizierung nicht aktiviert

#### Beispiel

```bash
# Token erhalten und extrahieren
TOKEN=$(curl -s -X POST -u owner:owner http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

echo "Erhaltener Token: $TOKEN"
```

---

### PUT /a - Token Erneuern

**Beschreibung:** Erneuert ein bestehendes Access-Token.

**Handler:** `internal/web/adapter/api/login.go::MakeRenewAuthHandler`

**Authentifizierung:** Erforderlich (Bearer Token)

#### Request

```bash
curl -X PUT \
  -H "Authorization: Bearer {token}" \
  http://127.0.0.1:23123/a
```

#### Verhalten

- **Erstes Viertel der Lebensdauer:** Gibt bestehendes Token zurück
- **Danach:** Generiert neues Token mit voller Lebensdauer

#### Response

**Erfolg (200 OK):**
```lisp
("Bearer" "eyJhbGciOiJIUzUxMiJ9..." 600)
```

**Fehler:**
- `401 Unauthorized` - Token ungültig oder abgelaufen

#### Beispiel

```bash
# Token erneuern
NEW_TOKEN=$(curl -s -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

echo "Neuer Token: $NEW_TOKEN"
```

---

## 📝 Zettel-Operationen (`/z`)

### GET /z - Alle Zettel Auflisten/Abfragen

**Beschreibung:** Liste oder Abfrage aller Zettel mit optionalen Filtern.

**Handler:** `internal/web/adapter/api/query.go::MakeQueryHandler`

**Authentifizierung:** Abhängig von der Konfiguration

#### Query-Parameter

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `enc` | string | Encoding-Format (plain, data, html, ...) |
| `part` | string | Teil auswählen (zettel, meta, content) |
| `{query}` | string | Query-String für Filterung |

#### Query-Syntax

**Grundlegende Operatoren:**
- `key HAS value` - Enthält-Suche
- `key:value` - Exakte Übereinstimmung
- `ORDER key` - Sortierung
- `REVERSE` - Umgekehrte Sortierung
- `LIMIT n` - Ergebnis begrenzen
- `OFFSET n` - Ergebnis-Offset

**Spezial-Parameter:**
- `?_tag=tagname` - Zettel mit bestimmtem Tag
- `?_role=rolename` - Zettel mit bestimmter Rolle

#### Request

```bash
# Alle Zettel
curl http://127.0.0.1:23123/z

# Mit Authentifizierung
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:23123/z

# Mit Query
curl 'http://127.0.0.1:23123/z?tags HAS api'

# Mit Sortierung und Limit
curl 'http://127.0.0.1:23123/z?role:zettel ORDER REVERSE created LIMIT 10'

# Data-Format
curl 'http://127.0.0.1:23123/z?enc=data'

# Nur Metadaten
curl 'http://127.0.0.1:23123/z?part=meta'

# Tag-basiert
curl 'http://127.0.0.1:23123/z?_tag=wichtig'

# Rolle-basiert
curl 'http://127.0.0.1:23123/z?_role=configuration'
```

#### Response

**Plain-Format (Standard):**
```
20210903211500 Mein Erstes Zettel
20210903211501 Zweites Zettel
20210903211502 Drittes Zettel
```

**Data-Format:**
```lisp
(meta-list
  (query "tags HAS api")
  (human "Zettel mit Tag 'api'")
  (zettel
    (id "20210903211500")
    (meta
      (title "API Test")
      (tags "#api #test"))
    (rights 15))
  (zettel
    (id "20210903211501")
    (meta
      (title "Zweiter Test")
      (tags "#api"))
    (rights 15)))
```

**Status-Codes:**
- `200 OK` - Erfolg
- `400 Bad Request` - Ungültige Query
- `401 Unauthorized` - Authentifizierung fehlt/ungültig

#### Implementierungsdetails

**Query-Implementierung:** `internal/query/`
- Parser: `parser.go`
- Compiled Query: `compiled.go`
- Context: `context.go`

#### Beispiele

```bash
# Alle Zettel mit Tag "projekt"
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z?tags HAS projekt'

# Neueste 5 Zettel
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z?ORDER REVERSE created LIMIT 5'

# Konfiguration-Zettel
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z?role:configuration'

# Komplexe Query
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z?tags HAS api role:zettel ORDER title LIMIT 20'
```

---

### POST /z - Neues Zettel Erstellen

**Beschreibung:** Erstellt ein neues Zettel.

**Handler:** `internal/web/adapter/api/create_zettel.go::MakePostCreateZettelHandler`

**Authentifizierung:** Erforderlich

#### Request

**Headers:**
- `Authorization: Bearer {token}` (erforderlich)
- `Content-Type: text/plain` oder `application/x-sxpf`

**Body - Plain-Format:**
```
title: Mein Neues Zettel
tags: #beispiel #neu
role: zettel
syntax: zmk

Dies ist der Inhalt des Zettels.
Er kann mehrere Zeilen umfassen.
```

**Body - Data-Format:**
```lisp
((meta
  (title "Mein Neues Zettel")
  (tags "#beispiel #neu")
  (role "zettel"))
 (content "Dies ist der Inhalt."))
```

#### Response

**Erfolg (201 Created):**
```
20210903211500
```

**Headers:**
```
HTTP/1.1 201 Created
Location: /z/20210903211500
Content-Type: text/plain

20210903211500
```

**Fehler:**
- `400 Bad Request` - Ungültiges Format
- `401 Unauthorized` - Authentifizierung fehlt
- `403 Forbidden` - Keine Berechtigung zum Erstellen

#### Beispiele

**Plain-Format:**
```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: API Test Zettel\ntags: #api #test\n\nDies ist ein Test-Zettel.' \
  http://127.0.0.1:23123/z
```

**Data-Format:**
```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/x-sxpf" \
  --data '((meta (title "API Test")) (content "Test-Inhalt"))' \
  'http://127.0.0.1:23123/z?enc=data'
```

**Mit Variable:**
```bash
NEW_ZID=$(curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Neues Zettel\n\nInhalt' \
  http://127.0.0.1:23123/z)

echo "Erstellt: $NEW_ZID"
```

---

### GET /z/{id} - Zettel Abrufen

**Beschreibung:** Ruft ein spezifisches Zettel ab.

**Handler:** `internal/web/adapter/api/get_zettel.go::MakeGetZettelHandler`

**Authentifizierung:** Abhängig von Zettel-Visibility

#### URL-Parameter

- `{id}` - 14-stellige Zettel-ID (z.B. `20210903211500`)

#### Query-Parameter

| Parameter | Werte | Beschreibung |
|-----------|-------|--------------|
| `enc` | plain, data, html, zmk, md, text | Encoding-Format |
| `part` | zettel, meta, content | Zettel-Teil |
| `_parseonly` | - | Nur parsen, nicht evaluieren |

#### Request

```bash
# Standard (plain)
curl http://127.0.0.1:23123/z/20210903211500

# Mit Authentifizierung
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/20210903211500

# Data-Format
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?enc=data'

# Nur Metadaten
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?part=meta'

# Nur Inhalt
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?part=content'

# HTML-Format
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?enc=html'

# Markdown-Format
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?enc=md'
```

#### Response

**Plain-Format:**
```
title: Mein Zettel
role: zettel
tags: #beispiel
created: 20210903211500
modified: 20210903211600

Dies ist der Inhalt des Zettels.
Mit mehreren Zeilen.
```

**Data-Format:**
```lisp
(zettel
  (id "20210903211500")
  (meta
    (title "Mein Zettel")
    (role "zettel")
    (tags "#beispiel")
    (created "20210903211500"))
  (rights 15)
  (encoding "zmk")
  (content "Dies ist der Inhalt des Zettels.\nMit mehreren Zeilen."))
```

**Status-Codes:**
- `200 OK` - Erfolg
- `401 Unauthorized` - Authentifizierung fehlt/ungültig
- `403 Forbidden` - Keine Leseberechtigung
- `404 Not Found` - Zettel existiert nicht

#### Beispiele

```bash
# Komplettes Zettel
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/20210903211500

# Nur Titel und Tags (Metadaten)
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?part=meta&enc=data'

# Als HTML rendern
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?enc=html' > zettel.html
```

---

### PUT /z/{id} - Zettel Aktualisieren

**Beschreibung:** Aktualisiert ein bestehendes Zettel.

**Handler:** `internal/web/adapter/api/update_zettel.go::MakeUpdateZettelHandler`

**Authentifizierung:** Erforderlich

#### URL-Parameter

- `{id}` - 14-stellige Zettel-ID

#### Request

**Headers:**
- `Authorization: Bearer {token}` (erforderlich)
- `Content-Type: text/plain` oder `application/x-sxpf`

**Body - Plain-Format:**
```
title: Aktualisierter Titel
tags: #aktualisiert #neu
role: zettel

Neuer aktualisierter Inhalt.
```

**Body - Data-Format:**
```lisp
((meta
  (title "Aktualisierter Titel")
  (tags "#aktualisiert"))
 (content "Neuer Inhalt"))
```

#### Response

**Erfolg (204 No Content):**
```
HTTP/1.1 204 No Content
```

Kein Response-Body.

**Fehler:**
- `400 Bad Request` - Ungültiges Format
- `401 Unauthorized` - Authentifizierung fehlt
- `403 Forbidden` - Keine Schreibberechtigung
- `404 Not Found` - Zettel existiert nicht

#### Beispiele

```bash
# Zettel aktualisieren
curl -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Neuer Titel\ntags: #updated\n\nAktualisierter Inhalt' \
  http://127.0.0.1:23123/z/20210903211500

# Status prüfen
if [ $? -eq 0 ]; then
  echo "Zettel erfolgreich aktualisiert"
fi

# Nur Metadaten aktualisieren
curl -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Nur Titel geändert\ntags: #meta' \
  'http://127.0.0.1:23123/z/20210903211500?part=meta'
```

**Wichtig:** Beim Update werden **alle** Metadaten ersetzt. Fehlende Keys werden entfernt. Um nur bestimmte Felder zu ändern, zuerst das Zettel abrufen, ändern und dann zurücksenden.

---

### DELETE /z/{id} - Zettel Löschen

**Beschreibung:** Löscht ein Zettel permanent.

**Handler:** `internal/web/adapter/api/delete_zettel.go::MakeDeleteZettelHandler`

**Authentifizierung:** Erforderlich

#### URL-Parameter

- `{id}` - 14-stellige Zettel-ID

#### Request

```bash
curl -X DELETE \
  -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/20210903211500
```

#### Response

**Erfolg (204 No Content):**
```
HTTP/1.1 204 No Content
```

Kein Response-Body.

**Fehler:**
- `401 Unauthorized` - Authentifizierung fehlt
- `403 Forbidden` - Keine Löschberechtigung
- `404 Not Found` - Zettel existiert nicht

#### Beispiel

```bash
# Zettel löschen
curl -X DELETE \
  -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/20210903211500

# Mit Fehlerbehandlung
if curl -s -X DELETE \
  -H "Authorization: Bearer $TOKEN" \
  -o /dev/null -w "%{http_code}" \
  http://127.0.0.1:23123/z/20210903211500 | grep -q "204"; then
  echo "Zettel gelöscht"
else
  echo "Fehler beim Löschen"
fi
```

**Warnung:** Löschvorgang ist permanent und kann nicht rückgängig gemacht werden (außer durch Backup-Wiederherstellung).

---

## 🔗 Referenzen (`/r`)

### GET /r/{id} - Zettel-Referenzen Abrufen

**Beschreibung:** Ruft alle Referenzen (Links) für ein spezifisches Zettel ab.

**Handler:** `internal/web/adapter/api/get_references.go::MakeGetReferencesHandler`

**Authentifizierung:** Abhängig von Zettel-Visibility

#### URL-Parameter

- `{id}` - 14-stellige Zettel-ID

#### Query-Parameter

| Parameter | Werte | Beschreibung |
|-----------|-------|--------------|
| `enc` | plain, data, html | Encoding-Format |
| `part` | zettel, meta, content | Teil, dessen Referenzen abgerufen werden |

#### Request

```bash
# Alle Referenzen
curl http://127.0.0.1:23123/r/20210903211500

# Mit Authentifizierung
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/r/20210903211500

# Nur Content-Referenzen
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/r/20210903211500?part=content'

# Data-Format
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/r/20210903211500?enc=data'
```

#### Response

**Plain-Format:**
```
20210903211501
20210903211502
https://example.com
00001012000000
```

**Data-Format:**
```lisp
(reference-list
  (zettel-id "20210903211501")
  (zettel-id "20210903211502")
  (url "https://example.com")
  (zettel-id "00001012000000"))
```

**Status-Codes:**
- `200 OK` - Erfolg
- `401 Unauthorized` - Authentifizierung fehlt/ungültig
- `403 Forbidden` - Keine Leseberechtigung
- `404 Not Found` - Zettel existiert nicht

#### Arten von Referenzen

1. **Zettel-Links:** Verweise auf andere Zettel (14-stellige IDs)
2. **URLs:** Externe Links
3. **Metadaten-Referenzen:** Links in Metadaten-Feldern

#### Beispiel

```bash
# Referenzen abrufen und verarbeiten
curl -s -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/r/20210903211500 | \
while read ref; do
  echo "Referenz gefunden: $ref"
  # Prüfe ob es eine Zettel-ID ist
  if [[ $ref =~ ^[0-9]{14}$ ]]; then
    echo "  -> Verweist auf Zettel $ref"
  fi
done
```

---

## ⚙️ Administrative Endpunkte (`/x`)

### GET /x - Versions- und System-Informationen

**Beschreibung:** Ruft Versionsinformationen und System-Daten ab.

**Handler:** `internal/web/adapter/api/get_data.go::MakeGetDataHandler`

**Authentifizierung:** Keine

#### Request

```bash
curl http://127.0.0.1:23123/x
```

#### Response

**Format (S-Expression):**
```lisp
(0 19 0 "dev" "abc123...")
```

**Elemente:**
1. Major-Version (z.B. `0`)
2. Minor-Version (z.B. `19`)
3. Patch-Version (z.B. `0`)
4. Build-Info (z.B. `"dev"`, `"stable"`)
5. Git-Hash (z.B. `"abc123..."`)

**Beispiel-Response:**
```lisp
(0 19 0 "dev" "a3f2c1b9")
```
Bedeutet: Version 0.19.0-dev, Git-Hash a3f2c1b9

#### Beispiele

```bash
# Version abrufen
curl http://127.0.0.1:23123/x

# Version parsen (Bash)
VERSION=$(curl -s http://127.0.0.1:23123/x)
echo "Zettelstore-Version: $VERSION"

# In Python
import requests
import re

response = requests.get('http://127.0.0.1:23123/x')
match = re.match(r'\((\d+) (\d+) (\d+) "([^"]+)" "([^"]+)"\)', response.text)
if match:
    major, minor, patch, info, hash = match.groups()
    print(f"Version: {major}.{minor}.{patch}-{info}")
    print(f"Git-Hash: {hash}")
```

---

### POST /x - Befehle Ausführen

**Beschreibung:** Führt administrative Befehle aus.

**Handler:** `internal/web/adapter/api/command.go::MakePostCommandHandler`

**Authentifizierung:** Abhängig vom Befehl

#### Query-Parameter

| Parameter | Werte | Beschreibung |
|-----------|-------|--------------|
| `_command` | authenticated, refresh | Auszuführender Befehl |

---

#### Befehl: authenticated

**Beschreibung:** Prüft Authentifizierungs-Status.

**Request:**
```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/x?_command=authenticated'
```

**Response-Codes:**
- `200 OK` - Authentifizierung ist deaktiviert
- `204 No Content` - Token ist gültig
- `401 Unauthorized` - Token ist ungültig/fehlt

**Verwendung:**
```bash
# Token-Gültigkeit prüfen
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  -X POST \
  -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/x?_command=authenticated')

if [ "$HTTP_CODE" -eq 204 ]; then
  echo "Token ist gültig"
elif [ "$HTTP_CODE" -eq 200 ]; then
  echo "Authentifizierung ist deaktiviert"
else
  echo "Token ist ungültig"
fi
```

---

#### Befehl: refresh

**Beschreibung:** Aktualisiert den internen Zettel-Index.

**Authentifizierung:** Erforderlich

**Request:**
```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/x?_command=refresh'
```

**Response:**
- `204 No Content` - Index wurde aktualisiert
- `401 Unauthorized` - Authentifizierung fehlt/ungültig
- `403 Forbidden` - Keine Berechtigung

**Verwendung:**
```bash
# Index nach externen Änderungen aktualisieren
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/x?_command=refresh'

echo "Index wurde aktualisiert"
```

**Wann verwenden:**
- Nach direkten Dateisystem-Änderungen
- Nach Backup-Wiederherstellung
- Bei Inkonsistenzen im Index

---

## 📊 Response-Formate im Detail

### Plain-Format

**MIME-Type:** `text/plain`

**Struktur:**
```
key1: value1
key2: value2
key3: value3

Content starts here
after blank line.
```

**Charakteristika:**
- Einfach zu lesen/schreiben
- Ein Metadaten-Key pro Zeile
- Leerzeile trennt Metadaten von Inhalt
- Standard-Format

**Verwendung:**
```bash
curl http://127.0.0.1:23123/z/20210903211500
```

---

### Data-Format (S-Expressions)

**MIME-Type:** `application/x-sxpf`

**Struktur:**
```lisp
(zettel
  (id "20210903211500")
  (meta
    (key1 "value1")
    (key2 "value2"))
  (rights 15)
  (encoding "zmk")
  (content "Content here"))
```

**Charakteristika:**
- Strukturiert und maschinenlesbar
- Enthält Rechte-Informationen
- Einfach zu parsen
- Bevorzugt für programmatischen Zugriff

**Verwendung:**
```bash
curl 'http://127.0.0.1:23123/z/20210903211500?enc=data'
```

**Parsing in Python:**
```python
import re

def parse_sexp_zettel(response):
    # Sehr vereinfachter Parser
    id_match = re.search(r'\(id "([^"]+)"\)', response)
    title_match = re.search(r'\(title "([^"]+)"\)', response)
    content_match = re.search(r'\(content "([^"]+)"\)', response)
    rights_match = re.search(r'\(rights (\d+)\)', response)

    return {
        'id': id_match.group(1) if id_match else None,
        'title': title_match.group(1) if title_match else None,
        'content': content_match.group(1) if content_match else None,
        'rights': int(rights_match.group(1)) if rights_match else 0
    }
```

---

### HTML-Format

**MIME-Type:** `text/html`

**Verwendung:**
```bash
curl 'http://127.0.0.1:23123/z/20210903211500?enc=html'
```

**Ausgabe:** Vollständig gerendertes HTML des Zettel-Inhalts.

**Verwendungszweck:**
- Anzeige in Web-Anwendungen
- HTML-Export
- Vorschau-Generierung

---

### Markdown-Format

**MIME-Type:** `text/markdown`

**Verwendung:**
```bash
curl 'http://127.0.0.1:23123/z/20210903211500?enc=md'
```

**Ausgabe:** Zettel-Inhalt konvertiert nach Markdown.

**Verwendungszweck:**
- Export für Markdown-Tools
- Kompatibilität mit anderen Systemen
- Konvertierung

---

## 🔍 Erweiterte Query-Beispiele

### Komplexe Suchen

```bash
# Zettel mit mehreren Tags
curl 'http://127.0.0.1:23123/z?tags HAS projekt tags HAS wichtig'

# Zettel mit bestimmtem Titel-Muster
curl 'http://127.0.0.1:23123/z?title HAS API'

# Nach Erstellungsdatum gefiltert
curl 'http://127.0.0.1:23123/z?created > 20210901000000'

# Kombination mit Sortierung
curl 'http://127.0.0.1:23123/z?role:zettel tags HAS api ORDER REVERSE modified LIMIT 10'
```

### Aggregationen

```bash
# Alle verwendeten Tags auflisten
curl 'http://127.0.0.1:23123/z?KEYS tags'

# Minimum und Maximum
curl 'http://127.0.0.1:23123/z?MIN created'
curl 'http://127.0.0.1:23123/z?MAX modified'
```

### Paginierung

```bash
# Erste 20 Zettel
curl 'http://127.0.0.1:23123/z?LIMIT 20'

# Nächste 20 Zettel
curl 'http://127.0.0.1:23123/z?LIMIT 20 OFFSET 20'

# Dritte Seite (Zettel 41-60)
curl 'http://127.0.0.1:23123/z?LIMIT 20 OFFSET 40'
```

---

## 🛠️ Fehlerbehandlung

### Allgemeine Fehler-Response

**Format:**
```
HTTP/1.1 {status-code} {status-text}
Content-Type: text/plain

{error-message}
```

**Beispiel:**
```
HTTP/1.1 404 Not Found
Content-Type: text/plain

Zettel not found: 99999999999999
```

### Fehlercode-Tabelle

| Code | Name | Typische Ursachen | Lösungen |
|------|------|-------------------|----------|
| 400 | Bad Request | Ungültiges Format, falsche Syntax | Request-Format prüfen |
| 401 | Unauthorized | Token fehlt/ungültig/abgelaufen | Neu authentifizieren |
| 403 | Forbidden | Keine Berechtigung | Rechte prüfen, anderen User verwenden |
| 404 | Not Found | Zettel existiert nicht | Zettel-ID validieren |
| 500 | Internal Server Error | Server-Problem | Server-Logs prüfen |

### Best Practices

```python
import requests

def safe_api_call(url, token, method='GET', data=None):
    headers = {'Authorization': f'Bearer {token}'}

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=data)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=data)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)

        # Spezifische Fehlerbehandlung
        if response.status_code == 401:
            raise AuthenticationError("Token abgelaufen oder ungültig")
        elif response.status_code == 403:
            raise PermissionError("Keine Berechtigung für diese Aktion")
        elif response.status_code == 404:
            raise NotFoundError("Ressource nicht gefunden")
        elif response.status_code >= 500:
            raise ServerError(f"Server-Fehler: {response.status_code}")

        response.raise_for_status()
        return response

    except requests.RequestException as e:
        print(f"Netzwerk-Fehler: {e}")
        raise
```

---

## 📚 Zusammenfassung aller Endpunkte

| Endpunkt | Methode | Beschreibung | Auth | Response |
|----------|---------|--------------|------|----------|
| `/a` | POST | Authentifizieren | Nein | Token |
| `/a` | PUT | Token erneuern | Ja | Token |
| `/z` | GET | Zettel auflisten/abfragen | Optional | Liste |
| `/z` | POST | Zettel erstellen | Ja | Zettel-ID |
| `/z/{id}` | GET | Zettel abrufen | Optional | Zettel |
| `/z/{id}` | PUT | Zettel aktualisieren | Ja | No Content |
| `/z/{id}` | DELETE | Zettel löschen | Ja | No Content |
| `/r/{id}` | GET | Referenzen abrufen | Optional | Liste |
| `/x` | GET | Versions-Info | Nein | Version |
| `/x?_command=authenticated` | POST | Auth prüfen | Ja | Status |
| `/x?_command=refresh` | POST | Index aktualisieren | Ja | No Content |

---

## 🔗 Weiterführende Dokumentation

- [01-API-Uebersicht.md](01-API-Uebersicht.md) - Grundlegende Konzepte
- [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md) - Security Details
- [04-Code-Beispiele.md](04-Code-Beispiele.md) - Praktische Implementierungen

---

**Version:** 1.0
**Letzte Aktualisierung:** 2025-11-12
**Basierend auf:** Zettelstore Version 0.19.0-dev
