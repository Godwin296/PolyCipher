"""Configuration de l'application (valeurs lues depuis l'environnement)."""
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-a-changer")
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
