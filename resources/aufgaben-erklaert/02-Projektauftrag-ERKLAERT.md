# 📝 AUFGABE 2: Projektauftrag - Erklärt

**Status:** ⚠️ Grundstruktur gut, aber ausbaufähig

---

## 🎯 WAS WURDE VERLANGT?

Lest nochmal die Original-Aufgabe:

> **Arbeitsanweisung:**
> Aus dem Fach "Einführung in das Projektmanagement" (WIN2) kennen Sie den Aufbau eines Projektauftrags.
>
> Erstellen Sie den Projektauftrag als README Ihres Git-Projekts.
>
> **Aufgabe erfüllt wenn:**
> - README existiert ✓
> - Struktur aus Projektmanagement ✓
> - Sofort einsehbar beim Öffnen ✓

---

## 🤔 WARUM DIESE AUFGABE?

### Was ist ein Projektauftrag?

**Einfach gesagt:** Ein Dokument das **alle** wichtigen Projekt-Infos enthält.

**Zweck:**
1. **Für das Team:** Alle wissen worum es geht
2. **Für Externe:** Schneller Überblick
3. **Für später:** Nachschlagen von Entscheidungen
4. **Für den Auftraggeber:** Bestätigung dass ihr es verstanden habt

**Analogie Hausbau:**
- Projektauftrag = Vertrag mit Bauherr
- Enthält: Was wird gebaut? Wann? Wer? Wie viel kostet es?

### Warum als README.md?

**README = erste Datei die man sieht**
- Jeder GitHub-User sieht sie sofort
- Markdown-Format = leicht lesbar
- Wie die "Homepage" eures Repos

---

## ✅ WAS IHR GEMACHT HABT

**Euer README.md enthält:**

```markdown
Projektauftrag

Projektname: „ZettelWeb" Gruppe 7

Kurzbeschreibung: [...]

Ziele:
1. Gruppierung [...]
2. Visualisierung [...]
3. Positionsspeicherung [...]
4. Speicherung der Eigenschaften [...]
5. Intuitive Bedienung [...]
6. Benutzerfreundlichkeit & Übersichtlichkeit [...]

Personal- und Zeitaufwand: 7 Personen und das Semester (125 Stunden)

Meilensteine:
1. Anforderungsanalyse & Konzeption
2. Architektur- und UI-Design
3. Grundfunktionalität des Zettel-Netzes
4. Datenmanagement
5. Erweiterte Nutzerfunktionen
6. Qualitätssicherung & Feinschliff
7. Projektabschluss & Präsentation

Risikoreflexion:
1. Missverständnisse [...]
2. Datenverlust [...]
3. Verzögerung [...]

Unterschriften: [7 Team-Mitglieder]
```

**Was GUT ist:** ✅
- Struktur vorhanden
- Alle Basis-Elemente da
- Ziele sind konkret
- Team-Mitglieder genannt

**Was FEHLT:** ⚠️
- Projekthintergrund/Kontext
- Erfolgskriterien
- Konkrete Deadlines bei Meilensteinen
- Gegenmaßnahmen bei Risiken

---

## 📚 WAS IST EIN VOLLSTÄNDIGER PROJEKTAUFTRAG?

### Pflicht-Inhalte (aus Projektmanagement WIN2):

#### 1. Projekttitel & Kontext
**Was:** Name + Warum gibt es das Projekt?

**Beispiel:**
```markdown
# ZettelWeb - Visualisierung für Zettelkasten

## Kontext
Im Rahmen der Vorlesung "Softwaretechnik und mobile Systeme" (WIN3)
soll eine Web-Anwendung entwickelt werden, die mit dem Zettelstore
interagiert und Zettel grafisch visualisiert.

## Auftraggeber
Prof. Dr. Detlef Stern, HS Heilbronn
```

**Bei euch:** ⚠️ Kontext fehlt ("Warum machen wir das?")

#### 2. Projektziele (SMART!)
**Was:** Was soll erreicht werden?

**SMART-Kriterien:**
- **S**pecific: Konkret
- **M**easurable: Messbar
- **A**chievable: Erreichbar
- **R**elevant: Sinnvoll
- **T**ime-bound: Zeitrahmen

**Beispiel:**
```markdown
## Ziele

### Hauptziel
Eine Web-Anwendung die Zettel aus Zettelstore als verschiebbares
Netzwerk visualisiert und Positionen persistent speichert.

### Teilziele
1. Grafische Darstellung von mind. 200 Zetteln (bis Meilenstein 3)
2. Drag & Drop für Zettel-Positionierung (bis Meilenstein 3)
3. Persistente Speicherung in SQLite (bis Meilenstein 4)
4. Performance: 30fps bei 200 Zetteln (bis Meilenstein 6)
```

**Bei euch:** ✅ Ziele sind da, aber nicht zeitgebunden

#### 3. Team & Rollen
**Was:** Wer macht mit? Wer macht was?

**Beispiel:**
```markdown
## Team (7 Personen)

| Name | Rolle | Hauptverantwortung |
|------|-------|-------------------|
| Heinrich Sprachmann | Product Owner | Requirements, Koordination |
| Michael Nowizki | Frontend Lead | UI/UX, HTML/CSS |
| Michael Kundoch | Backend Lead | API, Datenbank |
| Artur Grossu | Developer | Drag & Drop Features |
| ... | ... | ... |
```

**Bei euch:** ⚠️ Namen da, aber keine Rollen/Verantwortlichkeiten

#### 4. Zeitplan & Meilensteine
**Was:** Wann wird was fertig?

**Beispiel:**
```markdown
## Zeitplan

Semester: WiSe 2025/26 (10/2025 - 01/2026)
Gesamtaufwand: 125 Stunden pro Person (7 Personen)

### Meilensteine

| # | Meilenstein | Deadline | Deliverables |
|---|-------------|----------|--------------|
| 1 | Requirements | 20.10.25 | Issues, Wiki |
| 2 | Architektur | 03.11.25 | ADRs, Diagramme |
| 3 | MVP | 17.11.25 | Basis-Visualisierung |
| 4 | Datenbank | 01.12.25 | SQLite-Integration |
| 5 | Features | 15.12.25 | Alle User Stories |
| 6 | QA | 08.01.26 | Tests, Bugfixes |
| 7 | Abschluss | 22.01.26 | Präsentation |
```

**Bei euch:** ⚠️ Meilensteine ohne Deadlines

#### 5. Ressourcen & Budget
**Was:** Welche Mittel stehen zur Verfügung?

**Beispiel:**
```markdown
## Ressourcen

### Personal
7 Studierende à 125h = 875 Personenstunden

### Technologie (alle kostenfrei)
- Git/GitHub (Version Control)
- Zettelstore (Server)
- VS Code (IDE)
- Browser (Testing)

### Infrastruktur
- GitHub Repository (Cloud)
- Lokale Entwicklung (eigene PCs)
- Optional: Deployment auf Hochschul-Server

### Budget
Projekt ohne Budget (Uni-Kontext)
```

**Bei euch:** ❌ Fehlt komplett

#### 6. Erfolgskriterien
**Was:** Wann ist das Projekt erfolgreich?

**Beispiel:**
```markdown
## Erfolgskriterien

### Must-Have (zum Bestehen)
- [ ] Alle funktionalen Anforderungen (Issues) umgesetzt
- [ ] Architektur dokumentiert und eingehalten
- [ ] Code lauffähig und demonstrierbar
- [ ] Performance-Ziele erreicht (200 Zettel, 30fps)

### Nice-to-Have
- [ ] Erweiterte Features (Zoom, Pan, Filter)
- [ ] Tests (Unit, Integration)
- [ ] Deployment online
```

**Bei euch:** ❌ Fehlt komplett

#### 7. Risiken & Gegenmaßnahmen
**Was:** Was könnte schiefgehen? Was tun wir dagegen?

**Beispiel:**
```markdown
## Risiken

| Risiko | Wahrscheinlichkeit | Impact | Gegenmaßnahme |
|--------|-------------------|--------|---------------|
| Team-Mitglied fällt aus | Mittel | Hoch | Pair Programming, Wissenstransfer |
| Technische Probleme | Hoch | Mittel | Früh Prototyp, regelmäßig testen |
| Zeitverzug | Hoch | Hoch | MVP-Ansatz, Priorisierung |
| API-Änderungen | Niedrig | Mittel | Zettelstore-Version fixieren |
```

**Bei euch:** ⚠️ Risiken genannt, aber keine Gegenmaßnahmen

#### 8. Stakeholder
**Was:** Wer ist beteiligt/betroffen?

**Beispiel:**
```markdown
## Stakeholder

| Stakeholder | Rolle | Interesse | Einfluss |
|-------------|-------|-----------|----------|
| Prof. Stern | Auftraggeber | Bewertung | Hoch |
| Team | Entwickler | Note, Lernen | Hoch |
| Andere Studierende | Potenzielle Nutzer | Demo | Niedrig |
```

**Bei euch:** ❌ Fehlt komplett

---

## 🎓 WIE HÄTTE ICH DAS MACHEN SOLLEN?

### Schritt 1: Vorlage aus WIN2 anschauen
- Habt ihr die Folien/Skript aus Projektmanagement?
- Dort steht die Struktur

### Schritt 2: Brainstorming im Team
- Gemeinsam durchgehen: Was gehört rein?
- Jeder schreibt einen Teil

### Schritt 3: README strukturieren
```markdown
# Projektauftrag: ZettelWeb

## 1. Projekttitel & Kontext
[...]

## 2. Projektziele
[...]

## 3. Team & Rollen
[...]

## 4. Zeitplan & Meilensteine
[...]

## 5. Ressourcen & Budget
[...]

## 6. Erfolgskriterien
[...]

## 7. Risiken & Gegenmaßnahmen
[...]

## 8. Stakeholder
[...]

## 9. Unterschriften
[...]
```

### Schritt 4: Inhalt ausformulieren
- Konkret schreiben (nicht "irgendwann" sondern "20.11.25")
- SMART-Kriterien beachten
- Realistisch bleiben

### Schritt 5: Review
- Gegenseitig lesen
- Ist alles verständlich?
- Fehlt was?

---

## 💡 VERBESSERUNGSVORSCHLÄGE FÜR EUER README

### Sofort machen:
1. **Kontext hinzufügen**
   ```markdown
   ## Kontext
   Dieses Projekt entsteht im Rahmen der Vorlesung
   "Softwaretechnik und mobile Systeme" (WIN3, WiSe 25/26).
   Ziel ist die praktische Anwendung von SE-Methoden.
   ```

2. **Deadlines zu Meilensteinen**
   ```markdown
   1. Anforderungsanalyse & Konzeption (20.10.25)
   2. Architektur- und UI-Design (03.11.25)
   ...
   ```

3. **Gegenmaßnahmen bei Risiken**
   ```markdown
   1. Missverständnisse
      → Gegenmaßnahme: Wöchentliche Meetings, klare Aufgabenverteilung
   ```

### Nice-to-Have:
4. **Erfolgskriterien-Abschnitt**
5. **Stakeholder-Tabelle**
6. **Rollen im Team**

---

## ✅ CHECKLISTE

Habt ihr verstanden:
- [ ] Was ein Projektauftrag ist? (Zweck?)
- [ ] Welche 8 Elemente rein gehören?
- [ ] Was SMART-Kriterien sind?
- [ ] Was in eurem README fehlt?
- [ ] Wie ihr es verbessern würdet?

**Alle ✅?** Dann weiter zu Aufgabe 3!

---

## ➡️ NÄCHSTER SCHRITT

**Weiter zu:** `03-Anforderungsanalyse-ERKLAERT.md`

Dort geht's um eure User Stories und Issues!
