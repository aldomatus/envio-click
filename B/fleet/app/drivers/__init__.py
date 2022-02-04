from flask import Blueprint, request, jsonify
from app.drivers.controllers import create_driver_expedient, get_driver_expedient

drivers = Blueprint('drivers', __name__, url_prefix='/drivers')

@drivers.route("/", methods=['POST'])
def post_driver():
    try:
        if request.get_json():
            if create_driver_expedient(request.get_json()):
                e = get_driver_expedient(request.json['email']) 
                print(f'User {e.email} has been created')        
                return jsonify(success=True,user=e.email), 201
            else:
                return jsonify(success=False, message=f"Driver {request.json['email']} is already registered"), 409
    except Exception as e:
        print(e)
        return jsonify(success=False), 400