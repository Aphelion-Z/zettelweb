# infrastructure/sqlite_repo.py
# Datenschicht: SQLite-Datenbank fuer Positionsspeicherung
#
# Diese Schicht ist NUR fuer den Datenzugriff zustaendig.
# Keine Geschaeftslogik, keine Sortierung, keine Filterung.
#
# Auto-Init: Tabellen werden automatisch erstellt, falls nicht vorhanden.

import sqlite3
import os
from contextlib import contextmanager

# Datenbankpfad relativ zum Projektverzeichnis
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'zettelweb.db')


class SQLiteError(Exception):
    """Fehler bei der SQLite-Datenbankoperation"""
    pass


@contextmanager
def get_connection():
    """
    Kontextmanager fuer Datenbankverbindungen.
    Stellt sicher, dass Verbindungen sauber geschlossen werden.
    """
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row  # Ergebnisse als Dict-aehnliche Objekte
        yield conn
    except sqlite3.Error as e:
        raise SQLiteError(f"Datenbankfehler: {e}")
    finally:
        if conn:
            conn.close()


def init_db():
    """
    Initialisiert die Datenbank mit allen notwendigen Tabellen.
    Wird beim App-Start aufgerufen. Sicher bei mehrfachem Aufruf.

    Tabellen:
    - positionen: Speichert x/y Koordinaten der Zettel im Graph
    - graph_state: Speichert Zoom, Pan, Filter-Einstellungen
    """
    with get_connection() as conn:
        cursor = conn.cursor()

        # Tabelle fuer Zettel-Positionen
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS positionen (
                zettel_id TEXT PRIMARY KEY,
                x REAL NOT NULL,
                y REAL NOT NULL,
                fixiert INTEGER DEFAULT 0,
                aktualisiert_am TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Index fuer schnellere Abfragen
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_positionen_aktualisiert
            ON positionen(aktualisiert_am)
        ''')

        # Tabelle fuer Graph-State (Zoom, Pan, Filter)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS graph_state (
                schluessel TEXT PRIMARY KEY,
                wert TEXT,
                aktualisiert_am TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()


def speichere_position(zettel_id, x, y, fixiert=False):
    """
    Speichert oder aktualisiert die Position eines Zettels.

    Args:
        zettel_id: Die ID des Zettels (String)
        x: X-Koordinate (Float)
        y: Y-Koordinate (Float)
        fixiert: Ob der Zettel manuell positioniert wurde (Bool)

    Raises:
        SQLiteError: Bei Datenbankfehlern
    """
    # Validierung
    if not zettel_id or not isinstance(zettel_id, str):
        raise SQLiteError("Ungueltige Zettel-ID")

    try:
        x = float(x)
        y = float(y)
    except (TypeError, ValueError):
        raise SQLiteError("Ungueltige Koordinaten")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO positionen (zettel_id, x, y, fixiert, aktualisiert_am)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(zettel_id) DO UPDATE SET
                x = excluded.x,
                y = excluded.y,
                fixiert = excluded.fixiert,
                aktualisiert_am = CURRENT_TIMESTAMP
        ''', (zettel_id, x, y, 1 if fixiert else 0))
        conn.commit()


def lade_alle_positionen():
    """
    Laedt alle gespeicherten Positionen.

    Returns:
        dict: Dictionary mit zettel_id als Key und {x, y, fixiert} als Value
              z.B. {'20241027134512': {'x': 100.5, 'y': 200.3, 'fixiert': True}}
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT zettel_id, x, y, fixiert FROM positionen')

        positionen = {}
        for row in cursor.fetchall():
            positionen[row['zettel_id']] = {
                'x': row['x'],
                'y': row['y'],
                'fixiert': bool(row['fixiert'])
            }
        return positionen


def lade_position(zettel_id):
    """
    Laedt die Position eines einzelnen Zettels.

    Args:
        zettel_id: Die ID des Zettels

    Returns:
        dict: {x, y, fixiert} oder None wenn nicht gefunden
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT x, y, fixiert FROM positionen WHERE zettel_id = ?',
            (zettel_id,)
        )
        row = cursor.fetchone()

        if row:
            return {
                'x': row['x'],
                'y': row['y'],
                'fixiert': bool(row['fixiert'])
            }
        return None


def loesche_position(zettel_id):
    """
    Loescht die Position eines Zettels.

    Args:
        zettel_id: Die ID des Zettels

    Returns:
        bool: True wenn geloescht, False wenn nicht gefunden
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM positionen WHERE zettel_id = ?', (zettel_id,))
        conn.commit()
        return cursor.rowcount > 0


def loesche_alle_positionen():
    """
    Loescht alle gespeicherten Positionen (Reset).

    Returns:
        int: Anzahl der geloeschten Eintraege
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM positionen')
        conn.commit()
        return cursor.rowcount


def speichere_state(schluessel, wert):
    """
    Speichert einen Graph-State-Wert (z.B. Zoom, Pan, Filter).

    Args:
        schluessel: Der Schluessel (z.B. 'zoom', 'pan_x', 'filter_tags')
        wert: Der Wert als String (JSON fuer komplexe Werte)

    Raises:
        SQLiteError: Bei Datenbankfehlern
    """
    if not schluessel or not isinstance(schluessel, str):
        raise SQLiteError("Ungueltiger Schluessel")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO graph_state (schluessel, wert, aktualisiert_am)
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(schluessel) DO UPDATE SET
                wert = excluded.wert,
                aktualisiert_am = CURRENT_TIMESTAMP
        ''', (schluessel, str(wert) if wert is not None else None))
        conn.commit()


def lade_state(schluessel):
    """
    Laedt einen Graph-State-Wert.

    Args:
        schluessel: Der Schluessel

    Returns:
        str: Der gespeicherte Wert oder None
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT wert FROM graph_state WHERE schluessel = ?',
            (schluessel,)
        )
        row = cursor.fetchone()
        return row['wert'] if row else None


def lade_alle_states():
    """
    Laedt alle Graph-State-Werte.

    Returns:
        dict: Dictionary mit allen State-Werten
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT schluessel, wert FROM graph_state')
        return {row['schluessel']: row['wert'] for row in cursor.fetchall()}


def loesche_state(schluessel):
    """
    Loescht einen Graph-State-Wert.

    Args:
        schluessel: Der Schluessel

    Returns:
        bool: True wenn geloescht
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM graph_state WHERE schluessel = ?', (schluessel,))
        conn.commit()
        return cursor.rowcount > 0


def loesche_alle_states():
    """
    Loescht alle Graph-State-Werte (Reset View).

    Returns:
        int: Anzahl der geloeschten Eintraege
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM graph_state')
        conn.commit()
        return cursor.rowcount
