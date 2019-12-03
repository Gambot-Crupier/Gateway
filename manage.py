from flask.cli import FlaskGroup
from project import app
from flask import jsonify


cli = FlaskGroup(app)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World!"})

if __name__ == '__main__':
    cli()