/**
 * api.js - API-Wrapper fuer ZettelWeb
 *
 * Stellt alle Funktionen fuer die Kommunikation mit dem Backend bereit.
 * Alle Funktionen sind async und geben Promises zurueck.
 */

const api = {
    /**
     * Laedt die Graph-Daten (Knoten und Kanten).
     *
     * @returns {Promise<{nodes: Array, links: Array}>}
     */
    async getGraph() {
        const response = await fetch('/api/graph');

        if (!response.ok) {
            throw new Error(`Fehler beim Laden: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            throw new Error(data.error);
        }

        return data;
    },

    /**
     * Laedt alle gespeicherten Positionen.
     *
     * @returns {Promise<Object>} {zettel_id: {x, y, fixiert}}
     */
    async getPositions() {
        const response = await fetch('/api/positions');

        if (!response.ok) {
            throw new Error(`Fehler beim Laden: ${response.status}`);
        }

        return response.json();
    },

    /**
     * Speichert die Position eines Zettels.
     *
     * @param {string} id - Die Zettel-ID
     * @param {number} x - X-Koordinate
     * @param {number} y - Y-Koordinate
     * @returns {Promise<{success: boolean}>}
     */
    async savePosition(id, x, y) {
        const response = await fetch('/api/positions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id, x, y })
        });

        if (!response.ok) {
            throw new Error(`Fehler beim Speichern: ${response.status}`);
        }

        return response.json();
    },

    /**
     * Loescht alle Positionen (Reset Layout).
     *
     * @returns {Promise<{success: boolean, deleted: number}>}
     */
    async resetPositions() {
        const response = await fetch('/api/positions', {
            method: 'DELETE'
        });

        if (!response.ok) {
            throw new Error(`Fehler beim Loeschen: ${response.status}`);
        }

        return response.json();
    },

    /**
     * Laedt die Details eines Zettels.
     *
     * @param {string} id - Die Zettel-ID
     * @returns {Promise<Object>} {id, title, content, meta, tags, links}
     */
    async getZettelDetail(id) {
        const response = await fetch(`/api/zettel/${encodeURIComponent(id)}/json`);

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error('Zettel nicht gefunden');
            }
            throw new Error(`Fehler beim Laden: ${response.status}`);
        }

        return response.json();
    },

    /**
     * Laedt alle verfuegbaren Tags.
     *
     * @returns {Promise<{tags: Array<string>}>}
     */
    async getTags() {
        const response = await fetch('/api/tags');

        if (!response.ok) {
            throw new Error(`Fehler beim Laden: ${response.status}`);
        }

        return response.json();
    },

    /**
     * Laedt einen Graph-State-Wert.
     *
     * @param {string} key - Der Schluessel (z.B. 'zoom', 'pan', 'filter')
     * @returns {Promise<{value: string|null}>}
     */
    async getState(key) {
        const response = await fetch(`/api/state/${encodeURIComponent(key)}`);

        if (!response.ok) {
            throw new Error(`Fehler beim Laden: ${response.status}`);
        }

        return response.json();
    },

    /**
     * Speichert einen Graph-State-Wert.
     *
     * @param {string} key - Der Schluessel
     * @param {string} value - Der Wert
     * @returns {Promise<{success: boolean}>}
     */
    async saveState(key, value) {
        const response = await fetch(`/api/state/${encodeURIComponent(key)}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value })
        });

        if (!response.ok) {
            throw new Error(`Fehler beim Speichern: ${response.status}`);
        }

        return response.json();
    }
};
