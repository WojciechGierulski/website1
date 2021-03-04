from helpful_functions.functions1 import render_with_dict
from flask import Blueprint
from flask import redirect, session, url_for, flash, render_template
from database.db_operations import db

admin_bp = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

def check_if_admin():
    admins = db.get_all_names("admins")
    if session["user"] in [row["login"] for row in admins]:
        return True
    else:
        return False


@admin_bp.route("/")
def main_admin_page():
    if "user" not in session:
        return redirect(url_for("home_page"))
    else:
        if check_if_admin():
            return render_with_dict("admin_main_page.html")
        else:
            return redirect(url_for("home_page"))