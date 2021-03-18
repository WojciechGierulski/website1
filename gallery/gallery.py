from flask import Blueprint
from flask import redirect, session, url_for, request
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


def generate_unique_random_code(N=27):
    unique = False
    while not unique:
        unique = True
        photo_name = ''.join(
            random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))
        query = "SELECT photo_name FROM photos"
        records = db.get_records(query)
        for row in records:
            if row["photo_name"] == photo_name:
                unique = False
                break
    return photo_name


def save_file_to_disk(file, path, photo_name):
    file.stream.seek(0)
    file.save(os.path.join(path, photo_name))


def add_file_to_db(photo_name):
    today = str(date.today())
    query = f"INSERT INTO photos (login, photo_name, upload_date) VALUES ('{session['user']}', '{photo_name}', '{today}')"
    return db.execute_query(query)  # returns true if addition is successful


@gallery_bp.route("/user/")
def user_page():
    if "user" in session:
        return render_with_dict("user.html")
    else:
        return redirect(url_for("login.login"))


@gallery_bp.route('/images', methods=['GET', 'POST'])
def images():
    if "user" in session:
        path = os.path.join("gallery/", UPLOAD_FOLDER, session["user"] + "/")
        if request.method == 'POST':
            if 'file' not in request.files:
                return "", 400
            file = request.files['file']
            if file.filename == '':
                return "", 204
            if file and allowed_file(file.filename):
                if len(file.read()) < (20 * 1024 * 1024):
                    photo_name = generate_unique_random_code()
                    if add_file_to_db(photo_name):
                        try:
                            save_file_to_disk(file, path, photo_name)
                        except:
                            db.execute_query(f"DELETE FROM photos WHERE photo_name='{photo_name}'")
                        finally:
                            return redirect(url_for("gallery.images"))
                    else:
                        return "Error while saving your file", 400
                else:
                    return "File is too large (max size is 20MB)", 400
            else:
                return "File type not allowed (only images are allowed)", 400

        elif request.method == "GET":
            if not os.path.exists(path):
                os.mkdir(path)
            images_paths = get_images_paths(session["user"])
            dict = create_dict(user=session["user"], images=images_paths)
            return render_with_dict("images.html", dict)
    else:
        return redirect(url_for("login.login"))
