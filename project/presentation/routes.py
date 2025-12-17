# presentation/routes.py
# Praesentationsschicht: HTTP-Routen und Request-Handling
#
# Diese Schicht nimmt HTTP-Requests entgegen, delegiert an die
# Logikschicht und rendert die Antwort als HTML oder JSON.
#
# Routen:
# - /         : Listenansicht (bestehend)
# - /graph    : Graph-Visualisierung (neu)
# - /api/*    : JSON-API-Endpunkte (neu)

from flask import Blueprint, render_template, request, jsonify
from application import zettel_service
from application import graph_service
from infrastructure.zettelstore_repo import ZettelstoreError
from infrastructure.sqlite_repo import SQLiteError

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


# ============================================================================
# GRAPH-VISUALISIERUNG
# ============================================================================

@bp.route('/graph')
def graph_view():
    """
    Graph-Ansicht: Zeigt die interaktive D3.js-Visualisierung.
    """
    return render_template('graph.html')


@bp.route('/api/graph')
def api_graph():
    """
    API-Endpunkt: Liefert Graph-Daten fuer D3.js.

    Returns:
        JSON: {
            'nodes': [{id, title, tags, x?, y?, fixed?}, ...],
            'links': [{source, target}, ...]
        }
    """
    try:
        data = graph_service.baue_graph_daten()
        return jsonify(data)
    except ZettelstoreError as e:
        return jsonify({'error': str(e), 'nodes': [], 'links': []}), 503


@bp.route('/api/positions', methods=['GET'])
def api_get_positions():
    """
    API-Endpunkt: Laedt alle gespeicherten Positionen.

    Returns:
        JSON: {zettel_id: {x, y, fixiert}, ...}
    """
    try:
        positionen = graph_service.hole_positionen()
        return jsonify(positionen)
    except SQLiteError as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/api/positions', methods=['POST'])
def api_save_position():
    """
    API-Endpunkt: Speichert die Position eines Zettels.

    Request Body (JSON):
        {id: string, x: number, y: number}

    Returns:
        JSON: {success: bool}
    """
    try:
        data = request.get_json()

        if not data:
            return jsonify({'success': False, 'error': 'Keine Daten'}), 400

        zettel_id = data.get('id')
        x = data.get('x')
        y = data.get('y')

        if not all([zettel_id, x is not None, y is not None]):
            return jsonify({'success': False, 'error': 'id, x und y erforderlich'}), 400

        graph_service.aktualisiere_position(zettel_id, x, y)
        return jsonify({'success': True})

    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except SQLiteError as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@bp.route('/api/positions', methods=['DELETE'])
def api_delete_positions():
    """
    API-Endpunkt: Loescht alle Positionen (Reset Layout).

    Returns:
        JSON: {success: bool, deleted: int}
    """
    try:
        count = graph_service.setze_positionen_zurueck()
        return jsonify({'success': True, 'deleted': count})
    except SQLiteError as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@bp.route('/api/state/<key>', methods=['GET'])
def api_get_state(key):
    """
    API-Endpunkt: Laedt einen Graph-State-Wert.

    Args:
        key: Der Schluessel (z.B. 'zoom', 'pan', 'filter')

    Returns:
        JSON: {value: string|null}
    """
    try:
        value = graph_service.hole_graph_state(key)
        return jsonify({'value': value})
    except SQLiteError as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/api/state/<key>', methods=['POST'])
def api_save_state(key):
    """
    API-Endpunkt: Speichert einen Graph-State-Wert.

    Args:
        key: Der Schluessel

    Request Body (JSON):
        {value: string}

    Returns:
        JSON: {success: bool}
    """
    try:
        data = request.get_json()

        if data is None:
            return jsonify({'success': False, 'error': 'Keine Daten'}), 400

        value = data.get('value')
        graph_service.speichere_graph_state(key, value)
        return jsonify({'success': True})

    except SQLiteError as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@bp.route('/api/tags')
def api_tags():
    """
    API-Endpunkt: Liefert alle verfuegbaren Tags.

    Returns:
        JSON: {tags: ['#tag1', '#tag2', ...]}
    """
    try:
        tags = graph_service.hole_alle_tags()
        return jsonify({'tags': tags})
    except ZettelstoreError as e:
        return jsonify({'error': str(e), 'tags': []}), 503


@bp.route('/api/zettel/<id>/json')
def api_zettel_detail(id):
    """
    API-Endpunkt: Liefert Detail-Daten eines Zettels als JSON.

    Returns:
        JSON: {id, title, content, meta, tags, links}
    """
    try:
        detail = graph_service.hole_zettel_fuer_detail(id)

        if detail:
            return jsonify(detail)
        else:
            return jsonify({'error': 'Zettel nicht gefunden'}), 404

    except ZettelstoreError as e:
        return jsonify({'error': str(e)}), 503
