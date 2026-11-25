# PolyCipher

PolyCipher est un outil de chiffrement et de déchiffrement de messages basé sur un algorithme polygrammique, à savoir Hill et Playfair. L'interface web est construite avec Flask.

## Structure du projet

```
polycipher/
├── app/
│   ├── __init__.py            # création de l'application Flask
│   ├── config.py              # configuration
│   ├── routes/                # routes web (Hill, Playfair, cryptanalyse, pages)
│   ├── services/              # logique métier (algorithmes, cryptanalyse, utilitaires)
│   ├── templates/             # pages HTML (Jinja2)
│   └── static/                # css, js, images
├── tests/                     # tests (pytest)
├── docs/                      # rapport, maquettes, diagrammes
├── .env.example               # modèle de fichier d'environnement
├── requirements.txt
└── run.py                     # point d'entrée
```

## Installation

Python 3.14 est utilisé par tout le groupe.

```
git clone https://github.com/Godwin296/PolyCipher.git
cd PolyCipher
py -3.14 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Lancer l'application

```
python run.py
```

Puis ouvrir http://127.0.0.1:5000 dans le navigateur.

## Lancer les tests

```
pip install pytest
python -m pytest
```

## Règles de travail

- Une branche par fonctionnalité, puis une Pull Request vers `main`.
- Après l'installation d'un nouveau paquet : `pip freeze | Out-File -Encoding utf8 requirements.txt` (PowerShell), pour garder le fichier en UTF-8.
