from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys

round_blueprint = Blueprint('round_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')
base_player_url = os.getenv('GAMBOT_PLAYER_URL')

@round_blueprint.route('/device_id_list', methods=['POST']):
def get_device_id():
    player_url = base_player_url + "get_device_id"
    player_list = request.get_json()

    response = requests.request("POST", player_url, data = player_list
                                headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
    
    if response.status_code is 200:
        return jsonify({
            "data": response.device_id_list
        }), 200
    else :
        return jsonify({"
            'message': 'Erro ao receber device_id!'
        }), 400