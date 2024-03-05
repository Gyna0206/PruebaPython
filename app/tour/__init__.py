from flask import Blueprint

tour_bp= Blueprint('tour', __name__, template_folder='templates')

from . import routes