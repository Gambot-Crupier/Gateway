from flask import Blueprint
from flask import jsonify
from flask import request
import requests, json, os, sys

hands_blueprint = Blueprint('hands_blueprint', __name__)
base_url = os.getenv('GAMBOT_CARD_URL')
base_game_url = os.getenv('GAMBOT_GAME_URL')

@hands_blueprint.route('/post_hands', methods=['POST'])
def post_hands():
    try:
        hands_data = request.get_json()
        url_post_hands = base_url + "post_hands"
        url_get_round = base_game_url + "get_round"

        get_round_request = requests.get(url_get_round)
        round_id = get_round_request.json()['id']

        for hand in hands_data:
            hand['round_id'] = round_id
            print(hand, file=sys.stderr)

        if hands_data is not None:
            post_hands_request = requests.post(url_post_hands, json = hands_data)

            return jsonify(post_hands_request.json()), post_hands_request.status_code
        else:
            return jsonify({ 'message': 'Nenhum dado foi passado!'}), 500
    
    except Exception as e:
        return jsonify({"error": "Erro ao tentar salvar as mãos dos jogadores", "message": str(e)}), 500


@hands_blueprint.route('/get_hands', methods=['GET'])
def get_hands():
    url = base_url + "get_hands"
    PARAMS = {"round_id": request.args.get('round_id')}
    
    get_hands_request = requests.request("GET", url, params=PARAMS)

    if get_hands_request.status_code is 200:
        return jsonify(get_hands_request.json()), 200
    else:
        return jsonify({
            'message': 'Could not get hands'
        }), 400

@hands_blueprint.route('/get_winner', methods=['POST'])
def get_winner():
    url = base_url + 'get_winner'
    player_list = requests.get_json()

    get_winner_request = requests.request("POST", url, data = player_list,
                                        headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
    
    if get_winner_request.status_code is 200:
        return jsonify({
            'winner': get_winner_request.player_id
        }), 200
    else:
        return jsonify({
            'message': get_winner_request.message
        }), 400

@hands_blueprint.route("/get_player_hand", methods=["GET"])
def get_player_hand():
    url = base_url + "get_player_hand"
    PARAMS = {
        "round_id": request.args.get('round_id'),
        "player_id": request.args.get('round_id')
    }

    get_player_hand_request = requests.request("GET", url, params=PARAMS)

    if get_player_hand_request.status_code is 200:
        return jsonify(get_player_hand_request.json()), 200
    else:
        return jsonify({
            'message': 'Could not get hands'
        }), 400