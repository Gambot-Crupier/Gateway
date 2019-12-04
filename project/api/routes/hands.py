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
        hands = request.get_json()
        # hands = hands_data['hands']

        url_get_round = base_game_url + "get_round"
        get_round_request = requests.get(url_get_round)
        
        round_id = get_round_request.json()['id']

        for hand in hands:
            hand['round_id'] = round_id

        url_post_hands = base_url + "post_hands"

        if hands is not None:
            post_hands_request = requests.post(url_post_hands, json = hands)

            return jsonify(post_hands_request.json()), post_hands_request.status_code
        else:
            return jsonify({ 'message': 'Nenhum dado foi passado!'}), 500
    
    except Exception as e:
        return jsonify({"error": "Erro ao tentar salvar as mãos dos jogadores", "message": str(e)}), 500


@hands_blueprint.route('/get_round_cards_number', methods=['GET'])
def get_round_cards_number():
    url = base_url + 'get_round_cards_number'
    round_id = request.args.get('round_id')
    params = {'round_id': round_id}

    cards_response = requests.request("GET", url, params = params)

    if cards_response.status_code is 200:
        return jsonify({
            'number': cards_response.json()
        }), 200
    else:
        return jsonify({
            'message': cards_response.json()
        }), 400


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
    player_list = request.get_json()

    get_winner_request = requests.request("POST", url, json = player_list,
                                        headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
    
    if get_winner_request.status_code is 200:
        data = get_winner_request.json()
        return jsonify({
            'winner': data['player_id']
        }), 200
    else:
        data = get_winner_request.json()
        return jsonify({
            'message': data['message']
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