from flask import Blueprint
from flask import jsonify
from flask import request
import requests

table_cards = Blueprint('table_cards', __name__)
base_url = "http://localhost:5003"

@table_cards.route('/post_table_cards', methods=['POST'])
def post_table_cards():
    cards_data = request.get_json()
    url = base_url + "post_table_cards"

    data = {
        "round_id": get_current_round(),
        "cards": cards_data
    }

    if cards_data is not None:
        post_table_cards_request = requests.request("POST", url, data = data)

        if post_table_cards_request['status'] is 200:
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
    get_table_cards_request = requests.request("GET", url, data=get_current_round())

    if get_table_cards_request['status'] is 200:
        return jsonify({
            'table_cards':  get_table_cards_request.args.get('table_cards')
        }), 200
    else:
        return jsonify({
            'message': 'Could not get table_cards'
        }), 400



# @TODO Recuperar ID do round atual
def get_current_round():
    return 1