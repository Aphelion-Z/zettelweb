---
title: Systemaufbau-Komponentendiagramm
---

Das System NetzWeb ist als webbasierte Client-Server-Anwendung mit MVC-Struktur konzipiert.
Der Benutzer arbeitet im Browser (View, Controller), während das Backend (Model-Teil) Geschäftslogik und Persistenz kapselt.
Über standardisierte REST-Schnittstellen kommuniziert das NetzWeb-Backend mit dem bestehenden Zettelstore, aus dem Zettelinhalte und Metadaten bezogen werden.
Temporäre Layout- und Positionsdaten werden lokal im NetzWeb-Backend in einer separaten Datenbank gespeichert, um Performance zu gewährleisten und den Zettelstore zu entlasten.
Die gesamte Kommunikation erfolgt über HTTPS mit JSON-basierten Requests und Responses.
Durch diese klare Trennung bleibt das System wartbar, erweiterbar und performant.![Screenshot_2025-10-22_125636](uploads/513e4272939df0cb46b4c927b8ae8a83/Screenshot_2025-10-22_125636.png)