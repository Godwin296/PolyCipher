# PolyCipher

PolyCipher est un outil de chiffrement et de déchiffrement de messages basé sur un algorithme polygrammique, à savoir Hill et Playfair. L'interface web est construite avec Flask.

## Structure du projet

```
polycipher/
├── app/
│   ├── __init__.py        # création de l'application Flask
│   ├── routes.py          # routes web
│   ├── ciphers/
│   │   ├── hill.py        # chiffre de Hill
│   │   └── playfair.py    # chiffre de Playfair
│   ├── templates/         # pages HTML (Jinja2)
│   └── static/css/        # styles
├── tests/                 # tests (pytest)
├── run.py                 # point d'entrée
├── requirements.txt
└── README.md
```

## Installation

Python 3.14 est utilisé par tout le groupe.

```
git clone https://github.com/Godwin296/PolyCipher.git
cd PolyCipher
py -3.14 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer l'application

```
python run.py
```

Puis ouvrir http://127.0.0.1:5000 dans le navigateur.

## Règles de travail

- Une branche par fonctionnalité, puis une Pull Request vers `main`.
- Après l'installation d'un nouveau paquet : `pip freeze > requirements.txt` puis vérifier que le fichier est bien en UTF-8 (sous PowerShell, préférer `pip freeze | Out-File -Encoding utf8 requirements.txt`).
