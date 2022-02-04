from flask import Blueprint, request, jsonify
from app.vehicles.controllers import create_vehicle_expedient, get_vehicle_expedient

vehicles = Blueprint('vehicles', __name__, url_prefix='/vehicles')

@vehicles.route("/", methods=['POST'])
def post_vehicle():
    try:
        if request.get_json():
            if create_vehicle_expedient(request.get_json()):
                e = get_vehicle_expedient(request.json['VIN']) 
                print(f'Vehicle register {e.VIN} has been created')        
                return jsonify(success=True, VIN_vehicle=e.VIN), 201
            else:
                return jsonify(success=False, message=f"Vehicle {request.json['VIN']} is already registered"), 409
    except Exception as e:
        print(e)
        return jsonify(success=False), 400