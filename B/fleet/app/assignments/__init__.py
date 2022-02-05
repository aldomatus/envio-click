from email import message
from flask import Blueprint, request, jsonify
from app.assignments.controllers import create_assignment_expedient, get_assignment_expedient, get_driver_assignments, cancel_driver_assignments

assignments = Blueprint('assignments', __name__, url_prefix='/assignments')

@assignments.route("/", methods=['POST'])
def post_assignment():
    try:
        if request.get_json():
            assignment = create_assignment_expedient(request.get_json())
            if assignment[1]:
                e = get_assignment_expedient(assignment[0]['driver_id'], assignment[0]['vehicle_id']) 
                print(f'Assignment with driver: {str(e.driver_id)} and {str(e.vehicle_id)} has been created')        
                return jsonify(success = True, message=f"assignment with driver: {assignment[0]['driver_id']} and vehicle: {assignment[0]['vehicle_id']} has been registered"), 201
            else:
                return jsonify(success=False, message=f"assignment with driver: {request.get_json()['driver_email']} and vehicle: {request.get_json()['VIN']}is already registered"), 409
    except Exception as e:
        print(e)
        return jsonify(success=False), 400


@assignments.route("/get_assignment/<driver_email>", methods=['GET'])
def get_assignment_driver(driver_email):
    try:
        assignments = get_driver_assignments(driver_email)
        if assignments:
            print(f"{driver_email} assignments successfully obtained")        
            return jsonify(success = True, data=assignments), 200
        else:
            return jsonify(success=False, message=f"Driver {driver_email} has no assigned vehicles"), 409
    except Exception as e:
        print(e)
        return jsonify(success=False, message='something has gone wrong!'), 400


@assignments.route("/cancel_assignment/<driver_email>/<VIN>", methods=['PUT'])
def cancel_assignment_driver(driver_email, VIN):
    try:
        assignments = cancel_driver_assignments(driver_email, VIN)
        if assignments:
            print(f"Assignment {driver_email} and {VIN} canceled")        
            return jsonify(success = True, assignment_canceled = assignments), 200
        else:
            return jsonify(success=False, message=f"Driver {driver_email} has no assigned vehicles"), 409
    except Exception as e:
        print(e)
        return jsonify(success=False, message='something has gone wrong!'), 400