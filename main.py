import flask
from flask import Flask, render_template, redirect, session, url_for, flash, get_flashed_messages
import db_verf

app = Flask(__name__)
app.secret_key = "1234"


def render_with_dict(template):
    if "user" in session:
        user1 = session["user"]
    else:
        user1 = False
    return render_template(template, user=user1)


def pop_session():
    session.pop("user", None)


@app.route("/")
@app.route("/home")
def home_page():
    return render_with_dict("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        if "user" in session:
            return redirect(url_for("home_page"))
        else:
            return render_with_dict("login.html")
    elif flask.request.method == "POST":
        session["user"] = flask.request.form["login"]
        session["password"] = flask.request.form["password"]
        return redirect(url_for("home_page"))


@app.route("/logout")
def logout():
    if "user" in session:
        pop_session()
        flash("You have been logged out!")
        return redirect(url_for("login"))
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))


@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    if flask.request.method == "GET":
        return render_template("create.html")
    elif flask.request.method == "POST":
        login = flask.request.form["login"]
        password = flask.request.form["password"]
        c_password = flask.request.form["c_password"]


if __name__ == "__main__":
    app.run(debug=True)
