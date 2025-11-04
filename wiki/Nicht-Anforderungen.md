# Nicht-Anforderungen (Out of Scope)

**Projekt:** ZettelWeb
**Version:** 2.0
**Datum:** 2025-11-04

---

## 🚫 Was ZettelWeb NICHT ist

Diese Nicht-Anforderungen definieren explizit, **was NICHT Teil des Projekts ist**, um Scope-Creep zu vermeiden und den Fokus auf die Kern-Funktionalität (Graph-Visualisierung) zu bewahren.

---

## 1. Kollaboration & Multi-User-Features 🚫

**Nicht enthalten:**
- Echtzeit-Kollaboration (mehrere Nutzer gleichzeitig)
- User-Management (Registrierung, Login, Passwörter)
- Gemeinsame Graph-Sessions
- Kommentare/Diskussionen zwischen Nutzern
- Permissions (wer darf was sehen/ändern)

**Begründung:**
- Würde Backend-Infrastruktur (Server, Authentifizierung, WebSockets) erfordern
- Komplexität würde Projekt-Umfang sprengen (zusätzlich +30 Story Points)
- LocalStorage-basierte Lösung unterstützt nur Single-User
- Nicht Teil der Kern-Vision (persönliches Wissensmanagement)

**Zukunft:**
Falls später benötigt: Separate Backend-Komponente mit User-DB und Session-Management erforderlich.

---

## 2. Cloud-Speicherung & Geräte-Synchronisierung 🚫

**Nicht enthalten:**
- Cloud-Backup von Positionen/State
- Synchronisierung zwischen Desktop, Laptop, Tablet
- "Arbeite überall weiter"-Feature
- Automatisches Backup in Cloud-Storage (Dropbox, Google Drive, etc.)

**Begründung:**
- LocalStorage ist geräte-/browser-spezifisch (nicht sync-bar)
- Cloud-Integration würde Account-System erfordern
- Datenschutz-Probleme (wo liegen Nutzer-Daten?)
- Alternative: Nutzer kann Zettelstore selbst synchronisieren (Zettel-Inhalte), Positionen sind lokal

**Zukunft:**
Export/Import-Feature für Positionen könnte manuelle Übertragung ermöglichen (aber nicht in v1.0).

---

## 3. Zettel-Inhalte Bearbeiten ✏️🚫

**WICHTIG: Read-Only Visualisierung!**

**Nicht enthalten:**
- Zettel erstellen/löschen über ZettelWeb
- Zettel-Text bearbeiten
- Tags hinzufügen/entfernen über ZettelWeb
- Metadaten (Autor, Datum, etc.) ändern
- Verknüpfungen zwischen Zetteln erstellen/löschen

**Begründung:**
- **Zettelstore ist die "Single Source of Truth"** für Inhalte
- Duplikation der Bearbeitungs-Logik wäre komplex und fehleranfällig
- Zettelstore hat bereits perfekte Editor-UI
- ZettelWeb = Visualisierungs-Werkzeug, nicht Zettelkasten-Editor
- Scope-Fokus: Graph-Darstellung, nicht Content-Management

**Workflow:**
```
1. Zettel bearbeiten: Zettelstore Web-UI nutzen
2. ZettelWeb neu laden: Änderungen werden automatisch übernommen
```

**Zukunft:**
Quick-Edit-Button, der Zettelstore-Editor öffnet, wäre denkbar (aber nicht in MVP).

---

## 4. Export & Import in andere Formate 🚫

**Nicht enthalten:**
- Export als GraphML, GEXF, JSON (für Gephi, Cytoscape, etc.)
- Export als Bild (PNG, SVG, PDF)
- Import von externen Graph-Daten
- "Share Graph"-Feature (Link teilen)

**Begründung:**
- Primär-Ziel: Interaktive Exploration, nicht statische Dokumentation
- Export-Features würden Komplexität erhöhen (zusätzliche Libraries)
- Nutzer kann Screenshots machen (Browser-Feature)
- Zettelstore selbst bietet Export-Optionen für Inhalte

**Zukunft:**
SVG-Export für Präsentationen könnte sinnvoll sein (Phase 4+).

---

## 5. Alternative/Erweiterte Visualisierungen 🚫

**Nicht enthalten:**
- 3D-Graph (Three.js, WebGL)
- Timeline-Ansicht (chronologische Darstellung)
- Tree-Layout (hierarchische Darstellung)
- Matrix-Ansicht (Adjacency Matrix)
- Heatmaps (Aktivität, Verbindungsdichte)
- Mind-Map-Layout (radiale Anordnung)

**Begründung:**
- Force-Directed Layout ist die Kern-Visualisierung
- Andere Layouts würden jeweils eigene Logik/UI erfordern
- 3D ist visuell beeindruckend, aber schlecht navigierbar (UX-Problem)
- Fokus: Eine Visualisierung perfekt machen, nicht viele mittelmäßig

**Zukunft:**
Timeline oder Hierarchie als separate Views könnte interessant sein (separates Projekt).

---

## 6. UI-Anpassungen & Themes 🎨🚫

**Nicht enthalten:**
- Dark/Light Mode (Theme-Switcher)
- Farbschema-Auswahl (verschiedene Paletten)
- **Schriftarten ändern** (bereits in v1.0 erwähnt)
- **Schriftgröße ändern** (bereits in v1.0 erwähnt)
- Icon-Sets
- Layout-Varianten (Sidebar links/rechts)
- Custom CSS

**Begründung:**
- Standard-Design ist klar und funktional
- Themes würden CSS-Architektur verkomplizieren
- Accessibility besser über Browser-Zoom (eingebaute Funktion)
- Zeit besser in Kern-Features investieren
- Visuelle Anpassungen (Knotenfarbe, Liniendicke) sind in NFR-7 abgedeckt

**Zukunft:**
Basic Dark Mode könnte schnell implementiert werden (CSS-Variablen), aber nicht prioritär.

---

## 7. Mobile-App & Touch-Optimierung 📱🚫

**Nicht enthalten:**
- Native iOS/Android-App
- Responsive Layout für Smartphones
- Touch-Gesten (Pinch-to-Zoom, Swipe)
- Mobile-First Design
- Progressive Web App (PWA)

**Begründung:**
- Primäres Use-Case: Desktop-Nutzung (Wissensarbeit)
- Touch-Interaktion für komplexe Graphen schwierig (Präzision fehlt)
- Kleine Screens ungeeignet für 200+ Zettel
- Tablet-Nutzung möglicherweise funktionsfähig, aber nicht getestet/optimiert
- Team-Skills: Desktop-Webentwicklung, nicht Mobile

**Hinweis:**
App läuft **technisch** auf Tablets (Browser), aber UI ist nicht optimiert.

**Zukunft:**
PWA + Touch-Support könnte in separatem Sprint ergänzt werden.

---

## 8. Offline-Modus 🚫

**Nicht enthalten:**
- Funktionsfähigkeit ohne Zettelstore-Verbindung
- Service Worker für Offline-Caching
- "Kein Internet"-Fallback mit gecachten Daten
- Lokale Kopie aller Zettel

**Begründung:**
- ZettelWeb ist **abhängig von Zettelstore-API** (Server muss laufen)
- Offline-Fähigkeit würde vollständige Datensynchronisierung erfordern
- Komplexität: Conflict Resolution bei Änderungen
- Use-Case: Zettelstore läuft lokal (localhost) → keine Internet-Verbindung nötig

**Klarstellung:**
```
Zettelstore läuft auf localhost → ZettelWeb funktioniert ohne Internet ✅
Zettelstore ist remote → ZettelWeb braucht Netzwerk ✅
Zettelstore offline → ZettelWeb funktioniert NICHT ❌
```

**Zukunft:**
Read-Only Offline-Mode mit Service Worker möglich, aber geringer Nutzen.

---

## 9. Authentifizierung & Zugriffskontrolle 🔒🚫

**Nicht enthalten:**
- Login/Logout
- User-Accounts
- Passwort-Verwaltung
- OAuth/SSO-Integration
- Rollen & Permissions (Admin, Editor, Viewer)
- Zugriffsbeschränkungen für einzelne Zettel
- Audit-Log (wer hat was geändert)

**Begründung:**
- Zettelstore selbst hat optional Basic Auth → ausreichend
- ZettelWeb ist Frontend-Only (kein User-Management)
- Zusätzliche Auth-Schicht würde Backend erfordern
- Use-Case: Persönliches Tool, nicht Unternehmens-Software

**Sicherheitsmodell:**
```
Zettelstore mit Basic Auth → Browser-basierte Authentifizierung
ZettelWeb lädt dann Daten via authenticated requests
```

**Zukunft:**
Wenn Multi-User gewünscht: Komplett neues Backend-System erforderlich.

---

## 10. Erweiterte Algorithmen & KI-Features 🤖🚫

**Nicht enthalten:**
- Alternative Layout-Algorithmen (Hierarchical, Circular, Radial)
- Automatische Cluster-Erkennung (Machine Learning)
- Ähnlichkeits-Analyse (NLP auf Zettel-Inhalten)
- Empfehlungssystem ("Diese Zettel könnten zusammenhängen")
- Automatisches Tagging (KI-basiert)
- Graph-Analyse-Metriken (Betweenness, Centrality, etc.)

**Begründung:**
- Force-Directed Layout (D3.js) ist ausreichend und bewährt
- ML/NLP würde Backend-Prozessing erfordern (sehr komplex)
- Graph-Analyse-Bibliotheken (NetworkX, etc.) sind Python/Backend
- Scope-Fokus: Visualisierung vorhandener Struktur, nicht Struktur-Erkennung
- Student-Projekt: Realistische Komplexität wahren

**Was stattdessen implementiert ist:**
- Manuelle Tag-basierte Filterung (nutzer-kontrolliert)
- Hover-Highlighting für direkte Nachbarn (einfache Traversierung)

**Zukunft:**
Graph-Metriken könnten interessantes Feature sein (Zettel-Wichtigkeit visualisieren), aber sehr aufwändig.

---

## ✅ Was ZettelWeb STATTDESSEN ist

**Fokus auf Kern-Kompetenz:**
- 🎯 **Force-Directed Graph-Visualisierung** (Physik-basiert, smooth)
- 🎯 **Interaktive Exploration** (Click, Drag, Zoom, Pan)
- 🎯 **Tag-basierte Filterung** (mit semi-transparenten Verbindungen)
- 🎯 **Persistente Positionen** (LocalStorage)
- 🎯 **Performant** (200+ Zettel @ 30fps)

**Klare Abgrenzung:**
```
ZettelWeb ≠ Zettelkasten-Editor
ZettelWeb ≠ Kollaborations-Tool
ZettelWeb ≠ Knowledge-Management-Suite

ZettelWeb = Visualisierungs-Extension für Zettelstore
```

---

## 📋 Scope-Management im Projekt

**Bei neuen Feature-Wünschen:**

1. **Prüfen:** Ist es Teil der 11 User Stories? → JA: Implementieren
2. **Prüfen:** Ist es eine Nicht-Anforderung? → JA: Ablehnen mit Verweis auf dieses Dokument
3. **Prüfen:** Ist es Must/Should/Nice? → Nice + Zeitüberschreitung → Verschieben auf v2.0

**Beispiel-Ablauf:**
```
Team-Mitglied: "Können wir einen Dark Mode einbauen?"
→ Prüfung: Nicht-Anforderung #6
→ Antwort: "Nicht in v1.0, siehe Nicht-Anforderungen.md #6.
   Falls Zeit in Phase 3: Nice-to-Have."
```

---

**Siehe auch:**
- [REQUIREMENTS.md](../REQUIREMENTS.md) - Vollständige Requirements
- [Funktionale-Anforderungen.md](Funktionale-Anforderungen.md) - Was ZettelWeb IST
- [Nicht-Funktionale-Anforderungen.md](Nicht-Funktionale-Anforderungen.md) - Qualitätsanforderungen
