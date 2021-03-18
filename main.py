from flask import Flask, render_template, redirect, session, url_for
from login.login import login_bp
from gallery.gallery import gallery_bp
from helpful_functions.functions1 import render_with_dict

app = Flask(__name__)
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(gallery_bp, url_prefix="/gallery")
app.secret_key = "1234"


@app.route("/")
@app.route("/home")
def home_page():
    if "user" in session:
        user = session["user"]
    else:
        user = None
    return render_with_dict("home.html")


if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.109', port=5000)
