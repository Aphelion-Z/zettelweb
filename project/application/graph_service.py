# application/graph_service.py
# Logikschicht: Geschaeftslogik fuer Graph-Visualisierung
#
# Diese Schicht verarbeitet Daten und baut das Graph-Format fuer D3.js auf.
# Keine HTTP-Logik, keine direkten API-Aufrufe.

from application import zettel_service
from infrastructure import sqlite_repo
from infrastructure.zettelstore_repo import ZettelstoreError


def baue_graph_daten():
    """
    Baut die kompletten Graph-Daten fuer D3.js auf.

    Kombiniert:
    - Zettel-Daten vom Zettelstore (Knoten)
    - Verbindungen zwischen Zetteln (Kanten)
    - Gespeicherte Positionen aus SQLite
    - Tag-Informationen

    Returns:
        dict: {
            'nodes': [
                {
                    'id': '20241027134512',
                    'title': 'Mein Zettel',
                    'tags': ['#tag1', '#tag2'],
                    'x': 100.5,       # Nur wenn Position gespeichert
                    'y': 200.3,       # Nur wenn Position gespeichert
                    'fixed': False    # Manuell positioniert?
                },
                ...
            ],
            'links': [
                {'source': '20241027134512', 'target': '20241028091234'},
                ...
            ]
        }

    Raises:
        ZettelstoreError: Bei Verbindungsproblemen zum Zettelstore
    """
    # 1. Basis-Daten laden
    zettel = zettel_service.lade_alle_zettel()
    tags = zettel_service.lade_tags()
    links_dict = zettel_service.lade_links()

    # 2. Gespeicherte Positionen laden
    positionen = sqlite_repo.lade_alle_positionen()

    # 3. Knoten aufbauen
    nodes = []
    zettel_ids = set()  # Fuer Validierung der Links

    for z in zettel:
        zettel_id = z['id']
        zettel_ids.add(zettel_id)

        # Tags fuer diesen Zettel finden
        zettel_tags = [tag for tag, ids in tags.items() if zettel_id in ids]

        # Knoten-Objekt erstellen
        node = {
            'id': zettel_id,
            'title': z['title'],
            'tags': zettel_tags
        }

        # Position hinzufuegen falls vorhanden
        if zettel_id in positionen:
            pos = positionen[zettel_id]
            node['x'] = pos['x']
            node['y'] = pos['y']
            node['fixed'] = pos['fixiert']

        nodes.append(node)

    # 4. Kanten aufbauen (nur gueltige Verbindungen)
    links = []
    seen_links = set()  # Verhindert Duplikate bei bidirektionalen Links

    for source_id, target_ids in links_dict.items():
        # Nur Zettel die auch existieren
        if source_id not in zettel_ids:
            continue

        for target_id in target_ids:
            if target_id not in zettel_ids:
                continue

            # Bidirektionale Links nur einmal aufnehmen
            link_key = tuple(sorted([source_id, target_id]))
            if link_key in seen_links:
                continue

            seen_links.add(link_key)
            links.append({
                'source': source_id,
                'target': target_id
            })

    return {
        'nodes': nodes,
        'links': links
    }


def hole_positionen():
    """
    Laedt alle gespeicherten Positionen.

    Returns:
        dict: {zettel_id: {'x': float, 'y': float, 'fixiert': bool}}
    """
    return sqlite_repo.lade_alle_positionen()


def aktualisiere_position(zettel_id, x, y, fixiert=True):
    """
    Aktualisiert die Position eines Zettels.

    Args:
        zettel_id: Die ID des Zettels
        x: X-Koordinate
        y: Y-Koordinate
        fixiert: Ob manuell positioniert (default: True)

    Returns:
        bool: True wenn erfolgreich

    Raises:
        ValueError: Bei ungueltigen Koordinaten
    """
    # Validierung
    if not zettel_id:
        raise ValueError("Zettel-ID ist erforderlich")

    try:
        x = float(x)
        y = float(y)
    except (TypeError, ValueError):
        raise ValueError("Ungueltige Koordinaten")

    sqlite_repo.speichere_position(zettel_id, x, y, fixiert)
    return True


def setze_positionen_zurueck():
    """
    Loescht alle gespeicherten Positionen (Reset Layout).

    Returns:
        int: Anzahl der geloeschten Positionen
    """
    return sqlite_repo.loesche_alle_positionen()


def hole_graph_state(schluessel):
    """
    Laedt einen Graph-State-Wert (z.B. Zoom, Pan).

    Args:
        schluessel: Der Schluessel (z.B. 'zoom', 'pan')

    Returns:
        str: Der gespeicherte Wert oder None
    """
    return sqlite_repo.lade_state(schluessel)


def speichere_graph_state(schluessel, wert):
    """
    Speichert einen Graph-State-Wert.

    Args:
        schluessel: Der Schluessel
        wert: Der Wert (wird als String gespeichert)

    Returns:
        bool: True wenn erfolgreich
    """
    sqlite_repo.speichere_state(schluessel, wert)
    return True


def setze_graph_state_zurueck():
    """
    Loescht alle Graph-State-Werte (Reset View).

    Returns:
        int: Anzahl der geloeschten States
    """
    return sqlite_repo.loesche_alle_states()


def hole_alle_tags():
    """
    Laedt alle verfuegbaren Tags fuer den Filter.

    Returns:
        list: Sortierte Liste aller Tags (z.B. ['#graphen', '#visualisierung'])
    """
    tags = zettel_service.lade_tags()
    return sorted(tags.keys())


def hole_zettel_fuer_detail(zettel_id):
    """
    Laedt alle Daten eines Zettels fuer die Detail-Ansicht.

    Args:
        zettel_id: Die ID des Zettels

    Returns:
        dict: {
            'id': '20241027134512',
            'title': 'Mein Zettel',
            'content': '# Inhalt...',
            'meta': 'title: Mein Zettel\ntags: ...',
            'tags': ['#tag1', '#tag2'],
            'links': ['20241028091234', '20241029101500']
        }
        oder None wenn nicht gefunden
    """
    # Basis-Detail laden
    detail = zettel_service.hole_zettel_detail(zettel_id)
    if not detail:
        return None

    # Alle Zettel laden um Titel zu finden
    alle_zettel = zettel_service.lade_alle_zettel()
    zettel_titel = {z['id']: z['title'] for z in alle_zettel}

    # Tags laden
    tags = zettel_service.lade_tags()
    zettel_tags = [tag for tag, ids in tags.items() if zettel_id in ids]

    # Links laden
    links_dict = zettel_service.lade_links()
    verbundene_ids = links_dict.get(zettel_id, [])

    # Links mit Titeln anreichern
    verbundene = []
    for vid in verbundene_ids:
        verbundene.append({
            'id': vid,
            'title': zettel_titel.get(vid, vid)
        })

    return {
        'id': zettel_id,
        'title': zettel_titel.get(zettel_id, zettel_id),
        'content': detail['content'],
        'meta': detail['meta'],
        'tags': zettel_tags,
        'links': verbundene
    }
