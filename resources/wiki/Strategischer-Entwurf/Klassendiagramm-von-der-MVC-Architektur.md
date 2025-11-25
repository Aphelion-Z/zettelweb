---
title: Klassendiagramm von der MVC Architektur
---


![Screenshot_2025-10-22_123610](uploads/e07fd02a112742e6a6d509203dad8ca3/Screenshot_2025-10-22_123610.png)

Die Software „ZettelWeb“ basiert auf dem Architekturmodell Model–View–Controller (MVC). Dieses Modell trennt die Anwendung in drei zentrale Schichten – Model, View und Controller – um Verantwortlichkeiten klar zu definieren und eine lose Kopplung zwischen Datenhaltung, Steuerung und Darstellung zu gewährleisten.

Der Benutzer (User/UI) interagiert über die grafische Oberfläche mit dem System, beispielsweise durch das Klicken auf einen Zettel oder ein Tag. Diese Interaktion löst ein Ereignis aus, das vom Controller verarbeitet wird. Der Controller fungiert als Vermittler zwischen Nutzer, Model und View. Seine Hauptaufgaben bestehen darin, Benutzereingaben entgegenzunehmen (handleInput()), Daten aus dem Model zu laden (loadZettelData()) und die Benutzeroberfläche bei Änderungen zu aktualisieren (updateView()).

Das Model repräsentiert die Daten- und Logikebene der Anwendung. Es enthält Klassen wie Zettel, Tag und ZettelCluster, die für das Laden, Speichern und Analysieren der Zettel verantwortlich sind. Typische Methoden sind loadZettel(), clusterByTags() oder saveProperties(). Das Model verwaltet Zustände, Beziehungen und Koordinaten der Zettel und fungiert damit als zentrale Datenquelle der Anwendung. Über eine REST-API kommuniziert das Model mit dem externen Zettelstore-Service, um Daten zu laden oder zu speichern.

Der Zettelstore-Service stellt die Schnittstelle zwischen der Anwendung und dem externen Datenspeicher dar. Er stellt Methoden wie getZettelList(), getZettel(id) und saveZettelData() bereit. Diese ermöglichen den Zugriff auf Zettel, deren Metadaten und Koordinaten. Der Zettelstore-Service verwaltet dabei die Kommunikation mit der darunterliegenden Datenbank (DB), in der die Tabellen zettel, coordinates und properties gespeichert sind. Dadurch bleibt das Model der Anwendung unabhängig von der konkreten Datenhaltungsschicht.

Die View bildet die Präsentationsschicht und ist für die visuelle Darstellung der Daten verantwortlich. Sie visualisiert die von der Model-Schicht bereitgestellten Informationen in Form von Gruppen oder Clustern (renderGroups()) und reagiert auf Benutzeraktionen oder Controller-Events. Zu ihren Funktionen zählen etwa das Hervorheben von Tags (highlightTag()), die Anzeige von Zettelinformationen (displayZettelInfo()) und das Aktualisieren von Positionen (updateZettelPosition()).

Der Datenfluss verläuft grundsätzlich vom Nutzer über den Controller zum Model und zurück über die View zum Nutzer. Änderungen im Model werden über definierte Schnittstellen an die View weitergegeben, sodass eine automatische Aktualisierung der Oberfläche erfolgen kann.
Durch diese Trennung der Verantwortlichkeiten ermöglicht das MVC-Modell eine hohe Wartbarkeit und Erweiterbarkeit: Änderungen an der Darstellung oder an der Datenlogik können unabhängig voneinander vorgenommen werden. Außerdem erlaubt die klare Aufgabentrennung eine bessere Testbarkeit einzelner Komponenten.

Zusammenfassend besteht die innere Architektur von ZettelWeb aus einer strukturierten Kombination von Benutzerinteraktion, zentralem Datenmodell, Visualisierungsschicht und externer Datenspeicherung. Die Kommunikation mit dem Zettelstore erfolgt über eine REST-Schnittstelle, wodurch das System flexibel in bestehende Umgebungen integriert werden kann und zukünftige Erweiterungen – etwa neue Visualisierungen oder Datenquellen – ohne tiefgreifende Änderungen der Kernarchitektur möglich sind.