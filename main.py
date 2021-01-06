import flask
from flask import Flask, render_template, redirect, session, url_for, flash, get_flashed_messages
from db_operations import Database
from validator import check_create_acc_data

app = Flask(__name__)
app.secret_key = "1234"


db = Database()
db.init_db()


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
        return render_with_dict("create.html")
    elif flask.request.method == "POST":
        login = flask.request.form["login"]
        password = flask.request.form["password"]
        c_password = flask.request.form["c_password"]
        result, msg = check_create_acc_data(login, password, c_password, db)
        if not result:
            flash(msg)
            return redirect(url_for("create_account"))
        else:
            if db.add_record(login, password):
                flash(msg)
                session["user"] = login
                return redirect(url_for("user_page"))
            else:
                msg = "Something went wrong when creating account, please try again later"
                flash(msg)
                return redirect(url_for("create_account"))

@app.route("/user/")
def user_page():
    if flask.request.method == "GET":
        if "user" in session:
            return render_with_dict("user.html")
        else:
            return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
