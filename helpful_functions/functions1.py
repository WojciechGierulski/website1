from flask import render_template, session


def create_dict(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        dict[key] = value
    return dict


def render_with_dict(url, dict=None):
    if dict is None:
        if "user" in session:
            dict = {"user": session["user"]}
        else:
            dict = {}
    return render_template(url, dict=dict)
