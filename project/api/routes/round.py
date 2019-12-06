from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys

round_blueprint = Blueprint('round_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')
base_player_url = os.getenv('GAMBOT_PLAYER_URL')

@round_blueprint.route('/get_round_id', methods=['GET'])
def get_round_id():
    game_url = base_game_url + 'get_round_id'

    response = requests.request("GET", game_url)
    data = response.json()

    if response.status_code is 200:
        return jsonify({
            "round_id": data['round_id']
        }), 200
    else:
        return jsonify({
            "message": 'Could not get round_id'
        }), 400

@round_blueprint.route('/device_id_list', methods=['POST'])
def get_device_id():
    player_url = base_player_url + "list_device_id"
    player_list = request.get_json()

    response = requests.request("POST", player_url, data = player_list,
                                headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
    
    if response.status_code is 200:
        return jsonify({
            "data": response.device_id_list
        }), 200
    else :
        return jsonify({
            'message': 'Erro ao receber device_id!'
        }), 400

@round_blueprint.route('/create_round', methods=['POST'])
def create_round():
    game_url = base_game_url + "create_round"

    try:
        response = requests.request("POST", game_url,
                                    headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
        
        if response.status_code is 200:
            return jsonify({
                'message': 'Round criado com sucesso!'
            })
        else:
            return jsonify({
                'message': response.message
            }), 400
    except:
        return jsonify({
            "message": 'Erro ao se comunicar com o serviço de games.'
        }), 400

@round_blueprint.route('/get_round_bet', methods=['GET'])
def get_round_bet():
    url = base_game_url + "get_round_bet"
    params = {"round_id": request.args.get('round_id')}

    try:
        get_round_bet_request = requests.request("GET", url, params=params)
        return jsonify(get_round_bet_request.json()), get_round_bet_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502

@round_blueprint.route('/round_redirect', methods=['POST'])
def round_redirect():
    url = base_game_url + 'round_redirect'
    
    try:
        request = requests.request("POST", url)
        if request.status_code == 200:
            return jsonify({
                'message': 'boooom'
            }), 200
        else:
            return jsonify({
                'message': request.json()
            }), 400
    except Exception as e:
        return jsonify({
            'message': 'deu ruim'
        }), 400

@round_blueprint.route('/get_player_money', methods=['GET'])
def get_player_money():
    url = base_game_url + "get_player_money"
    params = {"game_id": request.args.get('game_id'), "player_id": request.args.get('player_id')}
    print(params)

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



@round_blueprint.route('/pay_bet', methods=['POST'])
def pay_bet():
    url = base_game_url + "pay_bet"
    data = request.get_json()

    try:
        pay_bet_request = requests.request("POST", url, json=data,
                           headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
        return jsonify(pay_bet_request.json()), pay_bet_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502



@round_blueprint.route('/get_round_actions', methods=['GET'])
def get_actions():
    url = base_game_url + 'get_round_actions'

    try:
        get_actions_request = requests.request("GET", url)
        return jsonify(get_actions_request.json()), get_actions_request.status_code
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400

@round_blueprint.route('/raise_bet', methods=['POST'])
def raise_bet():
    url = base_game_url + "raise_bet"
    data = request.get_json()

    try:
        raise_bet_request = requests.request("POST", url, json=data,
                            headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
        return jsonify(raise_bet_request.json()), raise_bet_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502



@round_blueprint.route('/leave_match', methods=['POST'])
def leave_match():
    url = base_game_url + "leave_match"
    data = request.get_json()

    try:
        leave_match_request = requests.request("POST", url, json=data,
                            headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
        return jsonify(leave_match_request.json()), leave_match_request.status_code

    except Exception as e:
        return jsonify({"error": "Error on Creating Round", "message": str(e)}), 502


@round_blueprint.route('/get_current_player', methods=['GET'])
def get_current_player():
    url = base_game_url + 'get_current_player'
    params = {'round_id': request.args.get('round_id')}

    try:
        current_player_request = requests.request("GET", url, params=params)
        return jsonify(
            current_player_request.json()
        ), current_player_request.status_code
    except Exception as e:
        return jsonify({
            "message": str(e)
        }), 400


@round_blueprint.route('/start_round', methods=['POST'])
def start_round():
    url = base_game_url + "start_round"

    try:
        start_round_request = requests.request("POST", url)
        return jsonify(start_round_request.json()), start_round_request.status_code

    except Exception as e:
        return jsonify({"error": "Erro ao tentar iniciar o round.", "message": str(e)}), 502





@round_blueprint.route('/get_continue', methods=['GET'])
def get_continue():

    url = base_game_url + "get_continue"

    try:
        get_continue_request = requests.request("GET", url)
        return jsonify(get_continue_request.json()), get_continue_request.status_code

    except Exception as e:
        return jsonify({"error": "Erro ao tentar recuperar continuidade.", "message": str(e)}), 502



@round_blueprint.route('/post_continue', methods=['POST'])
def post_continue():

    data = request.get_json()
    url = base_game_url + "post_continue"

    try:
        post_continue_request = requests.request("POST", url, json=data,
                            headers = {'Accept': 'application/json', 'content-type' : 'application/json'})
        return jsonify(post_continue_request.json()), post_continue_request.status_code

    except Exception as e:
        return jsonify({"error": "Erro ao tentar mandar ação de continuidade.", "message": str(e)}), 502




@round_blueprint.route('/get_round', methods=['GET'])
def get_round():

    url = base_game_url + "get_round"

    try:
        get_round_request = requests.request("GET", url)
        return jsonify(get_round_request.json()), get_round_request.status_code

    except Exception as e:
        return jsonify({"error": "Erro ao tentar recuperar continuidade.", "message": str(e)}), 502