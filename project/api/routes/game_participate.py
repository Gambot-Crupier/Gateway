from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys

player_in_game_blueprint = Blueprint('player_in_game_blueprint', __name__)
base_url = os.getenv('GAMBOT_GAME_URL')


@player_in_game_blueprint.route('/post_player_in_game', methods=['POST'])
def post_game_participate():
    player_in_game_data = request.get_json()
    url = base_url + "post_player_in_game"

    if player_in_game_data is not None:
        post_player_in_request = requests.post(url, json = json.dumps(player_in_game_data))

        if post_player_in_request.status_code is 200:
            return jsonify({
                'message': 'Player added to game'
            }), 200
        else:
            return jsonify({
                'message': 'Could not post player in game'
            }), 400
    else:
        return jsonify({
            'message': 'No data was passed'
        }), 400


@player_in_game_blueprint.route('/get_players_in_game', methods=['GET'])
def get_game_participate():
    url = base_url + "get_players_in_game"
    PARAMS = {"game_id": request.args.get('game_id')}
    
    post_player_in_request = requests.request("GET", url, params=PARAMS)

    if post_player_in_request.status_code is 200:
        return jsonify(post_player_in_request.json()), 200
    else:
        return jsonify({
            'message': 'Could not get players in game'
        }), 400
