from flask import Blueprint

wvar_auth = Blueprint('wvar_auth', __name__)

from . import routes 