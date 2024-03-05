from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login_manager=LoginManager()
db = SQLAlchemy()

def create_app():   
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    db.init_app(app)
    migrate=Migrate (app,db)
    
    # Registro de los Blueprints
    from .users import users_bp
    app.register_blueprint(users_bp)
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    from .bookings import bookings_bp
    app.register_blueprint(bookings_bp)
    from .tour import tour_bp
    app.register_blueprint(tour_bp)

    return app


