from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from ..tour.models import Tour
from . import admin_bp
from .forms import TourForm
from app.users.decorators import admin_required

@admin_bp.route("/admin/")
@login_required
@admin_required
def index():
    return render_template("admin/index.html")

@admin_bp.route("/admin/tours/")
@login_required
@admin_required
def list_tours():
    tours = Tour.get_all()
    return render_template("admin/tours.html", tours=tours)

@admin_bp.route("/admin/tour/", methods=['GET', 'POST'], defaults={'tour_id': None})
@login_required
@admin_required
def tour_form(tour_id):
    form = TourForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        date = form.date.data
        price = form.price.data
        tour = Tour( name=name, description= description, date=date, price=price)
        tour.save()
        return redirect(url_for('admin.list_tours'))
    return render_template("admin/tour_form.html", form=form)

@admin_bp.route("/admin/tour/<int:tour_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_tour_form(tour_id):
    """Actualiza un post existente"""
    tour = Tour.get_by_id(tour_id)
    if tour is None:
       abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del post.
    form = TourForm(obj=tour)
    if form.validate_on_submit():
        # Actualiza los campos del post existente
        tour.name = form.name.data
        tour.description = form.description.data
        tour.date= form.date.data
        tour.price=form.price.data
        tour.save()
        return redirect(url_for('admin.list_tours'))
    return render_template("admin/tour_form.html", form=form, tour=tour)

@admin_bp.route("/admin/tour/delete/<int:tour_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_tour(tour_id):
    tour = Tour.get_by_id(tour_id)
    if tour is None:
        abort(404)
    tour.delete()
    return redirect(url_for('admin.list_tours'))

from app.users.models import User
@admin_bp.route("/admin/users/")
@login_required
@admin_required
def list_users():
    users = User.get_all()
    return render_template("admin/users.html", users=users)


from .forms import TourForm, UserAdminForm

@admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
@login_required
@admin_required
def update_user_form(user_id):
    # Aquí entra para actualizar un usuario existente
    user = User.get_by_id(user_id)
    if user is None:
        abort(404)
    # Crea un formulario inicializando los campos con
    # los valores del usuario.
    form = UserAdminForm(obj=user)
    if form.validate_on_submit():
        # Actualiza los campos del usuario existente
        user.is_admin = form.is_admin.data
        user.save()
        return redirect(url_for('admin.list_users'))
    return render_template("admin/user_form.html", form=form, user=user)

@admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
@login_required
@admin_required
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user is None:
        abort(404)
    user.delete()
    return redirect(url_for('admin.list_users'))