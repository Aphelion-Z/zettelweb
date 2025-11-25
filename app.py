from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get("http://127.0.0.1:23123/z")

    zettel = []
    for line in r.text.strip().split('\n'):
        parts = line.split(' ', 1)
        zettel.append({'id': parts[0], 'title': parts[1] if len(parts) > 1 else ''})

    return render_template('index.html', zettel=zettel)

if __name__ == '__main__':
    app.run(debug=True)