# main.py
from flask import Flask
from app.routes.central_control_routes import central_control_bp

app = Flask(__name__)

# Register the central control Blueprint
app.register_blueprint(central_control_bp, url_prefix='/central_control')

# ... (other app configurations and routes)
