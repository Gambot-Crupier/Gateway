import os
from flask import Flask, jsonify
from project.api.routes.auth import auth_blueprint
from project.api.routes.hands import hands_blueprint
from project.api.routes.table_cards import table_cards

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

app.register_blueprint(auth_blueprint)
app.register_blueprint(hands_blueprint)
app.register_blueprint(table_cards)



@app.route('/', methods=['GET'])

def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })