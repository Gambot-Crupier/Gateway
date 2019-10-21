from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys

player_in_game_blueprint = Blueprint('player_in_game_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')
base_player_url = os.getenv('GAMBOT_PLAYER_URL')

@player_in_game_blueprint.route('/post_player_in_game', methods=['POST'])
def post_game_participate():
    player_in_game_data = request.get_json()
    url = base_game_url + "post_player_in_game"

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
    game_url = base_game_url + "get_players_in_game"
    player_url = base_player_url + "get_user_by_id"

    get_players_id_request = requests.request("GET", game_url)
    
    if get_players_id_request.status_code is 200:
        players_in_game = get_players_id_request.json()


        for index, player in enumerate(players_in_game['players']):
            get_player_request = requests.request("GET", player_url, params={"user_id": player['player_id']})
            
            if get_player_request.status_code is 200:
                players_in_game['players'][index] = get_player_request.json()
            else:
                return jsonify({'message': 'Could not get player with Id ' + player['player_id']}), 400

        return jsonify(players_in_game), 200 
    else:
        return jsonify({'message': 'Could not get players in game'}), 400
