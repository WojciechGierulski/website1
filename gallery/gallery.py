from flask import Blueprint
from flask import redirect, session, url_for, flash, request, current_app, send_from_directory
from helpful_functions.functions1 import render_with_dict, create_dict
from werkzeug.utils import secure_filename
import os
from datetime import date
from database.db_operations import db
import random
import string


gallery_bp = Blueprint("gallery", __name__, static_folder="static", template_folder="templates")

UPLOAD_FOLDER = "static/images/"
ALLOWED_EXTENSIONS = {"png", "jpg", "bmp"}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_images_paths(user_name):
    path = os.path.join("gallery/", UPLOAD_FOLDER, user_name + "/")
    images_paths = []
    for filename in os.listdir(path):
        images_paths.append(f"images/{user_name}/{filename}")
    return images_paths

def add_db_record(photo_name):
    today = str(date.today())
    query = f"INSERT INTO photos (login,photo_name,upload_date) VALUES ('{session['user']}','{photo_name}','{today}')"
    db.add_any_record(query)

def generate_random_code(N=27):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))

@gallery_bp.route("/user/")
def user_page():
    if "user" in session:
        return render_with_dict("user.html")
    else:
        return redirect(url_for("login.login"))

@gallery_bp.route('/images', methods=['GET', 'POST'])
def images():
    if "user" in session:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return "", 400
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                return "", 204
            if file and allowed_file(file.filename):
                if len(file.read()) < (30 * 1024 * 1024):
                    try:
                        filename = secure_filename(file.filename)
                        path = os.path.join("gallery/", UPLOAD_FOLDER, session["user"] + "/")
                        if not os.path.exists(path):
                            os.mkdir(path)
                        file.stream.seek(0)
                        file.save(os.path.join(path, filename))
                        add_db_record(filename)
                        return redirect(url_for("gallery.images"))
                    except:
                        return "Unknown error when uploading your image", 204
                else:
                    return "File is too large (max size is 10MB)", 400
            else:
                return "File type not allowed (only images are allowed)", 400
        elif request.method == "GET":
            images_paths = get_images_paths(session["user"])
            dict = create_dict(user=session["user"], images=images_paths)
            return render_with_dict("images.html", dict)
    else:
        return redirect(url_for("login.login"))