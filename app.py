from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import config


def create_app(conf_path="./config.py"):
    # Init app
    app = Flask(__name__)
    app.config.from_pyfile(conf_path)

    # Init SQLAlchemy and models
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = config.SECRET_KEY
    import models
    models.db.init_app(app)

    # Register views
    from views import site, auth
    app.register_blueprint(site)
    app.register_blueprint(auth, url_prefix='/auth')

    # Add auth provider
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(user_id)

    return app


def main():
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()
