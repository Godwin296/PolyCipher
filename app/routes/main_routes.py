from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/history")
def history():
    return render_template("history.html")


@main_bp.route("/documentation")
def documentation():
    return render_template("documentation.html")
