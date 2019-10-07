from flask import Blueprint
from flask import jsonify
from flask import request
import requests, json

hands_blueprint = Blueprint('hands_blueprint', __name__)
base_url = "http://gambot_card:5000/"

@hands_blueprint.route('/post_hands', methods=['POST'])
def post_hands():
    hands_data = request.get_json()
    url = base_url + "post_hands"

    if hands_data is not None:
        post_hands_request = requests.post(url, json = json.dumps(hands_data))
        if post_hands_request.json()['status_code'] is 200:
            return jsonify({
                'message': 'Hands were posted successfully' 
            }), 200
        else:
            return jsonify({
                'message': 'Could not post hands'
            }), 400
    else:
        return jsonify({
            'message': 'No data was passed'
        }), 400


@hands_blueprint.route('/get_hands', methods=['GET'])
def get_hands():
    url = base_url + "get_hands"
    get_hands_request = requests.request("GET", url)

    if get_hands_request['status'] is 200:
        return jsonify({
            'hands':  get_hands_request.args.get('hands')
        }), 200
    else:
        return jsonify({
            'message': 'Could not get hands'
        }), 400