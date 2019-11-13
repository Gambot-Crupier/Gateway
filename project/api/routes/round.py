from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os

round_blueprint = Blueprint('round_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')


@round_blueprint.route('/create_round', methods=['POST'])
def create_round():
    url = base_game_url + "create_round"

    try:
        create_round_request = requests.post(url)
        return jsonify(create_round_request.json()), create_round_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502



@round_blueprint.route('/get_round_bet', methods=['GET'])
def get_round_bet():
    url = base_game_url + "get_round_bet"
    params = {"round_id": request.args.get('round_id')}

    try:
        get_round_bet_request = requests.request("GET", url, params=params)
        return jsonify(get_round_bet_request.json()), get_round_bet_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502



@round_blueprint.route('/get_player_money', methods=['GET'])
def get_player_money():
    url = base_game_url + "get_player_money"
    params = {"game_id": request.args.get('game_id'), "player_id": request.args.get('player_id')}

    try:
        get_player_money_request = requests.request("GET", url, params=params)
        return jsonify(get_player_money_request.json()), get_player_money_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502



@round_blueprint.route('/get_player_bet', methods=['GET'])
def get_player_bet():
    url = base_game_url + "get_player_bet"
    params = {"game_id": request.args.get('game_id'), "player_id": request.args.get('player_id')}

    try:
        get_player_bet_request = requests.request("GET", url, params=params)
        return jsonify(get_player_bet_request.json()), get_player_bet_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502
