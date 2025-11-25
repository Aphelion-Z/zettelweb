# Zettelstore API - Dokumentation

Vollständige Dokumentation zur Zettelstore HTTP API mit Beispielen, Referenzen und Best Practices.

## 📚 Dokumentations-Übersicht

Diese Dokumentation umfasst alle Aspekte der Zettelstore API und ist strukturiert in vier Hauptdokumente:

### [01 - API-Übersicht](01-API-Uebersicht.md)
**Für wen:** Alle Benutzer (Einsteiger und Fortgeschrittene)

**Inhalt:**
- Grundlegende Konzepte der Zettelstore API
- URL-Struktur und Endpunkt-Muster
- Datenformate (Plain, Data, HTML, Markdown, etc.)
- HTTP-Methoden und Statuscodes
- Schnellstart-Beispiel
- Konfiguration und Deployment

**Beginne hier wenn du:**
- Neu bei der Zettelstore API bist
- Einen Überblick über die Möglichkeiten brauchst
- Die grundlegende Architektur verstehen möchtest

---

### [02 - Authentifizierung & Autorisierung](02-Authentifizierung-Autorisierung.md)
**Für wen:** Entwickler, die mit der API arbeiten

**Inhalt:**
- JWT-basierte Authentifizierung (HS512)
- Token-Management (Erhalten, Verwenden, Erneuern)
- Autorisierungs-Mechanismen und Berechtigungen
- Benutzer-Rollen und Rights-System
- Sicherheits-Best-Practices
- Troubleshooting

**Beginne hier wenn du:**
- Wissen möchtest, wie Authentifizierung funktioniert
- Tokens verwalten musst
- Berechtigungen und Zugriffskontrollen verstehen willst
- Sicherheitsfragen hast

---

### [03 - Endpunkt-Referenz](03-Endpunkt-Referenz.md)
**Für wen:** API-Entwickler und Integratoren

**Inhalt:**
- Vollständige Referenz aller API-Endpunkte
- Detaillierte Beschreibung jeder HTTP-Methode
- Request/Response-Formate mit Beispielen
- Query-Parameter und erweiterte Funktionen
- Fehlerbehandlung und Status-Codes
- Praktische curl-Beispiele für jeden Endpunkt

**Endpunkte:**
- `/a` - Authentifizierung (POST, PUT)
- `/z` - Zettel-Operationen (GET, POST, PUT, DELETE)
- `/r` - Referenzen (GET)
- `/x` - Administrative Funktionen (GET, POST)

**Beginne hier wenn du:**
- Einen bestimmten Endpunkt nachschlagen möchtest
- Technische Details zu Request/Response brauchst
- API-Integration implementierst

---

### [04 - Code-Beispiele](04-Code-Beispiele.md)
**Für wen:** Entwickler in verschiedenen Programmiersprachen

**Inhalt:**
- Vollständige Client-Implementierungen
- Praktische Verwendungsszenarien
- Best Practices und Patterns
- Fehlerbehandlung und Rate Limiting

**Sprachen:**
- Bash/Shell
- Python
- JavaScript/Node.js
- Go
- Java
- C#/.NET

**Verwendungsszenarien:**
- Automatisches Backup-System
- Zettel-Synchronisation
- Content-Migration
- Auto-Tagging

**Beginne hier wenn du:**
- Code-Beispiele in deiner Sprache suchst
- Einen funktionierenden Client implementieren möchtest
- Praktische Anwendungsbeispiele brauchst

---

## 🚀 Schnellstart

### Minimales Beispiel (curl)

```bash
# 1. Token erhalten
TOKEN=$(curl -s -X POST -u owner:owner http://127.0.0.1:23123/a | \
  grep -oP '(?<="Bearer" ")[^"]+')

# 2. Zettel erstellen
ZID=$(curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Mein Zettel\n\nInhalt hier' \
  http://127.0.0.1:23123/z)

# 3. Zettel abrufen
curl -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/z/$ZID
```

### Python-Beispiel

```python
from zettelstore_client import ZettelstoreClient

# Client initialisieren und authentifizieren
client = ZettelstoreClient()
client.authenticate("owner", "owner")

# Zettel erstellen
zid = client.create_zettel(
    "Mein Titel",
    "Mein Inhalt",
    tags="#beispiel"
)

# Zettel abrufen
content = client.get_zettel(zid)
print(content)
```

**Vollständige Implementierung:** Siehe [04-Code-Beispiele.md](04-Code-Beispiele.md)

---

## 📖 Empfohlener Lernpfad

### Für Einsteiger

1. **Start:** [01-API-Uebersicht.md](01-API-Uebersicht.md) - Grundlagen verstehen
2. **Sicherheit:** [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md) - Authentifizierung lernen
3. **Praxis:** [04-Code-Beispiele.md](04-Code-Beispiele.md) - Ersten Client implementieren
4. **Vertiefung:** [03-Endpunkt-Referenz.md](03-Endpunkt-Referenz.md) - Erweiterte Funktionen nutzen

### Für Fortgeschrittene

1. **Referenz:** [03-Endpunkt-Referenz.md](03-Endpunkt-Referenz.md) - Alle Endpunkte im Detail
2. **Code:** [04-Code-Beispiele.md](04-Code-Beispiele.md) - Fortgeschrittene Patterns
3. **Sicherheit:** [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md) - Autorisierungs-Details

---

## 🔍 Wichtige Konzepte

### API-Endpunkte

| Endpunkt | Zweck | Dokumentation |
|----------|-------|---------------|
| `/a` | Authentifizierung | [02](02-Authentifizierung-Autorisierung.md), [03](03-Endpunkt-Referenz.md#-authentifizierung-a) |
| `/z` | Zettel CRUD | [03](03-Endpunkt-Referenz.md#-zettel-operationen-z) |
| `/r` | Referenzen | [03](03-Endpunkt-Referenz.md#-referenzen-r) |
| `/x` | Administration | [03](03-Endpunkt-Referenz.md#-administrative-endpunkte-x) |

### Datenformate

| Format | Verwendung | Dokumentation |
|--------|------------|---------------|
| **plain** | Standard, menschenlesbar | [01](01-API-Uebersicht.md#plain-format-struktur) |
| **data** | S-Expressions, programmatisch | [01](01-API-Uebersicht.md#data-format-s-expressions) |
| **html** | Rendering, Anzeige | [01](01-API-Uebersicht.md#datenformate) |
| **md** | Markdown-Export | [01](01-API-Uebersicht.md#datenformate) |

---

## 💡 Häufige Aufgaben

### Zettel erstellen

```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  --data $'title: Titel\n\nInhalt' \
  http://127.0.0.1:23123/z
```

**Details:** [03-Endpunkt-Referenz.md - POST /z](03-Endpunkt-Referenz.md#post-z---neues-zettel-erstellen)

### Zettel suchen

```bash
curl -H "Authorization: Bearer $TOKEN" \
  'http://127.0.0.1:23123/z?tags HAS wichtig ORDER REVERSE created LIMIT 10'
```

**Details:** [03-Endpunkt-Referenz.md - GET /z](03-Endpunkt-Referenz.md#get-z---alle-zettel-auflistenabfragen)

### Token erneuern

```bash
curl -X PUT \
  -H "Authorization: Bearer $TOKEN" \
  http://127.0.0.1:23123/a
```

**Details:** [02-Authentifizierung-Autorisierung.md - Token Erneuern](02-Authentifizierung-Autorisierung.md#token-erneuern)

---

## 🛠️ Ressourcen

### Offizielle Dokumentation
- **Zettelstore Website:** https://zettelstore.de
- **Online-Manual:** https://zettelstore.de/manual/
- **API-Dokumentation:** https://zettelstore.de/manual/h/00001012000000

### Quellcode-Referenzen

**API-Implementierung:**
```
zettelstore/internal/web/adapter/api/
├── api.go                  # Haupt-API-Struktur
├── login.go                # Authentifizierung
├── *_zettel.go            # Zettel-Operationen
├── query.go               # Query-Handler
└── command.go             # Admin-Befehle
```

**Authentifizierung:**
```
zettelstore/internal/auth/
├── auth.go                # Interfaces
├── impl/digest.go         # JWT-Implementierung
└── policy/               # Autorisierungs-Richtlinien
```

### Client-Bibliotheken

- **Go:** `t73f.de/r/zsc/client` (offiziell)
- **Python:** Siehe [04-Code-Beispiele.md](04-Code-Beispiele.md#python)
- **JavaScript:** Siehe [04-Code-Beispiele.md](04-Code-Beispiele.md#javascriptnodejs)
- **Java:** Siehe [04-Code-Beispiele.md](04-Code-Beispiele.md#java)
- **C#:** Siehe [04-Code-Beispiele.md](04-Code-Beispiele.md#cnet)

---

## 📋 API-Übersicht (Kompakt)

### Authentifizierung
```
POST /a                         # Login (erhalte Token)
PUT  /a                         # Token erneuern
```

### Zettel
```
GET    /z                       # Liste/Query
POST   /z                       # Erstellen
GET    /z/{id}                  # Abrufen
PUT    /z/{id}                  # Aktualisieren
DELETE /z/{id}                  # Löschen
```

### Andere
```
GET  /r/{id}                    # Referenzen
GET  /x                         # Version-Info
POST /x?_command=...            # Admin-Befehle
```

**Vollständige Referenz:** [03-Endpunkt-Referenz.md](03-Endpunkt-Referenz.md)

---

## ❓ FAQ

### Wie authentifiziere ich mich?

```bash
curl -X POST -u username:password http://127.0.0.1:23123/a
```

**Siehe:** [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md#authentifizierung-token-erhalten)

### Wie verwende ich einen Token?

```bash
curl -H "Authorization: Bearer {token}" http://127.0.0.1:23123/z
```

**Siehe:** [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md#token-verwenden)

### Welches Format soll ich verwenden?

- **Menschenlesbar:** `plain` (Standard)
- **Programmatisch:** `data` (S-Expressions)
- **Export:** `md` (Markdown) oder `html`

**Siehe:** [01-API-Uebersicht.md - Datenformate](01-API-Uebersicht.md#datenformate)

### Wie suche ich Zettel?

```bash
curl 'http://127.0.0.1:23123/z?tags HAS wichtig'
```

**Query-Syntax:** [03-Endpunkt-Referenz.md - Query-Syntax](03-Endpunkt-Referenz.md#query-syntax)

### Wie gehe ich mit Fehlern um?

**Siehe:**
- [03-Endpunkt-Referenz.md - Fehlerbehandlung](03-Endpunkt-Referenz.md#-fehlerbehandlung)
- [04-Code-Beispiele.md - Best Practices](04-Code-Beispiele.md#best-practices)

---

## 🔐 Sicherheitshinweise

1. **Verwende HTTPS in Produktion** (nicht HTTP)
2. **Speichere Credentials nie im Code** (Environment-Variablen verwenden)
3. **Tokens sicher aufbewahren** (nicht in Logs oder Git)
4. **Kurze Token-Lebensdauer** für erhöhte Sicherheit
5. **Least Privilege Prinzip** anwenden

**Detaillierte Sicherheitsrichtlinien:** [02-Authentifizierung-Autorisierung.md - Sicherheitshinweise](02-Authentifizierung-Autorisierung.md#sicherheitshinweise)

---

## 📞 Support und Feedback

### Probleme oder Fragen?

1. **Dokumentation durchsuchen:** Nutze die Suchfunktion (Strg+F)
2. **Code-Beispiele prüfen:** [04-Code-Beispiele.md](04-Code-Beispiele.md)
3. **Troubleshooting:** [02-Authentifizierung-Autorisierung.md - Troubleshooting](02-Authentifizierung-Autorisierung.md#troubleshooting)

### Weitere Ressourcen

- **Zettelstore Manual:** https://zettelstore.de/manual/
- **GitHub:** https://github.com/zettelstore/zettelstore
- **Mailing List:** https://zettelstore.de/home/wiki?name=Communication

---

## 📝 Dokumentations-Informationen

- **Version:** 1.0
- **Letzte Aktualisierung:** 2025-11-12
- **Basierend auf:** Zettelstore Version 0.19.0-dev
- **Erstellt von:** Umfassende Analyse der Zettelstore-Quellcode und Dokumentation

### Dokumentations-Struktur

```
Zettelstore-API-Dokumentation/
├── README.md                                  # Diese Datei (Start hier!)
├── 01-API-Uebersicht.md                      # Grundlagen und Konzepte
├── 02-Authentifizierung-Autorisierung.md     # Security-Details
├── 03-Endpunkt-Referenz.md                   # Vollständige API-Referenz
└── 04-Code-Beispiele.md                       # Praktische Implementierungen
```

---

## 🚀 Los geht's!

**Neu bei der Zettelstore API?**
→ Beginne mit [01-API-Uebersicht.md](01-API-Uebersicht.md)

**Möchtest du sofort loslegen?**
→ Springe zu [04-Code-Beispiele.md](04-Code-Beispiele.md)

**Brauchst du eine spezifische Referenz?**
→ Schaue in [03-Endpunkt-Referenz.md](03-Endpunkt-Referenz.md)

**Hast du Authentifizierungs-Fragen?**
→ Lies [02-Authentifizierung-Autorisierung.md](02-Authentifizierung-Autorisierung.md)

---

**Viel Erfolg mit der Zettelstore API!** 🎉
