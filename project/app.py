# app.py
# Entry-Point der Anwendung
#
# Architektur: 3-Schichten (Three-Tier Architecture)
# - presentation/  : HTTP-Routen, Templates, Static Files
# - application/   : Geschaeftslogik (Sortierung, Filterung, Suche)
# - infrastructure/: Datenzugriff (Zettelstore API, SQLite)
#
# Siehe: project/Wahl des Architekturmodels + Begruendung

import os
from flask import Flask
from presentation.routes import bp as main_bp
from infrastructure import sqlite_repo


def create_app():
    """
    Application Factory: Erstellt und konfiguriert die Flask-App.

    - Initialisiert SQLite-Datenbank automatisch (Auto-Init)
    - Registriert alle Blueprints
    """
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'presentation', 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'presentation', 'static')
    )

    # SQLite-Datenbank initialisieren (erstellt Tabellen falls nicht vorhanden)
    sqlite_repo.init_db()

    # Blueprint registrieren
    app.register_blueprint(main_bp)

    return app


# Fuer direkten Start: python app.py
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
