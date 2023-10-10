# app/controllers/central_control/mission_list.py
from flask import Blueprint, jsonify

central_control_mission_list = Blueprint('central_control_mission_list', __name__)

@central_control_mission_list.route('/missions', methods=['GET'])
def get_mission_list():
    # Retrieve and return a list of all missions
    # Replace with actual data retrieval logic
    mission_list = [
        {'id': 1, 'name': 'Mission 1', 'status': 'completed'},
        {'id': 2, 'name': 'Mission 2', 'status': 'in-progress'},
        # ...
    ]
    return jsonify(mission_list)
