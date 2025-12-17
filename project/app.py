# app.py
# Entry-Point der Anwendung
#
# Architektur: 3-Schichten (Three-Tier Architecture)
# - presentation/  : HTTP-Routen, Templates, Static Files
# - application/   : Geschaeftslogik (Sortierung, Filterung, Suche)
# - infrastructure/: Datenzugriff (Zettelstore API)
#
# Siehe: project/Wahl des Architekturmodels + Begruendung

import os
from flask import Flask
from presentation.routes import bp as main_bp


def create_app():
    """
    Application Factory: Erstellt und konfiguriert die Flask-App.
    """
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'presentation', 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'presentation', 'static')
    )

    # Blueprint registrieren
    app.register_blueprint(main_bp)

    return app


# Fuer direkten Start: python app.py
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
