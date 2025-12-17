# infrastructure/zettelstore_repo.py
# Datenschicht: Kommunikation mit der Zettelstore REST API
#
# Diese Schicht ist NUR fuer den Datenzugriff zustaendig.
# Keine Geschaeftslogik, keine Sortierung, keine Filterung.

import requests

ZETTELSTORE_URL = "http://127.0.0.1:23123"
TIMEOUT = 5


class ZettelstoreError(Exception):
    """Fehler bei der Kommunikation mit dem Zettelstore"""
    pass


def hole_alle_zettel_roh():
    """
    Holt die rohe Zettel-Liste vom Zettelstore.

    Returns:
        str: Rohdaten im Format "ID Titel" pro Zeile

    Raises:
        ZettelstoreError: Bei Verbindungs- oder API-Fehlern
    """
    try:
        r = requests.get(f"{ZETTELSTORE_URL}/z", timeout=TIMEOUT)
        if r.status_code != 200:
            raise ZettelstoreError(f"API-Fehler: Status {r.status_code}")
        return r.text
    except requests.exceptions.ConnectionError:
        raise ZettelstoreError("Zettelstore nicht erreichbar")
    except requests.exceptions.Timeout:
        raise ZettelstoreError("Timeout bei Anfrage")


def hole_zettel_inhalt(zettel_id):
    """
    Holt den Inhalt eines einzelnen Zettels.

    Args:
        zettel_id: Die ID des Zettels

    Returns:
        str: Zettel-Inhalt oder None wenn nicht gefunden
    """
    try:
        r = requests.get(
            f"{ZETTELSTORE_URL}/z/{zettel_id}",
            params={"part": "zettel"},
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            return r.text
        return None
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None


def hole_zettel_meta(zettel_id):
    """
    Holt die Metadaten eines einzelnen Zettels.

    Args:
        zettel_id: Die ID des Zettels

    Returns:
        str: Metadaten oder None wenn nicht gefunden
    """
    try:
        r = requests.get(
            f"{ZETTELSTORE_URL}/z/{zettel_id}",
            params={"part": "meta"},
            timeout=TIMEOUT
        )
        if r.status_code == 200:
            return r.text
        return None
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None


def hole_tags_roh():
    """
    Holt die rohen Tag-Zuordnungen vom Zettelstore.

    Returns:
        str: Rohdaten im Format "TAG ID1 ID2 ..." pro Zeile

    Raises:
        ZettelstoreError: Bei Verbindungs- oder API-Fehlern
    """
    try:
        r = requests.get(
            f"{ZETTELSTORE_URL}/z",
            params={"q": "|tags"},
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        raise ZettelstoreError(f"Fehler beim Abrufen der Tags: {e}")


def hole_links_roh():
    """
    Holt die rohen Verbindungen vom Zettelstore.

    HINWEIS: Die alte |links Query liefert nur Zettel die Links haben,
    nicht die tatsaechlichen Verbindungen. Diese Funktion ist veraltet.

    Returns:
        str: Rohdaten im Format "ID LINK1 LINK2 ..." pro Zeile

    Raises:
        ZettelstoreError: Bei Verbindungs- oder API-Fehlern
    """
    try:
        r = requests.get(
            f"{ZETTELSTORE_URL}/z",
            params={"q": "|links"},
            timeout=TIMEOUT
        )
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as e:
        raise ZettelstoreError(f"Fehler beim Abrufen der Links: {e}")


def hole_alle_zettel_mit_inhalt():
    """
    Holt alle Zettel mit ihrem Inhalt (fuer Link-Extraktion).

    Returns:
        list: Liste von {id, title, content} Dictionaries

    Raises:
        ZettelstoreError: Bei Verbindungs- oder API-Fehlern
    """
    import re

    try:
        # Erst alle Zettel-IDs holen
        r = requests.get(f"{ZETTELSTORE_URL}/z", timeout=TIMEOUT)
        if r.status_code != 200:
            raise ZettelstoreError(f"API-Fehler: Status {r.status_code}")

        zettel_liste = []
        for zeile in r.text.strip().split('\n'):
            if not zeile:
                continue
            teile = zeile.split(' ', 1)
            zettel_id = teile[0]
            titel = teile[1] if len(teile) > 1 else ''

            # Inhalt fuer jeden Zettel holen
            try:
                r_content = requests.get(
                    f"{ZETTELSTORE_URL}/z/{zettel_id}",
                    params={"part": "content"},
                    timeout=TIMEOUT
                )
                inhalt = r_content.text if r_content.ok else ''
            except:
                inhalt = ''

            zettel_liste.append({
                'id': zettel_id,
                'title': titel,
                'content': inhalt
            })

        return zettel_liste

    except requests.exceptions.ConnectionError:
        raise ZettelstoreError("Zettelstore nicht erreichbar")
    except requests.exceptions.Timeout:
        raise ZettelstoreError("Timeout bei Anfrage")


def extrahiere_links_aus_inhalt(inhalt):
    """
    Extrahiert Zettel-Links aus ZettelMarkup-Inhalt.

    Links haben das Format: [[Text|ID]] oder [[ID]]
    wobei ID eine 14-stellige Zahl ist (YYYYMMDDHHMMSS)

    Args:
        inhalt: Der Zettel-Inhalt als String

    Returns:
        list: Liste von Zettel-IDs die verlinkt sind
    """
    import re

    if not inhalt:
        return []

    # Pattern: [[optionaler Text|ID]] oder [[ID]]
    # ID ist 14-stellig (Zettelstore-Format) oder andere Formate
    pattern = r'\[\[(?:[^\]|]*\|)?(\d{14}|\d{11})\]\]'
    gefundene = re.findall(pattern, inhalt)

    # Duplikate entfernen, Reihenfolge beibehalten
    gesehen = set()
    eindeutig = []
    for link_id in gefundene:
        if link_id not in gesehen:
            gesehen.add(link_id)
            eindeutig.append(link_id)

    return eindeutig


def baue_link_map():
    """
    Baut eine Map aller Verbindungen zwischen Zetteln.

    Parst jeden Zettel-Inhalt und extrahiert die verlinkten IDs.

    Returns:
        dict: {source_id: [target_id1, target_id2, ...]}

    Raises:
        ZettelstoreError: Bei Verbindungs- oder API-Fehlern
    """
    zettel_liste = hole_alle_zettel_mit_inhalt()

    link_map = {}
    for zettel in zettel_liste:
        links = extrahiere_links_aus_inhalt(zettel['content'])
        if links:
            link_map[zettel['id']] = links

    return link_map
