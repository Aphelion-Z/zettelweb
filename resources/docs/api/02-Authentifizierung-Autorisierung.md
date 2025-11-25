# Zettelstore API - Authentifizierung & Autorisierung

## Übersicht

Die Zettelstore API verwendet **JWT (JSON Web Tokens)** mit dem **HS512-Algorithmus** für Authentifizierung und Autorisierung. Das System bietet granulare Zugriffskontrollen auf Zettel-Ebene.

## Authentifizierungs-Mechanismus

### Token-Typ: JWT (HS512)

**Implementierung:** `internal/auth/impl/digest.go`

**Token-Struktur:**
```json
{
  "_tk": 1,
  "exp": 1681304062,        // Expiration timestamp
  "iat": 1681304002,        // Issued at timestamp
  "sub": "owner",           // Subject (Benutzername)
  "zid": "20210629163300"   // Benutzer-Zettel-ID
}
```

### Sicherheitsmerkmale

1. **Verzögerter Login (~500ms):** Schutz vor Brute-Force-Angriffen
2. **Konfigurierbare Token-Lebensdauer:** Standard 10 Minuten (600s)
3. **Token-Arten:**
   - `KindAPI` - Für API-Zugriff (kürzere Lebensdauer)
   - `KindWebUI` - Für Web-UI-Sessions (längere Lebensdauer)

---

## Authentifizierung: Token Erhalten

### Endpunkt
```
POST /a
```

### Methoden

#### Methode 1: HTTP Basic Authentication (empfohlen)

```bash
curl -X POST -u USERNAME:PASSWORD http://127.0.0.1:23123/a
```

**Beispiel:**
```bash
curl -X POST -u owner:owner http://127.0.0.1:23123/a
```

#### Methode 2: URL-eingebettete Credentials

```bash
curl -X POST http://USERNAME:PASSWORD@127.0.0.1:23123/a
```

**Beispiel:**
```bash
curl -X POST http://owner:owner@127.0.0.1:23123/a
```

#### Methode 3: Form-Daten

```bash
curl -X POST -d 'username=USERNAME&password=PASSWORD' http://127.0.0.1:23123/a
```

**Beispiel:**
```bash
curl -X POST -d 'username=owner&password=owner' http://127.0.0.1:23123/a
```

### Response-Format

**Erfolgreiche Authentifizierung (200 OK):**

```lisp
("Bearer" "eyJhbGci...token..." 600)
```

**Elemente:**
1. **Authentifizierungs-Schema:** "Bearer"
2. **Access Token:** JWT-Token (String)
3. **Lebensdauer:** In Sekunden (z.B. 600 = 10 Minuten)

**Beispiel-Response:**
```lisp
("Bearer" "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJfdGsiOjEsImV4cCI6MTY4MTMwNDA2MiwiaWF0IjoxNjgxMzA0MDAyLCJzdWIiOiJvd25lciIsInppZCI6IjIwMjEwNjI5MTYzMzAwIn0.xYz..." 600)
```

### Token aus Response extrahieren

**Bash/Linux:**
```bash
TOKEN=$(curl -s -X POST -u owner:owner http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

echo $TOKEN
```

**Python:**
```python
import requests
import re

response = requests.post('http://127.0.0.1:23123/a', auth=('owner', 'owner'))
token = re.search(r'"Bearer" "([^"]+)"', response.text).group(1)
print(token)
```

### Fehlercodes

| Code | Bedeutung | Beschreibung |
|------|-----------|--------------|
| **200** | OK | Erfolgreiche Authentifizierung |
| **400** | Bad Request | Ungültige Anfrage |
| **401** | Unauthorized | Authentifizierung fehlgeschlagen (falsche Credentials) |
| **403** | Forbidden | Authentifizierung ist nicht aktiviert |

---

## Token Verwenden

### HTTP-Header-Format (RFC 6750)

```
Authorization: Bearer {access-token}
```

**Implementierung:** `internal/web/server/router.go::getHeaderToken`

### Beispiele

#### curl
```bash
curl -H "Authorization: Bearer eyJhbGci..." http://127.0.0.1:23123/z
```

#### Vollständiges Beispiel mit Token
```bash
# Token erhalten
TOKEN=$(curl -s -X POST -u owner:owner http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

# Token verwenden
curl -H "Authorization: Bearer $TOKEN" http://127.0.0.1:23123/z

# Zettel erstellen mit Token
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Neues Zettel\n\nInhalt hier' \
  http://127.0.0.1:23123/z

# Zettel löschen mit Token
curl -X DELETE \
  -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/20210903211500
```

#### Python mit requests
```python
import requests

# Token erhalten
response = requests.post('http://127.0.0.1:23123/a', auth=('owner', 'owner'))
token = re.search(r'"Bearer" "([^"]+)"', response.text).group(1)

# Headers vorbereiten
headers = {'Authorization': f'Bearer {token}'}

# Zettel abrufen
response = requests.get('http://127.0.0.1:23123/z', headers=headers)
print(response.text)
```

#### JavaScript/Node.js
```javascript
const axios = require('axios');

// Token erhalten
const authResponse = await axios.post('http://127.0.0.1:23123/a', null, {
  auth: { username: 'owner', password: 'owner' }
});

// Token extrahieren
const token = authResponse.data.match(/"Bearer" "([^"]+)"/)[1];

// Token verwenden
const headers = { 'Authorization': `Bearer ${token}` };
const zettelResponse = await axios.get('http://127.0.0.1:23123/z', { headers });
console.log(zettelResponse.data);
```

---

## Token Erneuern

### Endpunkt
```
PUT /a
```

**Mit Authorization-Header und bestehendem Token**

### Verhalten

- **Erstes Viertel der Lebensdauer:** Gibt bestehendes Token zurück
- **Danach:** Generiert neues Token mit voller Lebensdauer

**Implementierung:** `internal/web/adapter/api/login.go::MakeRenewAuthHandler`

### Beispiel

```bash
# Bestehendes Token erneuern
NEW_TOKEN=$(curl -s -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

echo "Neuer Token: $NEW_TOKEN"
```

### Empfohlene Strategie

```python
import time
import requests

class ZettelstoreClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None
        self.token_expires = 0

    def authenticate(self):
        """Neuen Token erhalten"""
        response = requests.post(
            f'{self.base_url}/a',
            auth=(self.username, self.password)
        )
        match = re.search(r'"Bearer" "([^"]+)" (\d+)', response.text)
        self.token = match.group(1)
        lifetime = int(match.group(2))
        self.token_expires = time.time() + lifetime

    def ensure_token(self):
        """Token erneuern wenn nötig"""
        # Erneuern wenn weniger als 60 Sekunden verbleiben
        if time.time() + 60 >= self.token_expires:
            self.renew_token()

    def renew_token(self):
        """Token erneuern"""
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.put(f'{self.base_url}/a', headers=headers)
        match = re.search(r'"Bearer" "([^"]+)" (\d+)', response.text)
        self.token = match.group(1)
        lifetime = int(match.group(2))
        self.token_expires = time.time() + lifetime

    def get_zettel(self, zid):
        """Zettel abrufen mit automatischer Token-Erneuerung"""
        self.ensure_token()
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f'{self.base_url}/z/{zid}', headers=headers)
        return response.text

# Verwendung
client = ZettelstoreClient('http://127.0.0.1:23123', 'owner', 'owner')
client.authenticate()

# Token wird automatisch erneuert wenn nötig
for i in range(100):
    zettel = client.get_zettel('20210903211500')
    time.sleep(10)
```

---

## Autorisierung: Berechtigungssystem

### Policy-Interface

**Implementierung:** `internal/auth/auth.go::Policy`

### Berechtigungs-Methoden

```go
type Policy interface {
    CanCreate(user *User, newMeta *Meta) bool
    CanRead(user *User, meta *Meta) bool
    CanWrite(user *User, oldMeta, newMeta *Meta) bool
    CanDelete(user *User, meta *Meta) bool
    CanRefresh(user *User) bool
}
```

### Benutzer-Rollen

| Rolle | Beschreibung |
|-------|--------------|
| **Owner** | Vollzugriff auf alle Zettel und System |
| **Writer** | Kann Zettel erstellen, lesen und bearbeiten |
| **Reader** | Kann nur Zettel lesen |
| **Creator** | Kann neue Zettel erstellen und eigene bearbeiten |
| **Public** | Unauthentifizierter Zugriff (begrenzt) |

### Policy-Implementierungen

**Quellcode:** `internal/auth/policy/`

| Policy | Datei | Beschreibung |
|--------|-------|--------------|
| **Default Policy** | `default.go` | Standard-Autorisierungsregeln |
| **Anonymous Policy** | `anon.go` | Richtlinien für anonymen Zugriff |
| **Owner Policy** | `owner.go` | Besitzer-spezifische Richtlinien |
| **Read-Only Policy** | `readonly.go` | Read-Only-Modus |
| **Box Policy** | `box.go` | Box-Level-Berechtigungen |

### Rechte-Flags (Bitmask)

```go
ZettelCanNone    = 0        // 0000
ZettelCanCreate  = 1 << 0   // 0001
ZettelCanRead    = 1 << 1   // 0010
ZettelCanWrite   = 1 << 2   // 0100
ZettelCanDelete  = 1 << 3   // 1000
```

**Vollzugriff:** `ZettelCanCreate | ZettelCanRead | ZettelCanWrite | ZettelCanDelete = 15`

**Implementierung:** `internal/web/adapter/api/api.go::getRights`

### Rechte in API-Responses

Wenn das `data`-Format verwendet wird, enthalten Responses Rechte-Informationen:

```lisp
(zettel
  (id "20210903211500")
  (meta ...)
  (rights 15)           ; Bitmask: 1111 = alle Rechte
  (encoding "zmk")
  (content "..."))
```

**Rechte-Interpretation:**

```python
def parse_rights(rights_value):
    permissions = {
        'create': bool(rights_value & 1),   # Bit 0
        'read':   bool(rights_value & 2),   # Bit 1
        'write':  bool(rights_value & 4),   # Bit 2
        'delete': bool(rights_value & 8)    # Bit 3
    }
    return permissions

# Beispiel
rights = parse_rights(15)
# {'create': True, 'read': True, 'write': True, 'delete': True}

rights = parse_rights(6)
# {'create': False, 'read': True, 'write': True, 'delete': False}
```

### Zettel-Sichtbarkeit

Zettel können Metadaten-Felder enthalten, die die Sichtbarkeit steuern:

```
title: Privates Zettel
role: zettel
visibility: owner
```

**Visibility-Werte:**
- `public` - Für alle sichtbar (auch unauthentifiziert)
- `login` - Nur für authentifizierte Benutzer
- `creator` - Nur für Ersteller
- `owner` - Nur für Owner

---

## Authentifizierungs-freier Modus

Wenn Authentifizierung deaktiviert ist, gibt der Server einen künstlichen Token zurück:

```bash
curl -X POST http://127.0.0.1:23123/a
```

**Response:**
```lisp
("Bearer" "freeaccess" 316224000)
```

**Token-Lebensdauer:** ~10 Jahre (316224000 Sekunden)

### Erkennung

```python
def is_auth_enabled(base_url):
    response = requests.post(f'{base_url}/a')
    if 'freeaccess' in response.text:
        return False
    return True

# Verwendung
if not is_auth_enabled('http://127.0.0.1:23123'):
    print("Authentifizierung ist deaktiviert")
    # Kein Token nötig für API-Calls
```

---

## Authentifizierungs-Status prüfen

### Endpunkt
```
POST /x?_command=authenticated
```

**Mit Authorization-Header**

### Response-Codes

| Code | Bedeutung | Beschreibung |
|------|-----------|--------------|
| **200** | OK | Authentifizierung ist deaktiviert |
| **204** | No Content | Token ist gültig |
| **401** | Unauthorized | Token ist ungültig oder fehlt |

### Beispiel

```bash
# Token-Gültigkeit prüfen
curl -i -X POST \
  -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/x?_command=authenticated'
```

**Erfolgreiche Antwort:**
```
HTTP/1.1 204 No Content
```

**Ungültiger Token:**
```
HTTP/1.1 401 Unauthorized
```

### Implementierung in Client

```python
def is_token_valid(base_url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(
        f'{base_url}/x?_command=authenticated',
        headers=headers
    )
    return response.status_code in [200, 204]

# Verwendung
if not is_token_valid('http://127.0.0.1:23123', token):
    print("Token ist ungültig, erneute Authentifizierung nötig")
    # Erneut authentifizieren
```

---

## Best Practices

### 1. Token-Verwaltung

```python
# ✅ GUT: Token sicher speichern und wiederverwenden
class SecureTokenStorage:
    def __init__(self):
        self.token = None
        self.expires = 0

    def store(self, token, lifetime):
        self.token = token
        self.expires = time.time() + lifetime

    def is_valid(self):
        return self.token and time.time() < self.expires - 60

    def get(self):
        return self.token if self.is_valid() else None

# ❌ SCHLECHT: Token bei jeder Anfrage neu erstellen
def bad_practice():
    for i in range(100):
        token = authenticate()  # Unnötige Wiederholung
        make_request(token)
```

### 2. Fehlerbehandlung

```python
# ✅ GUT: Robuste Fehlerbehandlung
def make_authenticated_request(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 401:
        # Token abgelaufen, erneut authentifizieren
        token = renew_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)

    if response.status_code == 403:
        raise PermissionError("Keine Berechtigung für diese Aktion")

    response.raise_for_status()
    return response.text

# ❌ SCHLECHT: Keine Fehlerbehandlung
def bad_practice(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    return requests.get(url, headers=headers).text
```

### 3. Credentials-Sicherheit

```python
# ✅ GUT: Credentials aus Environment-Variablen
import os

username = os.getenv('ZETTELSTORE_USER')
password = os.getenv('ZETTELSTORE_PASSWORD')

# ❌ SCHLECHT: Hardcodierte Credentials
username = 'owner'  # Niemals im Code!
password = 'owner'  # Niemals im Code!
```

### 4. HTTPS verwenden (Produktion)

```bash
# ✅ GUT: HTTPS in Produktion
curl -X POST -u owner:password https://zettelstore.example.com/a

# ❌ SCHLECHT: HTTP mit sensiblen Daten über Netzwerk
curl -X POST -u owner:password http://remote-server.com/a
```

### 5. Token-Rotation

```python
# ✅ GUT: Token proaktiv erneuern
class SmartClient:
    def request(self, url):
        # Erneuern wenn 25% der Lebensdauer verbleiben
        if self.token_age() > 0.75 * self.token_lifetime:
            self.renew_token()
        return self.make_request(url)

# ❌ SCHLECHT: Warten bis Token abläuft
class BadClient:
    def request(self, url):
        try:
            return self.make_request(url)
        except UnauthorizedError:
            self.authenticate()  # Zu spät!
            return self.make_request(url)
```

---

## Sicherheitshinweise

1. **Niemals Credentials im Code:** Verwende Environment-Variablen oder Secrets-Management
2. **HTTPS in Produktion:** HTTP nur für lokale Entwicklung
3. **Token-Speicherung:** Speichere Tokens sicher (nicht in Logs, nicht in Git)
4. **Brute-Force-Schutz:** Der Server verzögert Login-Versuche automatisch (~500ms)
5. **Token-Lebensdauer:** Kurze Lebensdauer für erhöhte Sicherheit
6. **Least Privilege:** Verwende Benutzer mit minimalen Rechten für automatisierte Tasks

---

## Troubleshooting

### Problem: 401 Unauthorized

**Ursachen:**
- Token ist abgelaufen
- Token ist ungültig
- Token fehlt im Header
- Falsches Format im Authorization-Header

**Lösung:**
```bash
# Token-Gültigkeit prüfen
curl -i -X POST \
  -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/x?_command=authenticated'

# Bei Ablauf: Neuen Token anfordern
TOKEN=$(curl -s -X POST -u owner:owner http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')
```

### Problem: 403 Forbidden

**Ursachen:**
- Keine Berechtigung für die Aktion
- Zettel-Visibility-Einschränkungen
- Read-Only-Modus aktiv

**Lösung:**
```bash
# Rechte für Zettel prüfen (data-Format)
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z/20210903211500?enc=data'

# Suche nach "rights" in der Response
# rights 15 = voller Zugriff
# rights 2 = nur lesen
```

### Problem: Authentifizierung dauert lange

**Ursache:** Intentionale Verzögerung (~500ms) zum Schutz vor Brute-Force

**Lösung:** Normal, kein Problem. Token wiederverwenden statt bei jeder Anfrage neu zu authentifizieren.

---

## Quellcode-Referenz

### Authentifizierungs-Implementierung

```
zettelstore/internal/auth/
├── auth.go                # Kern-Interfaces
├── impl/
│   ├── impl.go           # Auth-Manager
│   └── digest.go         # Token-Generierung (JWT)
├── policy/
│   ├── policy.go         # Policy-Interface
│   ├── default.go        # Standard-Regeln
│   ├── anon.go          # Anonymer Zugriff
│   ├── owner.go         # Owner-Policy
│   ├── readonly.go      # Read-Only
│   └── box.go           # Box-Permissions
└── cred/
    └── cred.go          # Credential-Handling
```

### API-Handler

```
zettelstore/internal/web/adapter/api/
├── login.go              # POST /a, PUT /a
├── command.go            # POST /x?_command=authenticated
└── api.go                # getRights() Funktion
```

---

**Version:** 1.0
**Letzte Aktualisierung:** 2025-11-12
**Basierend auf:** Zettelstore Version 0.19.0-dev
