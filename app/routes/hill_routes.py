from flask import Blueprint, render_template

hill_bp = Blueprint("hill", __name__)


@hill_bp.route("/")
def index():
    # TODO : traiter le formulaire (clé, message, chiffrer / déchiffrer)
    return render_template("hill.html")
