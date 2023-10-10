# app/controllers/central_control/fire_incident_management.py
from flask import Blueprint, jsonify, request

central_control_fire_incident_management = Blueprint('central_control_fire_incident_management', __name__)

@central_control_fire_incident_management.route('/fire-incidents', methods=['POST'])
def report_fire_incident():
    # Receive and process reported fire incidents
    data = request.json  # Assuming the data is sent as JSON
    # Process and store the data in the database
    return jsonify({'message': 'Fire incident reported successfully'})

@central_control_fire_incident_management.route('/fire-incidents/<int:incident_id>', methods=['GET'])
def get_fire_incident_details(incident_id):
    # Retrieve details of a specific fire incident identified by incident_id
    # Replace with actual data retrieval logic
    fire_incident_details = {
        'id': incident_id,
        'location': {'latitude': 37.9, 'longitude': -121.0},
        'intensity': 'high',
        'timestamp': '2023-10-15 15:30:00',
    }
    return jsonify(fire_incident_details)
