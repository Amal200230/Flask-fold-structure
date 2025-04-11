from flask import Blueprint, jsonify 

from APP.services.service import greet

my_bp = Blueprint('my_bp', __name__)

@my_bp.route('/hello', methods=['GET'])
def hello():
    message = greet()
    return jsonify({'message': message})


