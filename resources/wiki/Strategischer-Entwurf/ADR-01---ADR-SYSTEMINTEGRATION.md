ADR SYSTEMINTEGRATION

Integration mit Zettelstore

Situation:

ZettelWeb benötigt Zugriff auf Zettel-Daten, die in Zettelstore gespeichert sind. Gleichzeitig
müssen zusätzliche Daten (Positionen, Verbindungen) gespeichert werden, die Zettelstore nicht verwaltet. Es muss entschieden werden, wie ZettelWeb mit Zettelstore zusammenarbeitet.

Bewertungskriterien:
  - Entwicklungsaufwand: Wie viel Arbeit ist nötig?
  - Wartbarkeit: Wie leicht sind Änderungen möglich?
  - Unabhängigkeit: Können ZettelWeb und Zettelstore getrennt entwickelt werden?
  - Kompatibilität: Funktioniert es mit der bestehenden Zettelstore-Version?

Alternativen:
Alternative A: Eigenständige Webanwendung
  ZettelWeb ist eine separate Anwendung, die:
  - Die Zettelstore REST-API nutzt, um Zettel-Daten abzurufen
  - Eine eigene Datenbank für Positions- und Verbindungsdaten verwendet
  - Im Browser als JavaScript-Anwendung läuft

Vorteile:
  - Keine Änderungen am Zettelstore-Code nötig
  - Frontend-Technologie frei wählbar
  - Unabhängige Entwicklung möglich
  - Zettelstore-Updates beeinflussen ZettelWeb nicht

Nachteile:
  - Zusätzliche Datenbank für Positions-Daten nötig
  - API-Calls verursachen Netzwerk-Latenz
  - Daten sind auf zwei Systeme verteilt

 Alternative B: Zettelstore-Erweiterung
  ZettelWeb wird als Plugin/Extension in Zettelstore integriert:
  - Erweitert Zettelstore um neue Views
  - Nutzt dieselbe Datenbank
  - Go-Code wird in Zettelstore integriert

Vorteile:
  - Alle Daten in einer Datenbank
  - Keine API-Calls, direkter Datenzugriff
  - Tighter Integration

Nachteile:
  - Zettelstore-Code muss geändert werden
  - Go-Kenntnisse erforderlich
  - Abhängig von Zettelstore-Releases
  - Höherer Entwicklungsaufwand

Bewertung der Alternativen
Entwicklungsaufwand:
•⁠  ⁠Alternative A (Eigenständige Webanwendung): niedrig, da nur Frontend entwickelt werden muss.
-Alternative B (Zettelstore-Erweiterung): hoch, da sowohl Go-Backend als auch Frontend implementiert werden müssen.

Wartbarkeit:
-Alternative A: gut, da die Codebases getrennt sind und Änderungen unabhängig voneinander erfolgen können.
-Alternative B: mittel, da die Codebases gemeinsam sind und Änderungen am Zettelstore Einfluss auf ZettelWeb haben können.

Unabhängigkeit:
-Alternative A: hoch, da ZettelWeb unabhängig vom Zettelstore entwickelt und deployed werden kann.
-Alternative B: niedrig, da ZettelWeb direkt in den Zettelstore integriert ist und von seinen Releases abhängt.

Kompatibilität:
-Alternative A: hoch, da nur die bestehende REST-API genutzt wird und Zettelstore selbst unverändert bleibt.
-Alternative B: mittel, da Änderungen am Zettelstore-Code notwendig sind und künftige Versionen berücksichtigt werden müssen.

Entscheidung:
Wir wählen Alternative A: Eigenständige Webanwendung

Begründung:
Die eigenständige Webanwendung ermöglicht Entwicklung unabhängig vom Zettelstore-Release-Zyklus. Es verfügt über Frontend-Kenntnisse (JavaScript, HTML, CSS), aber nicht über Go-Kenntnisse. Die Zettelstore REST-API ist dokumentiert und stabil. Der zusätzliche Aufwand für eine separate Positionsdatenbank ist geringer als die Integration in die Zettelstore-Codebase.

Konsequenzen:

Positive Konsequenzen
  - Frontend-Entwicklung kann sofort beginnen
  - Moderne JavaScript-Frameworks können eingesetzt werden
  - Zettelstore bleibt unverändert und stabil
  - Updates von Zettelstore beeinflussen ZettelWeb nicht

 Negative Konsequenzen
  - Separate Datenbank für Positionen muss implementiert werden
  - API-Calls zwischen Browser und Zettelstore nötig
  - Zwei Datenquellen müssen synchron gehalten werden

 Auswirkungen auf weitere Entscheidungen
  - Datenspeicher-Lösung muss gewählt werden (LocalStorage, eigene DB, etc.)
  - Frontend-Framework kann frei gewählt werden
  - API-Client muss implementiert werden