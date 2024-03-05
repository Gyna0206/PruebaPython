from flask import render_template, current_app
from flask import  redirect, url_for

from .models import Tour
from ..bookings.models import Booking
from . import tour_bp
from werkzeug.exceptions import NotFound
from ..bookings.forms import BookingForm
from flask_login import  current_user, login_required

@tour_bp.route("/")
def index():
    current_app.logger.info('Mostrando los posts del blog')
    tours= Tour.get_all()
    return render_template("tour/index.html", tours=tours)


@tour_bp.route("/<string:slug>/",methods=['GET', 'POST'])
def show_tour(slug):
        tour = Tour.get_by_slug(slug)
        if tour is None:
            raise NotFound(slug)
        form = BookingForm()
        if current_user.is_authenticated and form.validate_on_submit():
            people = form.people.data
            booking = Booking(people=people, user_id=current_user.id,
                          user_name=current_user.name, tour_id=tour.id, tour_name=tour.name)
            booking.save()
            return redirect(url_for('tour.index', slug=tour.name_slug))
   
        return render_template("tour/tour_view.html", tour=tour, form=form)

