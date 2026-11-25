"""PolyCipher : application Flask (chiffrement polygrammique Hill et Playfair)."""
from flask import Flask

from .config import Config


def create_app(config_class: type = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .routes.main_routes import main_bp
    from .routes.hill_routes import hill_bp
    from .routes.playfair_routes import playfair_bp
    from .routes.cryptanalysis_routes import cryptanalysis_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(hill_bp, url_prefix="/hill")
    app.register_blueprint(playfair_bp, url_prefix="/playfair")
    app.register_blueprint(cryptanalysis_bp, url_prefix="/cryptanalysis")

    return app
