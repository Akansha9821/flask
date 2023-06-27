from flask import Flask
from .models import db
from .views import users_blueprint

def create_app():
    app = Flask(__name__)
    
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost:27017/mydatabase'
    }
    
    db.init_app(app)
    
    app.register_blueprint(users_blueprint)
    
    return app
