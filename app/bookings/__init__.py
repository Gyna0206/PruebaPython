from flask import Blueprint

bookings_bp= Blueprint('bookings', __name__, template_folder='templates')

from . import routes