from flask import Blueprint, render_template

cryptanalysis_bp = Blueprint("cryptanalysis", __name__)


@cryptanalysis_bp.route("/hill")
def hill():
    return render_template("cryptanalysis_hill.html")


@cryptanalysis_bp.route("/playfair")
def playfair():
    return render_template("cryptanalysis_playfair.html")
