# app/controllers/central_control/mission_status.py
from flask import Blueprint, jsonify

central_control_mission_status = Blueprint('central_control_mission_status', __name__)

@central_control_mission_status.route('/missions/<int:mission_id>', methods=['GET'])
def get_mission_status(mission_id):
    # Retrieve and return the status of a specific mission identified by mission_id
    # Replace with actual data retrieval logic
    mission_status = {
        'id': mission_id,
        'name': 'Mission 1',
        'status': 'in-progress',
        'assigned_drones': [1, 2],
        'completion_percentage': 60,
    }
    return jsonify(mission_status)
