# app/controllers/mobile_app/resource_tracking.py
from flask import Blueprint, jsonify

mobile_app_resource_tracking = Blueprint('mobile_app_resource_tracking', __name__)

@mobile_app_resource_tracking.route('/resources/drones', methods=['GET'])
def get_nearby_drones():
    # Retrieve information about nearby drones on the mobile app
    # Replace with actual data retrieval logic
    nearby_drones = [
        {'id': 1, 'name': 'Drone 1', 'distance': 2.5},
        {'id': 2, 'name': 'Drone 2', 'distance': 1.8},
        # ...
    ]
    return jsonify(nearby_drones)

@mobile_app_resource_tracking.route('/resources/fire-incidents', methods=['GET'])
def get_nearby_fire_incidents():
    # Retrieve information about nearby fire incidents
    # Replace with actual data retrieval logic
    nearby_fire_incidents = [
        {'id': 1, 'intensity': 'high', 'distance': 3.2},
        {'id': 2, 'intensity': 'medium', 'distance': 1.5},
        # ...
    ]
    return jsonify(nearby_fire_incidents)
