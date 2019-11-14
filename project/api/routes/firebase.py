from firebase_admin import messaging

def create_topic(players_list, game_id):
    topic = 'Partida' + game_id
    response = messaging.subscribe_to_topic(players_list, topic)

    return response

def message_app(data, game_id):
    topic = 'Partida' + game_id
    message = messaging.Message(topic = topic, data = data)
    response = messaging.send(message)
    
    return response