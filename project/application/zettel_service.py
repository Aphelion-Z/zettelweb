# application/zettel_service.py
# Logikschicht: Geschaeftslogik fuer Zettel-Verarbeitung
#
# Diese Schicht verarbeitet Daten und implementiert die Geschaeftsregeln.
# Keine HTTP-Logik, keine direkten API-Aufrufe.

from infrastructure import zettelstore_repo
from infrastructure.zettelstore_repo import ZettelstoreError


def lade_alle_zettel():
    """
    Laedt alle Zettel und wandelt sie in eine Liste von Dictionaries um.

    Returns:
        list: Liste von Zettel-Dictionaries mit 'id' und 'title'

    Raises:
        ZettelstoreError: Bei Verbindungsproblemen
    """
    rohdaten = zettelstore_repo.hole_alle_zettel_roh()

    zettel = []
    for zeile in rohdaten.strip().split('\n'):
        if not zeile:
            continue
        teile = zeile.split(' ', 1)
        zettel.append({
            'id': teile[0],
            'title': teile[1] if len(teile) > 1 else ''
        })
    return zettel


def sortiere_zettel(zettel, sortierung='id', richtung='asc'):
    """
    Sortiert eine Zettel-Liste nach dem angegebenen Kriterium.

    Args:
        zettel: Liste von Zettel-Dictionaries
        sortierung: 'id' oder 'title'
        richtung: 'asc' oder 'desc'

    Returns:
        list: Sortierte Zettel-Liste
    """
    # Validierung der Parameter
    if sortierung not in {'id', 'title'}:
        sortierung = 'id'
    if richtung not in {'asc', 'desc'}:
        richtung = 'asc'

    umkehren = (richtung == 'desc')

    if sortierung == 'title':
        return sorted(
            zettel,
            key=lambda z: z['title'].lower(),
            reverse=umkehren
        )
    else:
        return sorted(
            zettel,
            key=lambda z: int(z['id']),
            reverse=umkehren
        )


def suche_zettel(zettel, suchbegriff):
    """
    Filtert Zettel nach einem Suchbegriff.

    Args:
        zettel: Liste von Zettel-Dictionaries
        suchbegriff: Suchstring (case-insensitive)

    Returns:
        list: Gefilterte Zettel-Liste
    """
    if not suchbegriff:
        return zettel

    suchbegriff = suchbegriff.lower()
    return [
        z for z in zettel
        if suchbegriff in z['title'].lower()
        or suchbegriff in z['id'].lower()
    ]


def lade_tags():
    """
    Laedt und parsed die Tag-Zuordnungen.

    Returns:
        dict: Dictionary mit Tag als Key und Liste von IDs als Value
    """
    rohdaten = zettelstore_repo.hole_tags_roh()

    tags = {}
    for zeile in rohdaten.strip().split('\n'):
        teile = zeile.split()
        if teile:
            tag = teile[0]
            ids = teile[1:]
            tags[tag] = ids
    return tags


def lade_links():
    """
    Laedt und parsed die Verbindungen zwischen Zetteln.

    Returns:
        dict: Dictionary mit Zettel-ID als Key und Liste von verbundenen IDs
    """
    rohdaten = zettelstore_repo.hole_links_roh()

    links = {}
    for zeile in rohdaten.strip().split('\n'):
        teile = zeile.split()
        if teile:
            zettel_id = teile[0]
            verbunden = teile[1:]
            links[zettel_id] = verbunden
    return links


def reichere_zettel_an(zettel, tags, links):
    """
    Reichert Zettel mit Tags und Verbindungen an.

    Args:
        zettel: Liste von Zettel-Dictionaries
        tags: Tag-Dictionary von lade_tags()
        links: Link-Dictionary von lade_links()

    Returns:
        list: Angereicherte Zettel-Liste
    """
    for z in zettel:
        # Tags zuordnen
        z['tags'] = [tag for tag, ids in tags.items() if z['id'] in ids]
        # Verbundene Zettel zuordnen
        z['verbunden'] = ', '.join(links.get(z['id'], []))

    return zettel


def hole_zettel_detail(zettel_id):
    """
    Holt Inhalt und Metadaten eines einzelnen Zettels.

    Args:
        zettel_id: Die ID des Zettels

    Returns:
        dict: Dictionary mit 'content' und 'meta', oder None
    """
    inhalt = zettelstore_repo.hole_zettel_inhalt(zettel_id)
    meta = zettelstore_repo.hole_zettel_meta(zettel_id)

    if inhalt is None:
        return None

    return {
        'content': inhalt,
        'meta': meta or ''
    }
