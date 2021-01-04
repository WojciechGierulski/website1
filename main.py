import flask
from flask import Flask, render_template, redirect, session, url_for, flash, get_flashed_messages
from db_verf import Db

app = Flask(__name__)
app.secret_key = "joiewf93jofnerwjb/3##"

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

@app.route("/create_account")
def create_account():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)