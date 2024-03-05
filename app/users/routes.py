from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from urllib.parse import urlparse
from app import login_manager
from . import users_bp
from .forms import SignupForm, LoginForm
from .models import User


@users_bp.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('tour.index'))
    form = SignupForm()
    error=None
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
                # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya está siendo utilizado por otro usuario'
        else:
             # Creamos el usuario y lo guardamos
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('tour.index')
            return redirect(next_page)
    return render_template("singup_form.html", form=form)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('tour.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('tour.index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@users_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('tour.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))
