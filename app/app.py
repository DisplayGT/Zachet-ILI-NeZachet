from flask import Flask, render_template
from app.controllers.priv_controller import bp as priv_bp
from app.controllers.group_controller import bp as group_bp
from app.controllers.prep_controller import bp as prep_bp
from app.controllers.kids_controller import bp as kids_bp
from app.controllers.auth_controller import bp as auth_bp
from app.models.tables import db
from app.models.user import User
from flask_login import LoginManager

app = Flask(__name__, template_folder="app/views", static_folder="app/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///priv.db'
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(priv_bp)
app.register_blueprint(group_bp)
app.register_blueprint(prep_bp)
app.register_blueprint(kids_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return render_template('index.html')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.models.user import UserRepo
with app.app_context():
    repo = UserRepo()
    if not repo.get_by_username('admin'):
        repo.add('admin', 'password123')

if __name__ == "__main__":
    app.run(debug=True)