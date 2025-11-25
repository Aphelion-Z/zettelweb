# 📝 AUFGABE 1: Infrastruktur - Erklärt

**Status:** ✅ Diese Aufgabe habt ihr perfekt gelöst!

---

## 🎯 WAS WURDE VERLANGT?

Lest nochmal die Original-Aufgabe:

> **Arbeitsanweisung:**
> Damit Sie als Gruppe gemeinsam arbeiten können, benötigen Sie eine gemeinsame Ablage der zu erstellenden Software.
>
> **Aufgabe erfüllt wenn:**
> - Git-Repository eingerichtet ✓
> - Verzeichnis "zettel" erstellt ✓
> - URL im ILIAS abgegeben ✓
> - Prof. Stern hat Lesezugriff ✓

---

## 🤔 WARUM DIESE AUFGABE?

### Problem ohne Git:
Stellt euch vor 7 Leute arbeiten an einem Projekt...

**Ohne Git:**
- Person A mailt Code an Person B
- Person B ändert was, mailt zurück
- Person C hat veraltete Version
- Person D überschreibt Person A's Änderungen
- **CHAOS!** 🔥

**Mit Git:**
- Zentrale Ablage (GitHub/GitLab)
- Jeder zieht neueste Version (`git pull`)
- Jeder macht Änderungen (`git commit`)
- Jeder schickt Änderungen hoch (`git push`)
- Git merged automatisch (meist!)
- **ORDNUNG!** ✅

### Warum "zettel" Ordner?
- Später: Zettelstore speichert dort Zettel
- Jetzt schon erstellen → zeigt dass ihr vorbereitet seid

---

## ✅ WAS IHR GEMACHT HABT

**Euer Repository:**
- URL: https://github.com/Aphelion-Z/zettelweb
- Typ: Private Repository
- Platform: GitHub
- Owner: Aphelion-Z

**Zettel-Ordner:**
- Pfad: `/zettel/`
- Inhalt: `.gitkeep` (damit Git den leeren Ordner trackt)

**Team-Zugriff:**
- Alle 7 Gruppenmitglieder haben Zugriff
- Prof. Stern hat Lesezugriff (für Bewertung)

**Bewertung:** **Perfekt erfüllt!** 🎉

---

## 📚 WAS LERNT IHR DARAUS?

### Git Basics (Wiederholung):

**Repository (Repo):**
- Ordner der mit Git versioniert wird
- Enthält `.git/` Verzeichnis (Git-Metadaten)
- Kann lokal (auf eurem PC) oder remote (GitHub) sein

**Wichtigste Git-Befehle:**
```bash
git clone <url>        # Repo runterladen
git pull               # Neueste Änderungen holen
git add <file>         # Datei für Commit vorbereiten
git commit -m "..."    # Änderungen speichern (lokal)
git push               # Änderungen hochladen (remote)
```

**Workflow:**
1. Morgens: `git pull` (neueste Version holen)
2. Arbeiten: Code schreiben
3. Zwischendurch: `git add .` + `git commit -m "Feature X"`
4. Abends: `git push` (Änderungen teilen)

### GitHub vs GitLab vs Codeberg:

| Platform | Pro | Contra |
|----------|-----|--------|
| **GitHub** | Bekannteste, viele Features | Microsoft-owned |
| **GitLab** | Selbst-hostbar, CI/CD | Komplexer |
| **Codeberg** | Open-Source, Europa | Weniger bekannt |

**Ihr habt GitHub gewählt:** ✓ Gute Wahl (am weitesten verbreitet)

### Public vs Private Repository:

**Public:**
- ✅ Jeder kann Code sehen
- ✅ Open-Source-Lizenz wählbar
- ❌ Projekt muss öffentlich sein

**Private:**
- ✅ Nur Teammitglieder sehen Code
- ✅ Gut für Uni-Projekte
- ⚠️ Prof braucht expliziten Zugriff

**Ihr habt Private gewählt:** ✓ Sinnvoll für Uni-Projekt

---

## 🎓 WIE HÄTTE ICH DAS MACHEN SOLLEN?

**Schritt-für-Schritt (falls ihr es wiederholen müsstet):**

### Schritt 1: Repository erstellen

**Option A: GitHub Web-Interface**
1. Auf github.com einloggen
2. "New repository" klicken
3. Name: `zettelweb` (oder beliebig)
4. Beschreibung: "ZettelWeb - Gruppe 7 - SWT Projekt"
5. **Private** auswählen
6. "Initialize with README" ✓ (ankreuzen)
7. "Create repository"

**Option B: GitHub CLI (für Profis)**
```bash
gh repo create zettelweb --private --clone
```

### Schritt 2: Zettel-Ordner erstellen

**Lokal auf eurem PC:**
```bash
cd zettelweb
mkdir zettel
touch zettel/.gitkeep
git add zettel/.gitkeep
git commit -m "Add zettel directory"
git push
```

**Warum `.gitkeep`?**
- Git trackt keine leeren Ordner
- `.gitkeep` = Dummy-Datei damit Git den Ordner sieht
- Name ist Konvention (könnte auch `.placeholder` heißen)

### Schritt 3: Team-Mitglieder einladen

1. GitHub Repo öffnen
2. "Settings" → "Collaborators"
3. "Add people"
4. Benutzernamen eingeben
5. Rolle wählen: "Write" (können committen)
6. Für Prof: "Read" (nur lesen)

### Schritt 4: URL abgeben

1. URL kopieren: `https://github.com/username/zettelweb`
2. In ILIAS einfügen
3. Abgeben

**Fertig!** ✅

---

## 💡 PRO-TIPPS

### Tipp 1: README.md sofort erstellen
Beim ersten Commit schon README mit Infos:
- Projekt-Name
- Kurzbeschreibung
- Team-Mitglieder

### Tipp 2: .gitignore erstellen
Dateien die NICHT ins Repo sollen:
```gitignore
# Build-Artefakte
*.exe
*.o
build/

# IDE-Settings
.vscode/
.idea/

# OS-Dateien
.DS_Store
Thumbs.db

# Secrets!
.env
credentials.json
```

### Tipp 3: Branch-Strategie überlegen
Später sinnvoll:
- `main` = stabile Version
- `dev` = Entwicklung
- `feature/zettel-drag-drop` = einzelne Features

### Tipp 4: Commit-Messages
**Schlecht:**
- "asdf"
- "fix"
- "stuff"

**Gut:**
- "Add drag-and-drop for Zettel"
- "Fix bug in position saving"
- "Update README with setup instructions"

**Format:**
```
[Type] Short description

Longer explanation if needed.

Fixes #42
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`

---

## 🧪 ÜBUNG

**Aufgabe:** Erstellt ein Test-Repository (lokal)

```bash
mkdir test-repo
cd test-repo
git init
echo "# Test" > README.md
git add README.md
git commit -m "Initial commit"
git log
```

**Was lernt ihr:**
- Wie man ein Repo erstellt (`git init`)
- Wie man committed
- Wie man Historie sieht (`git log`)

---

## ✅ CHECKLISTE

Habt ihr verstanden:
- [ ] Warum man Git braucht? (Teamarbeit)
- [ ] Was ein Repository ist?
- [ ] Wie man ein Repo erstellt?
- [ ] Wie man Team-Mitglieder einlädt?
- [ ] Warum `.gitkeep` für leere Ordner?
- [ ] Basic Git-Befehle (`clone`, `pull`, `add`, `commit`, `push`)?

**Alle ✅?** Dann weiter zu Aufgabe 2!

---

## ➡️ NÄCHSTER SCHRITT

**Weiter zu:** `02-Projektauftrag-ERKLAERT.md`

Dort geht's um euren README/Projektauftrag!
