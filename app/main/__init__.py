from flask import Blueprint

wvar_main = Blueprint('wvar_main', __name__)

from . import routes 