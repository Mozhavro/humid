import json
from flask import render_template, Blueprint, redirect, request, flash, url_for, current_app
from flask_login import login_user, logout_user, login_required

import models
import forms
from services import WeatherService


site = Blueprint('site', __name__)
auth = Blueprint('auth', __name__)


@site.route('/')
@login_required
def index():
    return render_template('index.html')


@site.route('/temperature-between-dates')
def get_temperature_between_dates():
    start = request.args.get('start')
    end = request.args.get('end')

    weather = WeatherService()
    data = weather.get_avg_temp_between_dates(start, end)
    return json.dumps(data)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or "/")

        flash('Invalid username or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        user = models.User(email=form.email.data,
                            username=form.username.data,
                            password=form.password.data)
        current_app.db.session.add(user)
        current_app.db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")
