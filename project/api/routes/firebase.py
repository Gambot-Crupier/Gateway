from firebase_admin import messaging

def create_topic(players_list, game_id):
    topic = 'Gambot'
    response = messaging.subscribe_to_topic(players_list, topic)

    return response

def message_app(data, game_id):
    topic = 'Gambot'
    message = messaging.Message(topic = topic, data = data)
    response = messaging.send(message)
    
    return response