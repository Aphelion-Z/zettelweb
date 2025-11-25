ADR: Wahl von SQLite als DBMS für Zettelweb

Situation:
Für unser Projekt Zettelweb, müssen wir uns für ein Datenbankmanagementsystem entscheiden.
Die Datenbank soll Zettel, Positionen, Verbindungen und Metadaten speichern.
Wir benötigen eine einfach zu implementierende und zuverlässige Datenbank, 
welche die Anforderungen in der Entwicklung- und Testphase erfüllt.



Bewertungskriterien:
1. Einfache Einrichtung und Wartung
2. Kompatibilität
3. Sicherheit und Zuverlässigkeit
4. Kosten
5. Performance für lokale Nutzung
6. Portabilität

Alternativen:
1. SQLite
2. MySQL
3. PostgreSQL

Bewertung:

Einfache Einrichtung und Wartung: SQLite lässt sich direkt in die Anwendung einbinden, benötigt keinen separaten Server und erfordert keine Benutzerverwaltung. Backups können durch Kopieren der Datenbankdatei erstellt werden. PostgreSQL und MySQL brauchen dagegen Installation eines Datenbankservers, Konfiguration von Benutzerkonten und Verwaltungsaufwand für Backups.
Kompatibilität: Alle drei Systeme unterstützen die gängigen Programmiersprachen. SQLite lässt sich direkt einbinden und benötigt keine Anpassungen an den Technologie-Stack. PostgreSQL und MySQL sind auch kompatibel, erfordern aber eine Netzwerkverbindung zum Server.
Sicherheit und Zuverlässigkeit: SQLite bietet einfache, sichere Speicherung. PostgreSQL und MySQL können mehrere Benutzer zugriff erlauben, ohne dass Daten verloren gehen.
Kosten: SQLite ist kostenfrei und benötigt keine Lizenzrechte. PostgreSQL ist Open Source und ebenfalls kostenfrei, erfordert aber Serverbetrieb. MySQL kann kostenfrei genutzt werden.
Performance für lokale Nutzung: SQLite zeigt bei lokalem Einzelbenutzerbetrieb hohe Performance, da keine Netzwerkverbindung notwendig ist. PostgreSQL und MySQL bieten ebenfalls gute Performance.
Portabilität: SQLite speichert alle Daten in einer einzelnen Datei, die leicht verschoben und gesichert werden kann. PostgreSQL und MySQL speichern Daten serverbasiert, dadurch wird die Portabilität eingeschränkt.


Entscheidung:
Nach ausführlicher Analyse der Optionen haben wir uns für SQLite entschieden.

Begründung:
SQLite ist eine dateibasierte Datenbank, welche direkt in der Anwendung eingebettet wird und keine separate Installation benötigt.
SQLite ist ideal für kleine Projekte und lokale Anwendungen und verbraucht wenig Speicher sowie Ressourcen.
SQLite bietet eine einfache Einrichtung und Wartung durch eine direkte Einbindung in die Anwendung.
SQLite vielen Betriebssystemen und Programmiersprachen kompatibel. 
Die Datenbankdateien sind portabel, lassen sich problemlos sichern und transportieren.
Durch die Unabhängigkeit zu separaten Servern ist SQLite weitestgehend ausfallsicher.
SQLite ist kostenlos und Lizenzfrei erhältlich.
	

Konsequenzen:

Positive Auswirkungen:
Durch unsere Entscheidung haben wir eine einfache Einrichtung, wodurch wir keinen separaten Server benötigen.
Da die Datenbank in einer Datei liegt, sind Tests und Backups einfach.
Durch minimales Setup wird schnell mit der Entwicklung begonnen.

Negative Auswirkungen:
Bei Mehrbenutzerbetrieb wird ein Umstieg auf eine Serverbasierte Datenbank benötigt.
Online Backups sind nicht möglich.
