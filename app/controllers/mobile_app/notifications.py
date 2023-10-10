# app/controllers/mobile_app/notifications.py
from flask import Blueprint, jsonify

mobile_app_notifications = Blueprint('mobile_app_notifications', __name__)

@mobile_app_notifications.route('/notifications', methods=['GET'])
def get_notifications():
    # Retrieve user notifications
    # Replace with actual data retrieval logic
    notifications = [
        {'id': 1, 'message': 'Fire detected near your location'},
        {'id': 2, 'message': 'New drone mission assigned'},
        # ...
    ]
    return jsonify(notifications)

@mobile_app_notifications.route('/notifications/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    # Delete a specific notification identified by notification_id
    # Remove the notification from the user's list of notifications
    return jsonify({'message': 'Notification deleted successfully'})
