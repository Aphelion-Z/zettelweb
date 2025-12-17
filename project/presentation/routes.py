# presentation/routes.py
# Praesentationsschicht: HTTP-Routen und Request-Handling
#
# Diese Schicht nimmt HTTP-Requests entgegen, delegiert an die
# Logikschicht und rendert die Antwort als HTML oder JSON.

from flask import Blueprint, render_template, request, jsonify
from application import zettel_service
from infrastructure.zettelstore_repo import ZettelstoreError

# Blueprint fuer alle Routen
bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """
    Hauptseite: Zeigt die Zettel-Uebersicht mit Sortierung und Suche.
    """
    try:
        # 1. Daten laden (ueber Logikschicht)
        zettel = zettel_service.lade_alle_zettel()
        tags = zettel_service.lade_tags()
        links = zettel_service.lade_links()

    except ZettelstoreError as e:
        # Fehlerfall: Leere Liste mit Fehlermeldung
        return render_template('index.html', zettel=[], error=str(e))

    # 2. Suchparameter verarbeiten
    query = request.args.get('query', '')
    if query:
        zettel = zettel_service.suche_zettel(zettel, query)

    # 3. Sortierparameter verarbeiten
    sort_param = request.args.get('sort', 'id')
    dir_param = request.args.get('dir', 'asc')
    zettel = zettel_service.sortiere_zettel(zettel, sort_param, dir_param)

    # 4. Zettel mit Tags und Links anreichern
    zettel = zettel_service.reichere_zettel_an(zettel, tags, links)

    # 5. Template rendern
    return render_template(
        'index.html',
        zettel=zettel,
        sort=sort_param,
        direction=dir_param,
        query=query
    )


@bp.route('/zettel/<id>')
def zettel_detail(id):
    """
    Detailansicht: Zeigt Inhalt und Metadaten eines Zettels.
    """
    detail = zettel_service.hole_zettel_detail(id)

    if detail:
        return render_template(
            'zettel_content.html',
            id=id,
            content=detail['content'],
            meta=detail['meta']
        )
    else:
        return "Zettel nicht gefunden", 404


@bp.route('/api/count')
def api_count():
    """
    API-Endpunkt: Gibt die Anzahl der Zettel zurueck.
    """
    try:
        zettel = zettel_service.lade_alle_zettel()
        return jsonify({'count': len(zettel)})
    except ZettelstoreError:
        return jsonify({'count': 0, 'error': 'Zettelstore nicht erreichbar'})
