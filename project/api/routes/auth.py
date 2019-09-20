from typing import List

from flask import Blueprint
from flask import jsonify
from flask import request
import requests

auth_blueprint = Blueprint('auth_blueprint', __name__)

"""
Nickname, email, password, password confirmation
"""
@auth_blueprint.route('/sign-up-gateway', methods=['POST'])
def sign_up_gateway():
    user_data = request.get_json()
    print(user_data)
    print(1)
    url = "http://localhost:5001/sign-up"

    if user_data is not None:
        print('oi')
        sign_up_request = requests.request("POST", url, data = user_data)

        print(sign_up_request)
        if sign_up_request['status'] is 200:
            return jsonify({
                'message': 'User account was created successfully' 
            }), 200
        else:
            return jsonify({
                'message': 'Could not create user account'
            }), 400
    else:
        print(2)
        return jsonify({
            'message': 'Could not reach Player server'
        }), 400
    
