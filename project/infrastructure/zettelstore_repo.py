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
