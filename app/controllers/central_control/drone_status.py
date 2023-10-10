# app/controllers/central_control/drone_status.py
from flask import Blueprint, jsonify

central_control_drone_status = Blueprint('central_control_drone_status', __name__)

@central_control_drone_status.route('/drones/status', methods=['GET'])
def get_drones_status():
    # Retrieve and return the status of all drones in the system
    # Replace with actual data retrieval logic
    drone_statuses = [
        {'id': 1, 'name': 'Drone 1', 'status': 'active'},
        {'id': 2, 'name': 'Drone 2', 'status': 'idle'},
        # ...
    ]
    return jsonify(drone_statuses)
