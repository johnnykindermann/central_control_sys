# myflaskapp/central_control/__init__.py
from flask import Blueprint

# Create a Blueprint for the central control package
central_control_bp = Blueprint('central_control', __name__)

# Import routes from central_control_routes.py
from . import central_control_routes

# You can perform package-level initialization here if needed

# Optionally, you can add a context_processor to make data available to all templates
@central_control_bp.app_context_processor
def inject_global_data():
    # Add global data that should be available in templates
    global_data = {
        'global_variable': 'value',
    }
    return global_data
