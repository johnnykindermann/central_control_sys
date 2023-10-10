# app/controllers/mobile_app/mission_feedback.py
from flask import Blueprint, jsonify, request

mobile_app_mission_feedback = Blueprint('mobile_app_mission_feedback', __name__)

@mobile_app_mission_feedback.route('/mission/<int:mission_id>/feedback', methods=['POST'])
def submit_mission_feedback(mission_id):
    # Allow users to submit feedback for completed missions
    data = request.json  # Assuming the data is sent as JSON
    # Process and store the feedback data
    return jsonify({'message': 'Mission feedback submitted successfully'})

@mobile_app_mission_feedback.route('/mission/<int:mission_id>/feedback', methods=['GET'])
def get_mission_feedback(mission_id):
    # Retrieve feedback for a specific completed mission
    # Replace with actual data retrieval logic
    feedback = {
        'mission_id': mission_id,
        'user_id': 1,
        'rating': 4,
        'comments': 'Great job on the mission!',
    }
    return jsonify(feedback)
