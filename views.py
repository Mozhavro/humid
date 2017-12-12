from flask import render_template, Blueprint
from app import app


views_bp = Blueprint('views_bp', __name__)


@app.route('/')
# @login_required
def index():
    return render_template('index.html')