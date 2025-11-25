# Zettelstore API - Code-Beispiele

Diese Dokumentation enthält praktische Code-Beispiele für die Verwendung der Zettelstore API in verschiedenen Programmiersprachen.

---

## 📑 Inhaltsverzeichnis

1. [Bash/Shell](#bashshell)
2. [Python](#python)
3. [JavaScript/Node.js](#javascriptnodejs)
4. [Go](#go)
5. [Java](#java)
6. [C#/.NET](#cnet)
7. [Verwendungsszenarien](#verwendungsszenarien)

---

## Bash/Shell

### Grundlegende Operationen

```bash
#!/bin/bash

# Konfiguration
BASE_URL="http://127.0.0.1:23123"
USERNAME="owner"
PASSWORD="owner"

# 1. Authentifizieren und Token erhalten
echo "Authentifiziere..."
TOKEN=$(curl -s -X POST -u "$USERNAME:$PASSWORD" "$BASE_URL/a" | \
  grep -oP '(?<="Bearer" ")[^"]+')

if [ -z "$TOKEN" ]; then
  echo "Fehler: Authentifizierung fehlgeschlagen"
  exit 1
fi

echo "Token erhalten: ${TOKEN:0:20}..."

# 2. Neues Zettel erstellen
echo "Erstelle neues Zettel..."
NEW_ZID=$(curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Bash Test Zettel\ntags: #bash #test\nrole: zettel\n\nDies ist ein Test-Zettel erstellt mit Bash.' \
  "$BASE_URL/z")

echo "Zettel erstellt mit ID: $NEW_ZID"

# 3. Zettel abrufen
echo "Rufe Zettel ab..."
curl -H "Authorization: Bearer $TOKEN" \
  "$BASE_URL/z/$NEW_ZID"

# 4. Zettel aktualisieren
echo "Aktualisiere Zettel..."
curl -s -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Aktualisiertes Bash Test Zettel\ntags: #bash #test #updated\n\nAktualisierter Inhalt.' \
  "$BASE_URL/z/$NEW_ZID"

echo "Zettel aktualisiert"

# 5. Alle Zettel mit Tag "test" finden
echo "Suche Zettel mit Tag 'test'..."
curl -H "Authorization: Bearer $TOKEN" \
  "$BASE_URL/z?tags%20HAS%20test"

# 6. Zettel löschen (optional)
read -p "Zettel löschen? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  curl -s -X DELETE \
    -H "Authorization: Bearer $TOKEN" \
    "$BASE_URL/z/$NEW_ZID"
  echo "Zettel gelöscht"
fi
```

### Erweiterte Bash-Funktionen

```bash
#!/bin/bash

BASE_URL="http://127.0.0.1:23123"

# Token-Management-Funktionen
authenticate() {
  local username="$1"
  local password="$2"
  curl -s -X POST -u "$username:$password" "$BASE_URL/a" | \
    grep -oP '(?<="Bearer" ")[^"]+')
}

renew_token() {
  local token="$1"
  curl -s -X PUT -H "Authorization: Bearer $token" "$BASE_URL/a" | \
    grep -oP '(?<="Bearer" ")[^"]+')
}

is_token_valid() {
  local token="$1"
  local status=$(curl -s -o /dev/null -w "%{http_code}" \
    -X POST -H "Authorization: Bearer $token" \
    "$BASE_URL/x?_command=authenticated")
  [ "$status" -eq 204 ] || [ "$status" -eq 200 ]
}

# Zettel-CRUD-Funktionen
create_zettel() {
  local token="$1"
  local title="$2"
  local content="$3"
  local tags="${4:-#default}"

  curl -s -X POST \
    -H "Authorization: Bearer $token" \
    --data "title: $title
tags: $tags
role: zettel

$content" \
    "$BASE_URL/z"
}

get_zettel() {
  local token="$1"
  local zid="$2"
  curl -s -H "Authorization: Bearer $token" \
    "$BASE_URL/z/$zid"
}

update_zettel() {
  local token="$1"
  local zid="$2"
  local title="$3"
  local content="$4"
  local tags="${5:-#default}"

  curl -s -X PUT \
    -H "Authorization: Bearer $token" \
    --data "title: $title
tags: $tags

$content" \
    "$BASE_URL/z/$zid"
}

delete_zettel() {
  local token="$1"
  local zid="$2"
  curl -s -X DELETE \
    -H "Authorization: Bearer $token" \
    "$BASE_URL/z/$zid"
}

query_zettel() {
  local token="$1"
  local query="$2"
  curl -s -H "Authorization: Bearer $token" \
    "$BASE_URL/z?$(echo "$query" | sed 's/ /%20/g')"
}

# Verwendung
TOKEN=$(authenticate "owner" "owner")
echo "Token: ${TOKEN:0:20}..."

# Zettel erstellen
ZID=$(create_zettel "$TOKEN" "Mein Zettel" "Inhalt hier" "#wichtig #projekt")
echo "Erstellt: $ZID"

# Zettel abrufen
echo "Inhalt:"
get_zettel "$TOKEN" "$ZID"

# Query
echo "Alle Zettel mit Tag 'projekt':"
query_zettel "$TOKEN" "tags HAS projekt"

# Zettel aktualisieren
update_zettel "$TOKEN" "$ZID" "Aktualisiert" "Neuer Inhalt" "#wichtig #updated"

# Zettel löschen
delete_zettel "$TOKEN" "$ZID"
echo "Gelöscht"
```

---

## Python

### Einfacher Client

```python
import requests
import re
from typing import Optional, Dict, List

class ZettelstoreClient:
    def __init__(self, base_url: str = "http://127.0.0.1:23123"):
        self.base_url = base_url
        self.token: Optional[str] = None

    def authenticate(self, username: str, password: str) -> bool:
        """Authentifizierung und Token-Erhalt"""
        try:
            response = requests.post(
                f'{self.base_url}/a',
                auth=(username, password)
            )
            response.raise_for_status()

            # Token extrahieren
            match = re.search(r'"Bearer" "([^"]+)"', response.text)
            if match:
                self.token = match.group(1)
                return True
            return False
        except requests.RequestException as e:
            print(f"Authentifizierungsfehler: {e}")
            return False

    def _get_headers(self) -> Dict[str, str]:
        """Erstellt Authorization-Header"""
        if not self.token:
            raise ValueError("Nicht authentifiziert. Bitte zuerst authenticate() aufrufen.")
        return {'Authorization': f'Bearer {self.token}'}

    def create_zettel(self, title: str, content: str, tags: str = "",
                     role: str = "zettel", **kwargs) -> Optional[str]:
        """Erstellt ein neues Zettel"""
        # Metadaten zusammenstellen
        metadata = f"title: {title}\n"
        if tags:
            metadata += f"tags: {tags}\n"
        metadata += f"role: {role}\n"

        # Zusätzliche Metadaten
        for key, value in kwargs.items():
            metadata += f"{key}: {value}\n"

        # Vollständiger Body
        body = f"{metadata}\n{content}"

        try:
            response = requests.post(
                f'{self.base_url}/z',
                headers=self._get_headers(),
                data=body.encode('utf-8')
            )
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as e:
            print(f"Fehler beim Erstellen: {e}")
            return None

    def get_zettel(self, zid: str, format: str = "plain") -> Optional[str]:
        """Ruft ein Zettel ab"""
        try:
            url = f'{self.base_url}/z/{zid}'
            if format != "plain":
                url += f'?enc={format}'

            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Fehler beim Abrufen: {e}")
            return None

    def update_zettel(self, zid: str, title: str, content: str,
                     tags: str = "", **kwargs) -> bool:
        """Aktualisiert ein Zettel"""
        # Metadaten zusammenstellen
        metadata = f"title: {title}\n"
        if tags:
            metadata += f"tags: {tags}\n"

        for key, value in kwargs.items():
            metadata += f"{key}: {value}\n"

        body = f"{metadata}\n{content}"

        try:
            response = requests.put(
                f'{self.base_url}/z/{zid}',
                headers=self._get_headers(),
                data=body.encode('utf-8')
            )
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Fehler beim Aktualisieren: {e}")
            return False

    def delete_zettel(self, zid: str) -> bool:
        """Löscht ein Zettel"""
        try:
            response = requests.delete(
                f'{self.base_url}/z/{zid}',
                headers=self._get_headers()
            )
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Fehler beim Löschen: {e}")
            return False

    def query_zettel(self, query: str = "", format: str = "plain") -> Optional[str]:
        """Führt eine Query aus"""
        try:
            url = f'{self.base_url}/z'
            params = {}
            if query:
                url += f'?{query}'
            if format != "plain":
                params['enc'] = format

            response = requests.get(url, headers=self._get_headers(), params=params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Fehler bei Query: {e}")
            return None

    def get_references(self, zid: str) -> List[str]:
        """Ruft Referenzen eines Zettels ab"""
        try:
            response = requests.get(
                f'{self.base_url}/r/{zid}',
                headers=self._get_headers()
            )
            response.raise_for_status()
            return [line.strip() for line in response.text.split('\n') if line.strip()]
        except requests.RequestException as e:
            print(f"Fehler beim Abrufen der Referenzen: {e}")
            return []


# Verwendungsbeispiel
if __name__ == "__main__":
    # Client initialisieren
    client = ZettelstoreClient()

    # Authentifizieren
    if client.authenticate("owner", "owner"):
        print("✓ Erfolgreich authentifiziert")

        # Zettel erstellen
        zid = client.create_zettel(
            title="Python API Test",
            content="Dies ist ein Test-Zettel erstellt mit Python.",
            tags="#python #api #test"
        )
        print(f"✓ Zettel erstellt: {zid}")

        # Zettel abrufen
        content = client.get_zettel(zid)
        print(f"✓ Zettel abgerufen:\n{content}")

        # Zettel aktualisieren
        if client.update_zettel(
            zid,
            title="Aktualisiertes Python API Test",
            content="Aktualisierter Inhalt.",
            tags="#python #api #updated"
        ):
            print("✓ Zettel aktualisiert")

        # Query ausführen
        results = client.query_zettel("tags HAS python")
        print(f"✓ Query-Ergebnisse:\n{results}")

        # Referenzen abrufen
        refs = client.get_references(zid)
        print(f"✓ Referenzen: {refs}")

        # Zettel löschen (optional)
        # if client.delete_zettel(zid):
        #     print("✓ Zettel gelöscht")
    else:
        print("✗ Authentifizierung fehlgeschlagen")
```

### Erweiterter Python-Client mit Token-Management

```python
import requests
import re
import time
from typing import Optional, Dict
from datetime import datetime, timedelta

class AdvancedZettelstoreClient:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token: Optional[str] = None
        self.token_expires: Optional[datetime] = None

    def authenticate(self) -> bool:
        """Neue Authentifizierung"""
        try:
            response = requests.post(
                f'{self.base_url}/a',
                auth=(self.username, self.password)
            )
            response.raise_for_status()

            match = re.search(r'"Bearer" "([^"]+)" (\d+)', response.text)
            if match:
                self.token = match.group(1)
                lifetime = int(match.group(2))
                self.token_expires = datetime.now() + timedelta(seconds=lifetime)
                return True
            return False
        except requests.RequestException as e:
            print(f"Authentifizierungsfehler: {e}")
            return False

    def renew_token(self) -> bool:
        """Token erneuern"""
        if not self.token:
            return self.authenticate()

        try:
            response = requests.put(
                f'{self.base_url}/a',
                headers={'Authorization': f'Bearer {self.token}'}
            )
            response.raise_for_status()

            match = re.search(r'"Bearer" "([^"]+)" (\d+)', response.text)
            if match:
                self.token = match.group(1)
                lifetime = int(match.group(2))
                self.token_expires = datetime.now() + timedelta(seconds=lifetime)
                return True
            return False
        except requests.RequestException:
            return self.authenticate()

    def ensure_token(self) -> bool:
        """Stellt sicher, dass ein gültiger Token vorhanden ist"""
        if not self.token or not self.token_expires:
            return self.authenticate()

        # Token erneuern wenn weniger als 60 Sekunden verbleiben
        if datetime.now() + timedelta(seconds=60) >= self.token_expires:
            return self.renew_token()

        return True

    def is_token_valid(self) -> bool:
        """Prüft Token-Gültigkeit"""
        if not self.token:
            return False

        try:
            response = requests.post(
                f'{self.base_url}/x?_command=authenticated',
                headers={'Authorization': f'Bearer {self.token}'}
            )
            return response.status_code in [200, 204]
        except requests.RequestException:
            return False

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Macht einen API-Request mit automatischer Token-Verwaltung"""
        self.ensure_token()

        headers = kwargs.pop('headers', {})
        headers['Authorization'] = f'Bearer {self.token}'

        url = f'{self.base_url}{endpoint}'
        response = requests.request(method, url, headers=headers, **kwargs)

        # Bei 401: Token erneuern und erneut versuchen
        if response.status_code == 401:
            if self.renew_token():
                headers['Authorization'] = f'Bearer {self.token}'
                response = requests.request(method, url, headers=headers, **kwargs)

        return response

    def create_zettel(self, title: str, content: str, **metadata) -> Optional[str]:
        """Erstellt ein Zettel mit automatischem Token-Management"""
        meta_str = f"title: {title}\n"
        for key, value in metadata.items():
            meta_str += f"{key}: {value}\n"

        body = f"{meta_str}\n{content}"

        try:
            response = self._make_request('POST', '/z', data=body.encode('utf-8'))
            response.raise_for_status()
            return response.text.strip()
        except requests.RequestException as e:
            print(f"Fehler: {e}")
            return None

    def get_zettel(self, zid: str) -> Optional[Dict]:
        """Ruft Zettel mit Metadaten ab"""
        try:
            response = self._make_request('GET', f'/z/{zid}')
            response.raise_for_status()

            # Parse plain format
            text = response.text
            parts = text.split('\n\n', 1)

            metadata = {}
            if len(parts) >= 1:
                for line in parts[0].split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip()

            content = parts[1] if len(parts) > 1 else ""

            return {
                'id': zid,
                'metadata': metadata,
                'content': content
            }
        except requests.RequestException as e:
            print(f"Fehler: {e}")
            return None


# Verwendung
if __name__ == "__main__":
    client = AdvancedZettelstoreClient(
        "http://127.0.0.1:23123",
        "owner",
        "owner"
    )

    # Automatische Authentifizierung bei erstem Request
    zid = client.create_zettel(
        "Automatischer Test",
        "Inhalt mit automatischem Token-Management",
        tags="#auto #test",
        role="zettel"
    )
    print(f"Erstellt: {zid}")

    # Token wird automatisch erneuert wenn nötig
    for i in range(100):
        zettel = client.get_zettel(zid)
        print(f"Iteration {i}: {zettel['metadata'].get('title')}")
        time.sleep(10)
```

---

## JavaScript/Node.js

### Basis-Client

```javascript
const axios = require('axios');

class ZettelstoreClient {
  constructor(baseUrl = 'http://127.0.0.1:23123') {
    this.baseUrl = baseUrl;
    this.token = null;
  }

  async authenticate(username, password) {
    try {
      const response = await axios.post(`${this.baseUrl}/a`, null, {
        auth: { username, password }
      });

      // Token extrahieren
      const match = response.data.match(/"Bearer" "([^"]+)"/);
      if (match) {
        this.token = match[1];
        return true;
      }
      return false;
    } catch (error) {
      console.error('Authentifizierungsfehler:', error.message);
      return false;
    }
  }

  _getHeaders() {
    if (!this.token) {
      throw new Error('Nicht authentifiziert');
    }
    return {
      'Authorization': `Bearer ${this.token}`
    };
  }

  async createZettel(title, content, tags = '', metadata = {}) {
    let body = `title: ${title}\n`;
    if (tags) body += `tags: ${tags}\n`;
    body += 'role: zettel\n';

    for (const [key, value] of Object.entries(metadata)) {
      body += `${key}: ${value}\n`;
    }

    body += `\n${content}`;

    try {
      const response = await axios.post(
        `${this.baseUrl}/z`,
        body,
        { headers: this._getHeaders() }
      );
      return response.data.trim();
    } catch (error) {
      console.error('Fehler beim Erstellen:', error.message);
      return null;
    }
  }

  async getZettel(zid, format = 'plain') {
    try {
      let url = `${this.baseUrl}/z/${zid}`;
      if (format !== 'plain') {
        url += `?enc=${format}`;
      }

      const response = await axios.get(url, {
        headers: this._getHeaders()
      });
      return response.data;
    } catch (error) {
      console.error('Fehler beim Abrufen:', error.message);
      return null;
    }
  }

  async updateZettel(zid, title, content, tags = '', metadata = {}) {
    let body = `title: ${title}\n`;
    if (tags) body += `tags: ${tags}\n`;

    for (const [key, value] of Object.entries(metadata)) {
      body += `${key}: ${value}\n`;
    }

    body += `\n${content}`;

    try {
      await axios.put(
        `${this.baseUrl}/z/${zid}`,
        body,
        { headers: this._getHeaders() }
      );
      return true;
    } catch (error) {
      console.error('Fehler beim Aktualisieren:', error.message);
      return false;
    }
  }

  async deleteZettel(zid) {
    try {
      await axios.delete(
        `${this.baseUrl}/z/${zid}`,
        { headers: this._getHeaders() }
      );
      return true;
    } catch (error) {
      console.error('Fehler beim Löschen:', error.message);
      return false;
    }
  }

  async queryZettel(query = '', format = 'plain') {
    try {
      let url = `${this.baseUrl}/z`;
      if (query) url += `?${query}`;
      if (format !== 'plain') {
        url += (query ? '&' : '?') + `enc=${format}`;
      }

      const response = await axios.get(url, {
        headers: this._getHeaders()
      });
      return response.data;
    } catch (error) {
      console.error('Fehler bei Query:', error.message);
      return null;
    }
  }

  async getReferences(zid) {
    try {
      const response = await axios.get(
        `${this.baseUrl}/r/${zid}`,
        { headers: this._getHeaders() }
      );
      return response.data.split('\n').filter(line => line.trim());
    } catch (error) {
      console.error('Fehler beim Abrufen der Referenzen:', error.message);
      return [];
    }
  }
}

// Verwendung
async function main() {
  const client = new ZettelstoreClient();

  // Authentifizieren
  if (await client.authenticate('owner', 'owner')) {
    console.log('✓ Authentifiziert');

    // Zettel erstellen
    const zid = await client.createZettel(
      'JavaScript API Test',
      'Dies ist ein Test-Zettel erstellt mit JavaScript.',
      '#javascript #api #test'
    );
    console.log(`✓ Zettel erstellt: ${zid}`);

    // Zettel abrufen
    const content = await client.getZettel(zid);
    console.log(`✓ Zettel abgerufen:\n${content}`);

    // Zettel aktualisieren
    await client.updateZettel(
      zid,
      'Aktualisiertes JavaScript API Test',
      'Aktualisierter Inhalt.',
      '#javascript #api #updated'
    );
    console.log('✓ Zettel aktualisiert');

    // Query ausführen
    const results = await client.queryZettel('tags HAS javascript');
    console.log(`✓ Query-Ergebnisse:\n${results}`);

    // Optional: Zettel löschen
    // await client.deleteZettel(zid);
    // console.log('✓ Zettel gelöscht');
  } else {
    console.log('✗ Authentifizierung fehlgeschlagen');
  }
}

main();
```

---

## Go

### Nutzung der offiziellen Client-Bibliothek

```go
package main

import (
	"context"
	"fmt"
	"log"

	"t73f.de/r/zsc/api"
	"t73f.de/r/zsc/client"
)

func main() {
	// Client erstellen
	c := client.NewClient("http://127.0.0.1:23123")

	// Authentifizierung setzen
	c.SetAuth("owner", "owner")

	ctx := context.Background()

	// Zettel erstellen
	zettel := api.ZettelData{
		Meta: api.ZidMetaJSON{
			api.KeyTitle: "Go API Test",
			api.KeyTags:  "#go #api #test",
			api.KeyRole:  "zettel",
		},
		Encoding: "zmk",
		Content:  "Dies ist ein Test-Zettel erstellt mit Go.",
	}

	zid, err := c.CreateZettel(ctx, &zettel)
	if err != nil {
		log.Fatalf("Fehler beim Erstellen: %v", err)
	}
	fmt.Printf("✓ Zettel erstellt: %s\n", zid)

	// Zettel abrufen
	retrievedZettel, err := c.GetZettelData(ctx, zid)
	if err != nil {
		log.Fatalf("Fehler beim Abrufen: %v", err)
	}
	fmt.Printf("✓ Zettel abgerufen: %s\n", retrievedZettel.Meta[api.KeyTitle])

	// Zettel aktualisieren
	retrievedZettel.Meta[api.KeyTitle] = "Aktualisiertes Go API Test"
	retrievedZettel.Meta[api.KeyTags] = "#go #api #updated"
	retrievedZettel.Content = "Aktualisierter Inhalt."

	err = c.UpdateZettel(ctx, zid, retrievedZettel)
	if err != nil {
		log.Fatalf("Fehler beim Aktualisieren: %v", err)
	}
	fmt.Println("✓ Zettel aktualisiert")

	// Query ausführen
	query := "tags HAS go"
	_, _, list, err := c.QueryZettelData(ctx, query)
	if err != nil {
		log.Fatalf("Fehler bei Query: %v", err)
	}
	fmt.Printf("✓ Query gefunden: %d Zettel\n", len(list))

	// Optional: Zettel löschen
	// err = c.DeleteZettel(ctx, zid)
	// if err != nil {
	// 	log.Fatalf("Fehler beim Löschen: %v", err)
	// }
	// fmt.Println("✓ Zettel gelöscht")
}
```

---

## Java

### Java-Client mit HttpClient

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ZettelstoreClient {
    private final String baseUrl;
    private final HttpClient httpClient;
    private String token;

    public ZettelstoreClient(String baseUrl) {
        this.baseUrl = baseUrl;
        this.httpClient = HttpClient.newHttpClient();
    }

    public boolean authenticate(String username, String password) throws Exception {
        String auth = username + ":" + password;
        String encodedAuth = Base64.getEncoder()
            .encodeToString(auth.getBytes(StandardCharsets.UTF_8));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/a"))
            .header("Authorization", "Basic " + encodedAuth)
            .POST(HttpRequest.BodyPublishers.noBody())
            .build();

        HttpResponse<String> response = httpClient.send(
            request,
            HttpResponse.BodyHandlers.ofString()
        );

        if (response.statusCode() == 200) {
            Pattern pattern = Pattern.compile("\"Bearer\" \"([^\"]+)\"");
            Matcher matcher = pattern.matcher(response.body());
            if (matcher.find()) {
                this.token = matcher.group(1);
                return true;
            }
        }
        return false;
    }

    public String createZettel(String title, String content, String tags) throws Exception {
        String body = String.format(
            "title: %s\ntags: %s\nrole: zettel\n\n%s",
            title, tags, content
        );

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/z"))
            .header("Authorization", "Bearer " + token)
            .header("Content-Type", "text/plain; charset=UTF-8")
            .POST(HttpRequest.BodyPublishers.ofString(body, StandardCharsets.UTF_8))
            .build();

        HttpResponse<String> response = httpClient.send(
            request,
            HttpResponse.BodyHandlers.ofString()
        );

        if (response.statusCode() == 201) {
            return response.body().trim();
        }
        throw new RuntimeException("Fehler beim Erstellen: " + response.statusCode());
    }

    public String getZettel(String zid) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/z/" + zid))
            .header("Authorization", "Bearer " + token)
            .GET()
            .build();

        HttpResponse<String> response = httpClient.send(
            request,
            HttpResponse.BodyHandlers.ofString()
        );

        if (response.statusCode() == 200) {
            return response.body();
        }
        throw new RuntimeException("Fehler beim Abrufen: " + response.statusCode());
    }

    public boolean updateZettel(String zid, String title, String content, String tags)
            throws Exception {
        String body = String.format(
            "title: %s\ntags: %s\n\n%s",
            title, tags, content
        );

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/z/" + zid))
            .header("Authorization", "Bearer " + token)
            .header("Content-Type", "text/plain; charset=UTF-8")
            .PUT(HttpRequest.BodyPublishers.ofString(body, StandardCharsets.UTF_8))
            .build();

        HttpResponse<String> response = httpClient.send(
            request,
            HttpResponse.BodyHandlers.ofString()
        );

        return response.statusCode() == 204;
    }

    public boolean deleteZettel(String zid) throws Exception {
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(baseUrl + "/z/" + zid))
            .header("Authorization", "Bearer " + token)
            .DELETE()
            .build();

        HttpResponse<String> response = httpClient.send(
            request,
            HttpResponse.BodyHandlers.ofString()
        );

        return response.statusCode() == 204;
    }

    public static void main(String[] args) {
        try {
            ZettelstoreClient client = new ZettelstoreClient("http://127.0.0.1:23123");

            // Authentifizieren
            if (client.authenticate("owner", "owner")) {
                System.out.println("✓ Authentifiziert");

                // Zettel erstellen
                String zid = client.createZettel(
                    "Java API Test",
                    "Dies ist ein Test-Zettel erstellt mit Java.",
                    "#java #api #test"
                );
                System.out.println("✓ Zettel erstellt: " + zid);

                // Zettel abrufen
                String content = client.getZettel(zid);
                System.out.println("✓ Zettel abgerufen:\n" + content);

                // Zettel aktualisieren
                client.updateZettel(
                    zid,
                    "Aktualisiertes Java API Test",
                    "Aktualisierter Inhalt.",
                    "#java #api #updated"
                );
                System.out.println("✓ Zettel aktualisiert");

                // Optional: Zettel löschen
                // client.deleteZettel(zid);
                // System.out.println("✓ Zettel gelöscht");
            } else {
                System.out.println("✗ Authentifizierung fehlgeschlagen");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

---

## C#/.NET

### C#-Client

```csharp
using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

public class ZettelstoreClient
{
    private readonly string baseUrl;
    private readonly HttpClient httpClient;
    private string token;

    public ZettelstoreClient(string baseUrl)
    {
        this.baseUrl = baseUrl;
        this.httpClient = new HttpClient();
    }

    public async Task<bool> AuthenticateAsync(string username, string password)
    {
        var authBytes = Encoding.UTF8.GetBytes($"{username}:{password}");
        var authHeader = Convert.ToBase64String(authBytes);

        var request = new HttpRequestMessage(HttpMethod.Post, $"{baseUrl}/a");
        request.Headers.Authorization = new AuthenticationHeaderValue("Basic", authHeader);

        var response = await httpClient.SendAsync(request);

        if (response.IsSuccessStatusCode)
        {
            var content = await response.Content.ReadAsStringAsync();
            var match = Regex.Match(content, @"""Bearer"" ""([^""]+)""");
            if (match.Success)
            {
                token = match.Groups[1].Value;
                return true;
            }
        }
        return false;
    }

    public async Task<string> CreateZettelAsync(string title, string content, string tags = "")
    {
        var body = $"title: {title}\n";
        if (!string.IsNullOrEmpty(tags))
            body += $"tags: {tags}\n";
        body += $"role: zettel\n\n{content}";

        var request = new HttpRequestMessage(HttpMethod.Post, $"{baseUrl}/z");
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);
        request.Content = new StringContent(body, Encoding.UTF8, "text/plain");

        var response = await httpClient.SendAsync(request);
        response.EnsureSuccessStatusCode();

        return (await response.Content.ReadAsStringAsync()).Trim();
    }

    public async Task<string> GetZettelAsync(string zid)
    {
        var request = new HttpRequestMessage(HttpMethod.Get, $"{baseUrl}/z/{zid}");
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var response = await httpClient.SendAsync(request);
        response.EnsureSuccessStatusCode();

        return await response.Content.ReadAsStringAsync();
    }

    public async Task<bool> UpdateZettelAsync(string zid, string title, string content, string tags = "")
    {
        var body = $"title: {title}\n";
        if (!string.IsNullOrEmpty(tags))
            body += $"tags: {tags}\n";
        body += $"\n{content}";

        var request = new HttpRequestMessage(HttpMethod.Put, $"{baseUrl}/z/{zid}");
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);
        request.Content = new StringContent(body, Encoding.UTF8, "text/plain");

        var response = await httpClient.SendAsync(request);
        return response.IsSuccessStatusCode;
    }

    public async Task<bool> DeleteZettelAsync(string zid)
    {
        var request = new HttpRequestMessage(HttpMethod.Delete, $"{baseUrl}/z/{zid}");
        request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var response = await httpClient.SendAsync(request);
        return response.IsSuccessStatusCode;
    }

    public static async Task Main()
    {
        var client = new ZettelstoreClient("http://127.0.0.1:23123");

        // Authentifizieren
        if (await client.AuthenticateAsync("owner", "owner"))
        {
            Console.WriteLine("✓ Authentifiziert");

            // Zettel erstellen
            var zid = await client.CreateZettelAsync(
                "C# API Test",
                "Dies ist ein Test-Zettel erstellt mit C#.",
                "#csharp #api #test"
            );
            Console.WriteLine($"✓ Zettel erstellt: {zid}");

            // Zettel abrufen
            var content = await client.GetZettelAsync(zid);
            Console.WriteLine($"✓ Zettel abgerufen:\n{content}");

            // Zettel aktualisieren
            await client.UpdateZettelAsync(
                zid,
                "Aktualisiertes C# API Test",
                "Aktualisierter Inhalt.",
                "#csharp #api #updated"
            );
            Console.WriteLine("✓ Zettel aktualisiert");

            // Optional: Zettel löschen
            // await client.DeleteZettelAsync(zid);
            // Console.WriteLine("✓ Zettel gelöscht");
        }
        else
        {
            Console.WriteLine("✗ Authentifizierung fehlgeschlagen");
        }
    }
}
```

---

## Verwendungsszenarien

### 1. Automatisches Backup-System

```python
import os
import json
from datetime import datetime

class ZettelstoreBackup:
    def __init__(self, client, backup_dir):
        self.client = client
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)

    def backup_all(self):
        """Erstellt Backup aller Zettel"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(self.backup_dir, f'backup_{timestamp}')
        os.makedirs(backup_path)

        # Alle Zettel abrufen
        result = self.client.query_zettel("")
        zettel_ids = [line.split()[0] for line in result.split('\n') if line.strip()]

        for zid in zettel_ids:
            zettel = self.client.get_zettel(zid)
            if zettel:
                filepath = os.path.join(backup_path, f'{zid}.txt')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(zettel)

        print(f"Backup erstellt: {len(zettel_ids)} Zettel in {backup_path}")
        return backup_path

# Verwendung
client = ZettelstoreClient()
client.authenticate('owner', 'owner')

backup = ZettelstoreBackup(client, './backups')
backup.backup_all()
```

### 2. Zettel-Synchronisation zwischen Instanzen

```python
class ZettelstoreSync:
    def __init__(self, source_client, target_client):
        self.source = source_client
        self.target = target_client

    def sync_by_tag(self, tag):
        """Synchronisiert Zettel mit bestimmtem Tag"""
        # Zettel in Quelle finden
        result = self.source.query_zettel(f"tags HAS {tag}")
        source_ids = [line.split()[0] for line in result.split('\n') if line.strip()]

        synced = 0
        for zid in source_ids:
            # Zettel von Quelle abrufen
            source_zettel = self.source.get_zettel(zid)
            if not source_zettel:
                continue

            # Prüfen ob im Ziel vorhanden
            target_zettel = self.target.get_zettel(zid)

            # Parse Metadaten und Inhalt
            parts = source_zettel.split('\n\n', 1)
            metadata_lines = parts[0].split('\n')
            content = parts[1] if len(parts) > 1 else ""

            # Extrahiere Titel und Tags
            title = ""
            tags = ""
            for line in metadata_lines:
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip()
                elif line.startswith('tags:'):
                    tags = line.split(':', 1)[1].strip()

            if target_zettel is None:
                # Neu erstellen
                self.target.create_zettel(title, content, tags)
                synced += 1
            else:
                # Aktualisieren
                self.target.update_zettel(zid, title, content, tags)
                synced += 1

        print(f"Synchronisiert: {synced} Zettel mit Tag '{tag}'")

# Verwendung
source = ZettelstoreClient('http://source.example.com:23123')
source.authenticate('user', 'pass')

target = ZettelstoreClient('http://target.example.com:23123')
target.authenticate('user', 'pass')

sync = ZettelstoreSync(source, target)
sync.sync_by_tag('sync')
```

### 3. Content-Migration-Tool

```python
import markdown
import html2text

class ContentMigration:
    def __init__(self, client):
        self.client = client

    def import_from_markdown(self, filepath):
        """Importiert Markdown-Dateien als Zettel"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Erste Zeile als Titel verwenden
        lines = content.split('\n')
        title = lines[0].replace('#', '').strip()
        content = '\n'.join(lines[1:]).strip()

        # Als Zettel erstellen
        zid = self.client.create_zettel(
            title,
            content,
            tags='#imported #markdown',
            syntax='md'
        )
        print(f"Importiert: {title} -> {zid}")
        return zid

    def export_to_markdown(self, zid, output_path):
        """Exportiert Zettel als Markdown"""
        zettel = self.client.get_zettel(zid, format='md')
        if zettel:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(zettel)
            print(f"Exportiert: {zid} -> {output_path}")

# Verwendung
client = ZettelstoreClient()
client.authenticate('owner', 'owner')

migration = ContentMigration(client)

# Import
migration.import_from_markdown('document.md')

# Export
migration.export_to_markdown('20210903211500', 'exported.md')
```

### 4. Automatische Tagging/Kategorisierung

```python
import re
from collections import Counter

class AutoTagger:
    def __init__(self, client):
        self.client = client

    def suggest_tags(self, content, num_tags=3):
        """Schlägt Tags basierend auf Inhalt vor"""
        # Wörter extrahieren
        words = re.findall(r'\b[a-zäöüß]+\b', content.lower())

        # Stopwörter entfernen
        stopwords = {'der', 'die', 'das', 'und', 'oder', 'ein', 'eine', 'ist', 'sind'}
        words = [w for w in words if w not in stopwords and len(w) > 3]

        # Häufigste Wörter
        counter = Counter(words)
        suggestions = [f"#{word}" for word, _ in counter.most_common(num_tags)]

        return ' '.join(suggestions)

    def auto_tag_zettel(self, zid):
        """Fügt automatisch Tags zu Zettel hinzu"""
        zettel = self.client.get_zettel(zid)
        if not zettel:
            return

        # Parse
        parts = zettel.split('\n\n', 1)
        metadata_lines = parts[0].split('\n')
        content = parts[1] if len(parts) > 1 else ""

        # Extrahiere aktuelle Metadaten
        title = ""
        current_tags = ""
        for line in metadata_lines:
            if line.startswith('title:'):
                title = line.split(':', 1)[1].strip()
            elif line.startswith('tags:'):
                current_tags = line.split(':', 1)[1].strip()

        # Tags vorschlagen
        suggested = self.suggest_tags(content)

        # Kombinieren
        all_tags = f"{current_tags} {suggested}".strip()

        # Aktualisieren
        self.client.update_zettel(zid, title, content, all_tags)
        print(f"Auto-Tagged {zid}: {suggested}")

# Verwendung
client = ZettelstoreClient()
client.authenticate('owner', 'owner')

tagger = AutoTagger(client)
tagger.auto_tag_zettel('20210903211500')
```

---

## Best Practices

### 1. Fehlerbehandlung

Implementiere immer robuste Fehlerbehandlung:

```python
def safe_create_zettel(client, title, content, retries=3):
    """Erstellt Zettel mit Wiederholungsversuchen"""
    for attempt in range(retries):
        try:
            zid = client.create_zettel(title, content)
            return zid
        except requests.RequestException as e:
            if attempt < retries - 1:
                print(f"Versuch {attempt + 1} fehlgeschlagen, wiederhole...")
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise Exception(f"Fehler nach {retries} Versuchen: {e}")
```

### 2. Rate Limiting

Respektiere Server-Limits:

```python
import time

class RateLimitedClient:
    def __init__(self, client, requests_per_second=10):
        self.client = client
        self.min_interval = 1.0 / requests_per_second
        self.last_request = 0

    def _wait_if_needed(self):
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request = time.time()

    def create_zettel(self, *args, **kwargs):
        self._wait_if_needed()
        return self.client.create_zettel(*args, **kwargs)
```

### 3. Batch-Operationen

Optimiere für viele Operationen:

```python
def batch_create(client, zettel_list, batch_size=10):
    """Erstellt Zettel in Batches"""
    created = []
    for i in range(0, len(zettel_list), batch_size):
        batch = zettel_list[i:i + batch_size]
        for zettel in batch:
            zid = client.create_zettel(**zettel)
            created.append(zid)
        print(f"Batch {i//batch_size + 1}: {len(batch)} Zettel erstellt")
        time.sleep(0.5)  # Kurze Pause zwischen Batches
    return created
```

---

**Version:** 1.0
**Letzte Aktualisierung:** 2025-11-12
**Basierend auf:** Zettelstore Version 0.19.0-dev
