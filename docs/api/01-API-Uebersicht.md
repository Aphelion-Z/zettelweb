# Zettelstore API - Übersicht

## Einführung

Die Zettelstore API ist eine HTTP-basierte RESTful API, die vollständigen programmatischen Zugriff auf das Zettelstore-System ermöglicht. Sie dient als primäre Schnittstelle für alle Operationen mit Zetteln (Notizen/Dokumenten).

## Grundlegende Informationen

### Basis-URL
```
http://127.0.0.1:23123/
```

**Standardkonfiguration:**
- **Protokoll:** HTTP (HTTPS wird unterstützt)
- **Host:** 127.0.0.1 (localhost)
- **Port:** 23123 (konfigurierbar)
- **URL-Prefix:** `/` (konfigurierbar)

### URL-Struktur

Alle API-Endpunkte folgen diesem Muster:

```
[PREFIX]LETTER[/ZETTEL-ID]
```

- **PREFIX**: URL-Prefix (Standard: `/`)
- **LETTER**: Einzelner Buchstabe zur Angabe des Ressourcentyps
- **ZETTEL-ID**: Optional, 14-stellige Zettel-Identifikation

**Beispiele:**
```
/z                    # Alle Zettel auflisten
/z/20210903211500     # Spezifisches Zettel abrufen
/a                    # Authentifizierung
/r/20210903211500     # Referenzen eines Zettels
```

## API-Endpunkte im Überblick

| Buchstabe | Ressource | Beschreibung | Mnemonic |
|-----------|-----------|--------------|----------|
| **a** | Authentication | Authentifizierung und Token-Verwaltung | **A**uthenticate |
| **r** | References | Referenzen zwischen Zetteln | **R**eference |
| **x** | eXecute | Administrative Funktionen und Befehle | e**X**ecute |
| **z** | Zettel | Haupt-CRUD-Operationen für Zettel | **Z**ettel |

## Unterstützte HTTP-Methoden

Die API verwendet Standard-HTTP-Methoden für CRUD-Operationen:

| Methode | Verwendung |
|---------|------------|
| **GET** | Ressourcen abrufen (Read) |
| **POST** | Neue Ressourcen erstellen (Create) |
| **PUT** | Bestehende Ressourcen aktualisieren (Update) |
| **DELETE** | Ressourcen löschen (Delete) |
| **HEAD** | Metadaten abrufen |

## Datenformate

Die API unterstützt mehrere Encoding-Formate für Request/Response:

| Format | MIME-Type | Beschreibung |
|--------|-----------|--------------|
| **plain** | `text/plain` | Standard-Format: Metadaten + Inhalt getrennt durch Leerzeile |
| **data** | `application/x-sxpf` | S-Expressions (Symbolic Expressions) |
| **html** | `text/html` | HTML-Rendering |
| **zmk** | - | Zettelmarkup-Format |
| **md** | `text/markdown` | Markdown-Format |
| **text** | `text/plain` | Reiner Text |
| **sz** | - | Strukturierte S-Expression Blöcke |
| **shtml** | - | Vereinfachtes HTML |

### Format-Auswahl

Das gewünschte Format kann auf drei Arten angegeben werden (Priorität von oben nach unten):

1. **Query-Parameter:** `?enc=data`
2. **Accept-Header:** `Accept: application/x-sxpf`
3. **Content-Type-Header:** `Content-Type: application/x-sxpf`
4. **Standard:** `plain`

**Beispiele:**
```bash
# Plain-Format (Standard)
curl http://127.0.0.1:23123/z/20210903211500

# Data-Format (S-Expressions)
curl http://127.0.0.1:23123/z/20210903211500?enc=data

# HTML-Format
curl -H "Accept: text/html" http://127.0.0.1:23123/z/20210903211500
```

## Plain-Format Struktur

Das Plain-Format ist das Standardformat und strukturiert wie folgt:

```
title: Mein Zettel-Titel
role: zettel
tags: #beispiel #api
syntax: zmk
created: 20210903211500

Dies ist der Inhalt des Zettels.
Er kommt nach einer Leerzeile.
Mehrere Zeilen sind möglich.
```

**Aufbau:**
1. **Metadaten-Block:** Key-Value-Paare (ein Paar pro Zeile)
2. **Leerzeile:** Trennung zwischen Metadaten und Inhalt
3. **Inhalt-Block:** Eigentlicher Zettel-Inhalt

## Data-Format (S-Expressions)

S-Expressions sind die bevorzugte Format für programmatischen Zugriff:

```lisp
(zettel
  (id "20210903211500")
  (meta
    (title "Mein Zettel-Titel")
    (role "zettel")
    (tags "#beispiel #api"))
  (rights 15)
  (encoding "zmk")
  (content "Dies ist der Inhalt des Zettels."))
```

**Vorteile:**
- Strukturiert und maschinenlesbar
- Eindeutige Typisierung
- Einfach zu parsen
- Enthält zusätzliche Informationen (z.B. Rechte)

## Query-Parameter

Wichtige Query-Parameter für alle Endpunkte:

| Parameter | Werte | Beschreibung |
|-----------|-------|--------------|
| **enc** | plain, data, html, zmk, md, text | Encoding-Format |
| **part** | zettel, meta, content | Zettel-Teil auswählen |
| **_parseonly** | - | Nur parsen, nicht evaluieren |
| **_command** | authenticated, refresh | Befehl ausführen |

**Beispiele:**
```bash
# Nur Metadaten abrufen
curl http://127.0.0.1:23123/z/20210903211500?part=meta

# Nur Inhalt abrufen
curl http://127.0.0.1:23123/z/20210903211500?part=content

# Data-Format mit nur Metadaten
curl http://127.0.0.1:23123/z/20210903211500?enc=data&part=meta
```

## Authentifizierung

Die meisten API-Operationen erfordern Authentifizierung:

1. **Token erhalten:** `POST /a` mit Credentials
2. **Token verwenden:** `Authorization: Bearer {token}` Header
3. **Token erneuern:** `PUT /a` mit bestehendem Token

Siehe [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md) für Details.

## HTTP-Statuscodes

Die API verwendet Standard-HTTP-Statuscodes:

| Code | Bedeutung | Verwendung |
|------|-----------|------------|
| **200** | OK | Erfolgreiche GET-Anfrage |
| **201** | Created | Erfolgreiche POST-Anfrage (Ressource erstellt) |
| **204** | No Content | Erfolgreiche PUT/DELETE-Anfrage (kein Body) |
| **400** | Bad Request | Ungültige Anfrage |
| **401** | Unauthorized | Authentifizierung fehlgeschlagen oder fehlt |
| **403** | Forbidden | Keine Berechtigung für die Aktion |
| **404** | Not Found | Ressource nicht gefunden |
| **500** | Internal Server Error | Serverfehler |

## Fehlerbehandlung

Fehlerantworten folgen diesem Format:

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

## Schnellstart-Beispiel

Vollständiger Workflow mit curl:

```bash
# 1. Token erhalten
TOKEN=$(curl -s -X POST -u owner:owner http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

# 2. Neues Zettel erstellen
ZID=$(curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: API Test\ntags: #test\n\nMein erster API-Test!' \
  http://127.0.0.1:23123/z)

echo "Erstellt: Zettel $ZID"

# 3. Zettel abrufen
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/$ZID

# 4. Alle Zettel mit Tag "test" finden
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z?tags HAS test'

# 5. Zettel löschen
curl -X DELETE -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/$ZID
```

## Weitere Dokumentation

- **[02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md)** - Vollständige Authentifizierungs- und Autorisierungsdetails
- **[03-Endpunkt-Referenz.md](03-Endpunkt-Referenz.md)** - Detaillierte Beschreibung aller Endpunkte
- **[04-Code-Beispiele.md](04-Code-Beispiele.md)** - Praktische Code-Beispiele in verschiedenen Sprachen

## Implementierungsdetails

### Quellcode-Lokation

Die API-Implementierung befindet sich im Zettelstore-Repository:

```
zettelstore/internal/web/adapter/api/
├── api.go                  # Haupt-API-Struktur
├── login.go                # Authentifizierung (POST/PUT /a)
├── get_zettel.go          # Zettel abrufen (GET /z/{id})
├── create_zettel.go       # Zettel erstellen (POST /z)
├── update_zettel.go       # Zettel aktualisieren (PUT /z/{id})
├── delete_zettel.go       # Zettel löschen (DELETE /z/{id})
├── query.go               # Zettel abfragen (GET /z)
├── get_references.go      # Referenzen (GET /r/{id})
├── get_data.go            # Admin-Daten (GET /x)
├── command.go             # Befehle (POST /x)
├── request.go             # Request-Parsing
└── response.go            # Response-Writing
```

### Client-Bibliothek

Offizielle Go-Client-Bibliothek:
- **Package:** `t73f.de/r/zsc/client`
- **Link:** https://t73f.de/r/zsc

## Architektur-Hinweise

Die Zettelstore API folgt **Clean Architecture**-Prinzipien:

1. **Adapter Layer** (`internal/web/adapter/api/`) - HTTP-Handler
2. **Use Case Layer** (`internal/usecase/`) - Business-Logik
3. **Domain Layer** (`t73f.de/r/zsc/domain/`) - Domain-Modelle
4. **Infrastructure** (`internal/box/`, `internal/auth/`) - Persistence & Auth

Diese Trennung ermöglicht:
- Testbarkeit
- Erweiterbarkeit
- Wartbarkeit
- Klare Verantwortlichkeiten

## Konfiguration

Die API kann über Startup-Parameter konfiguriert werden:

```bash
zettelstore run \
  -c config.zcf \        # Konfigurationsdatei
  -p 23123 \              # Port (Standard: 23123)
  -d ./zettel \           # Zettel-Verzeichnis
  -r                      # Read-Only-Modus
```

**Wichtige Konfigurationsparameter:**
- `token-lifetime-api` - Token-Lebensdauer (Standard: 600s)
- `url-prefix` - URL-Prefix für alle Endpunkte
- `max-request-size` - Maximale Request-Größe
- `base-url` - Basis-URL für absolute URLs

## Best Practices

1. **Token-Verwaltung:** Speichere Tokens sicher und erneuere sie rechtzeitig
2. **Error Handling:** Prüfe immer HTTP-Statuscodes
3. **Encoding:** Verwende `data`-Format für programmatischen Zugriff
4. **Query-Optimierung:** Nutze Filter und LIMIT für große Datenmengen
5. **Idempotenz:** PUT und DELETE sind idempotent, POST nicht
6. **Caching:** Implementiere Client-seitiges Caching für bessere Performance

## Support und Ressourcen

- **Offizielle Dokumentation:** https://zettelstore.de/manual/
- **Lokale Dokumentation:** `zettelstore/docs/manual/`
- **Source Code:** `zettelstore/internal/web/adapter/api/`
- **Tests:** `zettelstore/tests/client/`

---

**Version:** 1.0
**Letzte Aktualisierung:** 2025-11-12
**Basierend auf:** Zettelstore Version 0.19.0-dev
