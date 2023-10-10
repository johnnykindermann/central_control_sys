# app/controllers/mobile_app/drone_details.py
from flask import Blueprint, jsonify

mobile_app_drone_details = Blueprint('mobile_app_drone_details', __name__)

@mobile_app_drone_details.route('/drones/<int:drone_id>', methods=['GET'])
def get_drone_details(drone_id):
    # Retrieve and return details of a specific drone identified by drone_id
    # Replace with actual data retrieval logic
    drone_details = {
        'id': drone_id,
        'name': 'Drone 1',
        'status': 'active',
        'battery_percentage': 80,
        'last_mission_completed': 'Mission 123',
    }
    return jsonify(drone_details)
