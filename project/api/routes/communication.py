from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys


communication_blueprint = Blueprint('communication_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')
base_player_url = os.getenv('GAMBOT_PLAYER_URL')


@communication_blueprint.route('/post_player_id', methods=['POST'])
def post_player_id():
    try:
        res = {
            "message_player_position": '',
            "status_player_position": '',
            "message_player_id": '',
            "status_player_id": ''
        }
        
        url = base_game_url + "post_player_position"
        post_player_position_request = requests.post(url, params={"player_id": request.args.get('player_id')})
        
        res['message_player_position'] = post_player_position_request.json()['message']
        res['status_player_position'] = post_player_position_request.status_code


        url = base_player_url + "post_player_id"
        post_player_id_request = requests.post(url, params = {'player_id': request.args.get('player_id')})

        res['message_player_id'] = post_player_id_request.json()
        res['status_player_id'] = post_player_id_request.status_code

        return jsonify(res), post_player_id_request.status_code
       
    except Exception as e:
        return jsonify({"error": "Erro em mandar o Id do Player", "message": str(e)}), 500



@communication_blueprint.route('/post_ignore_player', methods=['POST'])
def post_ignore_player():
    try:
        url = base_player_url + "post_ignore_player"

        post_player_id_request = requests.post(url)

        return jsonify(post_player_id_request.json()), post_player_id_request.status_code
       
    except Exception as e:
        return jsonify({"error": "Erro em ignorar o player", "message": str(e)}), 500



@communication_blueprint.route('/post_end_recognition', methods=['POST'])
def post_end_recognition():
    try:
        url = base_player_url + "post_end_recognition"

        post_end_recognition_request = requests.post(url)

        return jsonify(post_end_recognition_request.json()), post_end_recognition_request.status_code
       
    except Exception as e:
        return jsonify({"error": "Erro ao terminar o reconhecimento do player", "message": str(e)}), 500



@communication_blueprint.route('/get_player_id', methods=['GET'])
def get_player_id():
    try:
        url = base_player_url + "get_player_id"

        get_player_id_request = requests.get(url)

        return jsonify(get_player_id_request.json()), get_player_id_request.status_code
       
    except Exception as e:
        return jsonify({"error": "Erro ao tentar recuperar o Id do player", "message": str(e)}), 500


@communication_blueprint.route('/distribuite_cards', methods=['GET'])
def distribuite_cards():
    try:
        url = base_game_url + "distribuite_cards"

        distribuite_cards_request = requests.get(url)

        return jsonify(distribuite_cards_request.json()), distribuite_cards_request.status_code
       
    except Exception as e:
        return jsonify({"error": "Erro ao tentar recuperar se as cartas devem ser distrubuídas", "message": str(e)}), 500
