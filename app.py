from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import config

# Init app
app = Flask(__name__)
app.config.from_object(config)

# Init SQLAlchemy and models
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config.SECRET_KEY
db = SQLAlchemy(app)
import models

# Add auth provider
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)


# Register views
# FIXME: blueprint is not working for some reason
# from views import views_bp
# app.register_blueprint(views_bp)
from views import *

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
