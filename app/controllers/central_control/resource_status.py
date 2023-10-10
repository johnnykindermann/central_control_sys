# app/controllers/central_control/resource_status.py
from flask import Blueprint, jsonify

central_control_resource_status = Blueprint('central_control_resource_status', __name__)

@central_control_resource_status.route('/resources/drones', methods=['GET'])
def get_drones_status():
    # Retrieve real-time status information for all drones
    # Replace with actual data retrieval logic
    drone_statuses = [
        {'id': 1, 'name': 'Drone 1', 'status': 'active'},
        {'id': 2, 'name': 'Drone 2', 'status': 'idle'},
        # ...
    ]
    return jsonify(drone_statuses)

@central_control_resource_status.route('/resources/batteries', methods=['GET'])
def get_battery_status():
    # Retrieve battery status for all drones
    # Replace with actual data retrieval logic
    battery_statuses = [
        {'drone_id': 1, 'battery_percentage': 80},
        {'drone_id': 2, 'battery_percentage': 60},
        # ...
    ]
    return jsonify(battery_statuses)
