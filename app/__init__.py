from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models.tables import db
from .models.user import User


def create_app():
    app = Flask(__name__, template_folder="views", static_folder="static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///priv.db'
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from .controllers.auth_controller import bp as auth_bp
    from .controllers.group_controller import bp as group_bp
    from .controllers.kids_controller import bp as kids_bp
    from .controllers.prep_controller import bp as prep_bp
    from .controllers.priv_controller import bp as priv_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(kids_bp)
    app.register_blueprint(prep_bp)
    app.register_blueprint(priv_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    # Create database tables and admin user
    with app.app_context():
        db.create_all()

        from .models.user import UserRepo
        repo = UserRepo()
        if not repo.get_by_username('admin'):
            repo.add('admin', 'password123')

    return app