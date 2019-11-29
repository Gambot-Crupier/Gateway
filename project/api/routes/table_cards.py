from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys

table_cards = Blueprint('table_cards', __name__)
base_url = os.getenv('GAMBOT_CARD_URL')
base_game_url = os.getenv('GAMBOT_GAME_URL')

@table_cards.route('/post_table_cards', methods=['POST'])
def post_table_cards():
    data = request.get_json()
    url = base_url + "post_table_cards"
    url_get_round = base_game_url + "get_round"

    if data is not None:
        get_round_request = requests.get(url_get_round)
        round_id = get_round_request.json()['id']

        data['round_id'] = round_id
        post_table_cards_request = requests.request("POST", url, json = data)
        print(post_table_cards_request, file=sys.stderr)

        if post_table_cards_request.status_code is 200:
            return jsonify({
                'message': 'Table Cards were posted successfully' 
            }), 200
        else:
            return jsonify({
                'message': 'Could not post table_cards'
            }), 400
    else:
        return jsonify({
            'message': 'No data was passed'
        }), 400



@table_cards.route('/get_table_cards', methods=['GET'])
def get_table_cards():
    url = base_url + "get_table_cards"
    PARAMS = {"round_id": request.args.get('round_id')}
    
    get_table_cards_request = requests.request("GET", url, params=PARAMS)

    if get_table_cards_request.status_code is 200:
        return jsonify(get_table_cards_request.json()), 200
    else:
        return jsonify({
            'message': 'Could not get table_cards'
        }), 400