from flask import Blueprint, request, jsonify
from app.assignments.controllers import create_assignment_expedient, get_assignment_expedient

assignments = Blueprint('assignments', __name__, url_prefix='/assignments')

@assignments.route("/", methods=['POST'])
def post_assignment():
    try:
        if request.get_json():
            if create_assignment_expedient(request.get_json()):
                e = get_assignment_expedient(request.json['email']) 
                print(f'User {e.email} has been created')        
                return jsonify(success=True,user=e.email), 201
            else:
                return jsonify(success=False, message=f"assignment {request.json['email']} is already registered"), 409
    except Exception as e:
        print(e)
        return jsonify(success=False), 400