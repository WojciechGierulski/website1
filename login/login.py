from flask import Blueprint
import flask
from flask import redirect, session, url_for, flash, render_template
from database.db_operations import db
from login.validator import check_create_acc_data, check_password_correct
from helpful_functions.functions1 import render_with_dict

login_bp = Blueprint("login", __name__, static_folder="static", template_folder="templates")


def pop_session():
    session.pop("user", None)

@login_bp.route("/", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        if "user" not in session:
            return render_with_dict("login.html")
        else:
            return redirect(url_for("gallery.user_page"))
    elif flask.request.method == "POST":
        login = flask.request.form["login"]
        password = flask.request.form["password"]
        sql_row_object = db.get_password(login)
        if check_password_correct(login, password, sql_row_object):
            session["user"] = login
            msg = "You have been logged in"
            flash(msg)
            return redirect(url_for("gallery.user_page"))
        else:
            msg = "Login or password is incorrect"
            flash(msg)
            return redirect(url_for("login.login"))


@login_bp.route("/logout")
def logout():
    if "user" in session:
        pop_session()
        flash("You have been logged out!")
        return redirect(url_for("login.login"))
    else:
        flash("You are not logged in")
        return redirect(url_for("login.login"))


@login_bp.route("/create_account", methods=["GET", "POST"])
def create_account():
    if flask.request.method == "GET":
        return render_with_dict("create.html")
    elif flask.request.method == "POST":
        login = flask.request.form["login"]
        password = flask.request.form["password"]
        c_password = flask.request.form["c_password"]
        result, msg = check_create_acc_data(login, password, c_password, db)
        if not result:
            flash(msg)
            return redirect(url_for("login.create_account"))
        else:
            if db.add_record(login, password):
                flash(msg)
                session["user"] = login
                return redirect(url_for("gallery.user_page"))
            else:
                msg = "Something went wrong when creating account, please try again later"
                flash(msg)
                return redirect(url_for("login.create_account"))
