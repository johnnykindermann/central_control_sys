# app/controllers/mobile_app/mission_history.py
from flask import Blueprint, jsonify

mobile_app_mission_history = Blueprint('mobile_app_mission_history', __name__)

@mobile_app_mission_history.route('/missions/history', methods=['GET'])
def get_mission_history():
    # Retrieve and return a history of completed missions
    # Replace with actual data retrieval logic
    mission_history = [
        {'id': 1, 'name': 'Mission 1', 'status': 'completed'},
        {'id': 2, 'name': 'Mission 2', 'status': 'completed'},
        # ...
    ]
    return jsonify(mission_history)
