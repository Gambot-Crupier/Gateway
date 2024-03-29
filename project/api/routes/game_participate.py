from flask import Blueprint
from flask import jsonify
from flask import request
import requests, os, json, sys
from project.api.routes.firebase import message_app

player_in_game_blueprint = Blueprint('player_in_game_blueprint', __name__)
base_game_url = os.getenv('GAMBOT_GAME_URL')
base_player_url = os.getenv('GAMBOT_PLAYER_URL')

@player_in_game_blueprint.route('/post_player_in_game', methods=['POST'])
def post_game_participate():
    player_in_game_data = request.get_json()
    url = base_game_url + "post_player_in_game"

    if player_in_game_data is not None:
        post_player_in_request = requests.post(url, json = player_in_game_data)

        if post_player_in_request.status_code is 200:
            return jsonify(post_player_in_request.json()), post_player_in_request.status_code
        else:
            return jsonify(post_player_in_request.json()), post_player_in_request.status_code
    else:
        return jsonify({
            'message': 'No data was passed'
        }), 400

@player_in_game_blueprint.route('/get_user_by_id', methods=['GET'])
def get_player_name():
    player_url = base_player_url + 'get_user_by_id'
    user_id = request.args.get('user_id')
    params = {'user_id': user_id}

    player_request = requests.request("GET", player_url, params = params)

    if player_request.status_code is 200:
        return jsonify({
            'player': player_request.json()
        }), 200 


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
                return jsonify({'message': 'Could not get player with Id ' + str(player['player_id'])}), 400
        
        return jsonify(players_in_game), 200 
    else:
        return jsonify({'message': 'Could not get players in game'}), 400




@player_in_game_blueprint.route('/delete_player_in_game', methods=['DELETE'])
def delete_player_in_game():
    try:
        game_url = base_game_url + "delete_player_in_game"
        PARAMS={"player_id": request.args.get('player_id'), "game_id": request.args.get('game_id')}

        delete_player_request = requests.request("DELETE", game_url, params=PARAMS)
        
        if delete_player_request.status_code is 200:
            # print(delete_player_request.json(), file=sys.stderr)
            return jsonify(delete_player_request.json()), 200

        else:
            return jsonify(delete_player_request.json()), 400

    except Exception as e:
        return jsonify({"error": "Error on starting Game", "message": str(e)}), 500



@player_in_game_blueprint.route('/start_game', methods=['POST'])
def start_game():
    try:
        url = base_game_url + "start_game"
        start_game_request = requests.post(url)

        if start_game_request.status_code is 200:
            return jsonify({ 'message': 'Game Started' }), 200
        elif start_game_request.status_code == 406:
            return jsonify({ 'message': start_game_request.json()['message'] }), 406
        else:
            return jsonify({  'message': 'Could not start game' }), 400    

    except Exception as e:
        return jsonify({"error": "Error on starting Game", "message": str(e)}), 500



@player_in_game_blueprint.route('/get_players_money', methods=['GET'])
def get_players_money():
    try:
        url = base_game_url + "get_players_money"
        start_game_request = requests.get(url, params={"player_id": request.args.get('player_id')})


        if start_game_request.status_code is 200:
            return jsonify(start_game_request.json()), 200
        elif start_game_request.status_code == 406:
            return jsonify({ 'message': start_game_request.json()['error'] }), 406
        else:
            return jsonify({  'message': "Could not get player's money" }), 400

    except Exception as e:
        return jsonify({"error": "Error on getting player's money", "message": str(e)}), 500


def order_players(response):
    return response['money']
    

@player_in_game_blueprint.route('/get_players_ranking', methods=['GET'])
def get_players_ranking():
    game_url = base_game_url + "get_players_in_game"
    player_url = base_player_url + "get_user_by_id"

    get_players_id_request = requests.request("GET", game_url)


    if get_players_id_request.status_code is 200:
        players_in_game = get_players_id_request.json()

        response = {
            "players": []
        }

        for index, player in enumerate(players_in_game['players']):

            get_player_name_request = requests.request("GET", player_url, params={"user_id": player['player_id']})
            
            if get_player_name_request.status_code is 200:
                players_in_game['players'][index] = get_player_name_request.json()

                response['players'].append({
                    "player_id": player['player_id'],
                    "money": player['player_money'],
                    "player_name": players_in_game['players'][index]['name']
                })

            else:
                return jsonify({'message': 'Could not get player with Id'}), 400

        response["players"].sort(reverse= True, key=order_players)

        return json.dumps(response), 200  
    else:
        return jsonify({'message': 'Could not get players in game'}), 400

@player_in_game_blueprint.route('/get_total_players_in_game', methods=['GET'])
def get_total_players_in_game():
    try:
        url = base_game_url + "get_players_in_game"
        get_total_players_in_game_request = requests.request("GET", url)


        if get_total_players_in_game_request.status_code is 200:
            players_array = get_total_players_in_game_request.json()['players']
            players_qty = len(players_array)

            return jsonify({'qtd_players': players_qty}), 200
        else:
            return jsonify({ 'message': "Não foi possível recuperar a quantidade de jogadores." }), 400

    except Exception as e:
        return jsonify({"error": "Error on getting player's money", "message": str(e)}), 500
