# app/controllers/central_control/mission_assignment.py
from flask import Blueprint, jsonify, request

central_control_mission_assignment = Blueprint('central_control_mission_assignment', __name__)

# In-memory storage for drone data (replace with a database in a production application)
drones = [
    {'id': 1, 'name': 'Drone 1', 'status': 'active'},
    {'id': 2, 'name': 'Drone 2', 'status': 'idle'},
    # ...
]

# Sample mission data (replace with actual mission details)
missions = [
    {'id': 1, 'name': 'Mission 1', 'details': 'Sample mission details'},
    {'id': 2, 'name': 'Mission 2', 'details': 'Another mission'},
    # ...
]

@central_control_mission_assignment.route('/missions/assign', methods=['POST'])
def assign_mission():
    try:
        data = request.json  # Assuming the data is sent as JSON

        # Validate required fields (e.g., mission_name, drone_ids, mission_details)
        required_fields = ['mission_name', 'drone_ids', 'mission_details']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        # Retrieve mission details
        mission_name = data['mission_name']
        mission_details = data['mission_details']

        # Retrieve selected drone IDs
        selected_drone_ids = data['drone_ids']

        # Check the status of selected drones and assign the mission to active drones
        assigned_drones = []
        for drone in drones:
            if drone['id'] in selected_drone_ids and drone['status'] == 'active':
                assigned_drones.append(drone)
        
        # Store the mission assignment and return the response
        mission_assignment = {
            'mission_name': mission_name,
            'mission_details': mission_details,
            'assigned_drones': assigned_drones,
        }

        missions.append(mission_assignment)

        return jsonify({'message': 'Mission assigned successfully', 'assignment_details': mission_assignment}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
