import os
from flask import Flask, jsonify
from project.api.routes.auth import auth_blueprint

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

app.register_blueprint(auth_blueprint)



@app.route('/', methods=['GET'])

def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })