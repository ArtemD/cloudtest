from flask import Flask
from api import get_json

app = Flask(__name__)

@app.route('/api/all')
def api():
    return get_json()

if __name__ == "__main__":
    app.run(port=5000)