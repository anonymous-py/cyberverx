from flask import Flask

from .extensions import db, migrate, bootstrap, login_manager
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .admin import admin as admin_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(user_id)


@login_manager.user_loader
def load_admin(admin_id):
    from .models import Admin
    return Admin.query.get(admin_id)
