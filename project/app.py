from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def request_zettel_page():
    try:
        r = requests.get("http://127.0.0.1:23123/z", timeout=5)
        if r.status_code != 200: #kontrolliert, ob die API verfügbar ist
            return None, "API-Fehler"

        return r.text, None

    except requests.exceptions.ConnectionError:
        return None, "Zettelstore nicht erreichbar" #Verfügbarkeit Zettelstore

    except requests.exceptions.Timeout:
        return None, "Timeout bei Anfrage" #Timeout-Error

def sort_zettel(zettel, sort_param, dir_param):
    # Sortierkriterium prüfen
    valid_sorts = {'id', 'title'}
    sort = sort_param if sort_param in valid_sorts else 'id'

    # Richtung prüfen
    direction = dir_param if dir_param in {'asc', 'desc'} else 'asc'
    reverse = (direction == 'desc')

    # Sortierung anwenden
    if sort == 'title':
        zettel_sorted = sorted(
            zettel,
            key=lambda z: z['title'].lower(),
            reverse=reverse
        )
    else:
        zettel_sorted = sorted(
            zettel,
            key=lambda z: int(z['id']),
            reverse=reverse
        )

    return zettel_sorted, sort, direction

def get_tags():

    r = requests.get("http://127.0.0.1:23123/z", params={"q": "|tags"})
    r.raise_for_status()  # Fehler auslösen falls der request fehlschlägt

    tags = {}
    # Zeilen der Reihe nach durchgehen
    for line in r.text.strip().split('\n'):
        parts = line.split()
        if not parts:
            continue

        tag = parts[0]
        ids = parts[1:]

        tags[tag] = ids

    return tags

def get_links():
    r = requests.get("http://127.0.0.1:23123/z", params={"q": "|links"})
    r.raise_for_status()
    links = {}
    for line in r.text.strip().split('\n'):
        parts = line.split()
        if parts:
            z_id = parts[0]
            connected = parts[1:]
            links[z_id] = connected
    return links


@app.route('/')
def index():
    data, error = request_zettel_page()  # Zugriff auf Funktion

    if error:
        return render_template('index.html', zettel=[], error=error)


    zettel = []
    r = requests.get("http://127.0.0.1:23123/z")
    for line in r.text.strip().split('\n'):
        parts = line.split(' ', 1)
        zettel.append({'id': parts[0], 'title': parts[1] if len(parts) > 1 else ''})

    query = request.args.get('query', '').lower()
    if query:
        zettel = [z for z in zettel if query in z['title'].lower() or query in z['id'].lower()]

    tags = get_tags()

    # Sortierparameter aus den URL holen
    sort_param = request.args.get('sort', 'id')
    dir_param = request.args.get('dir', 'asc')

    zettel, sort, direction = sort_zettel(zettel, sort_param, dir_param)

    # Tags und Links abrufen
    tags = get_tags()
    links = get_links()

    for z in zettel:
        # Tags zuordnen
        z['tags'] = [t for t, ids in tags.items() if z['id'] in ids]
        # Verbundene Zettel zuordnen
        z['verbunden'] = ', '.join(links.get(z['id'], []))

    return render_template(
        'index.html',
        zettel=zettel,
        sort=sort,
        direction=direction,
        query=query
    )


'''Zettel Inhalt und Metadaten - Heinrich'''
@app.route('/zettel/<id>')
def zettel_content(id):
    r_content = requests.get(f"http://127.0.0.1:23123/z/{id}?part=zettel")
    r_meta = requests.get(f"http://127.0.0.1:23123/z/{id}?part=meta")

    if r_content.status_code == 200:
        return render_template('zettel_content.html', id=id, content=r_content.text, meta=r_meta.text)
    elif r_content.status_code == 418:
        return "🫖", 418
    else:
        return "Zettel nicht gefunden", 404


if __name__ == '__main__':
    app.run(debug=True)

@app.route("api/count")
def api_count():
    zettel = request.args.get("zettel")
    c = 0
    for _ in zettel:
        c += 1
    if c > 0:
        return jsonify({'count': c})
    return jsonify({'count': 0})