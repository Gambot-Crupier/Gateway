from firebase_admin import messaging

def create_topic(players_list, game_id):
    topic = 'Gambot'
    response = messaging.subscribe_to_topic(players_list, topic)

    return response

def message_app(data, game_id):
    players_list = PlayerInGame.query.filter_by(game_id = game_id).all()
    
    for player in players_list:
        message = messaging.Message(data = data, token = player.device_id)
        response = messaging.send(message)

    return response