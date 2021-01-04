from flask import Blueprint

login_blueprint = Blueprint("login_blueprint", __name__, static_folder="static", template_folder="templates")