from flask import Flask

def create_app(config_name):
    app = Flask(__name__)  
    app.config['FLASK_RUN_PORT'] = "5001"
    return app