
from flask import render_template, abort, redirect, url_for
from ..bookings.models import Booking
from . import bookings_bp
from werkzeug.exceptions import NotFound
from ..bookings.forms import BookingForm
from flask_login import  login_required, current_user

@bookings_bp.route("/bookings/<int:booking_id>", methods=['GET', 'POST'])
@login_required
def show_booking(booking_id):
        booking = Booking.get_by_id(booking_id)
        if booking is None:
            raise NotFound(booking_id)
        
        return render_template("booking_view.html", booking=booking)

@bookings_bp.route("/bookings/delete/<int:booking_id>/", methods=['POST', ])
@login_required
def delete_booking(booking_id):
   
    booking = Booking.get_by_id(booking_id)
    if booking is None:
        abort(404)
    booking.delete()
    return redirect(url_for('tour.index'))

@bookings_bp.route("/bookings")
@login_required
def show_bookings():
    user_id = current_user.id
    bookings = Booking.get_by_user_id(user_id)
    return render_template("booking_list.html", bookings=bookings)