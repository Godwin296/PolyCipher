from flask import Blueprint, render_template

playfair_bp = Blueprint("playfair", __name__)


@playfair_bp.route("/")
def index():
    # TODO : traiter le formulaire (mot-clé, message, chiffrer / déchiffrer)
    return render_template("playfair.html")
