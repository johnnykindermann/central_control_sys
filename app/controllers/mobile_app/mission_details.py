# app/controllers/mobile_app/mission_details.py
from flask import Blueprint, jsonify

mobile_app_mission_details = Blueprint('mobile_app_mission_details', __name__)

@mobile_app_mission_details.route('/missions/<int:mission_id>', methods=['GET'])
def get_mission_details(mission_id):
    # Retrieve and return details of a specific mission identified by mission_id
    # Replace with actual data retrieval logic
    mission_details = {
        'id': mission_id,
        'name': 'Mission 1',
        'status': 'in-progress',
        'assigned_drones': [1, 2],
        'details': 'Sample mission details',
    }
    return jsonify(mission_details)
