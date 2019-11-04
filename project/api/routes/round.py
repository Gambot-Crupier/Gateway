from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os

round_blueprint = Blueprint('round_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')


@round_blueprint.route('/get_player_money', methods=['GET'])
def get_player_money():
    try:
        url = base_game_url + "get_player_money"
        params={"player_id": request.args.get('player_id'), "game_id": request.args.get('game_id')}

        get_player_money_request = requests.request("GET", url, params=params)


        if get_player_money_request.status_code is 200:
            return jsonify(get_player_money_request.json()), 200
        else:
            return jsonify({ 'message': get_player_money_request.json()['message'] }), 406

    except Exception as e:
        return jsonify({"error": "Error on starting Game", "message": str(e)}), 500
