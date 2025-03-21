from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import json
from urllib.request import urlopen
import sqlite3

# Initialisation de l'application Flask
app = Flask(__name__)  # ⚠️ Correction ici : __name__ permet à Flask de savoir où se trouve le point d'entrée de l'application

# Route d'accueil — simple texte HTML retourné
@app.route('/')
def home():
    return "<h1>Bienvenue sur l'API CryptoPython</h1>"

# Route pour chiffrer un message avec une clé donnée
@app.route('/encrypt/<string:key>/<string:message>')
def encrypt_message(key, message):
    try:
        key_bytes = key.encode()  # La clé reçue est une chaîne, on la convertit en bytes
        f = Fernet(key_bytes)  # On crée un objet Fernet avec cette clé
        encrypted = f.encrypt(message.encode())  # On chiffre le message
        return encrypted.decode()  # On renvoie le message chiffré (bytes → str)
    except Exception as e:
        return f"Erreur : {str(e)}"  # En cas d'erreur (clé invalide, etc.), on renvoie le message d'erreur

# Route pour déchiffrer un message chiffré avec une clé donnée
@app.route('/decrypt/<string:key>/<string:token>')
def decrypt_message(key, token):
    try:
        key_bytes = key.encode()  # Conversion de la clé en bytes
        f = Fernet(key_bytes)  # Création de l'objet Fernet avec la clé
        decrypted = f.decrypt(token.encode())  # Déchiffrement du token reçu
        return decrypted.decode()  # Retour du message original (bytes → str)
    except Exception as e:
        return f"Erreur : {str(e)}"  # Gestion des erreurs (clé incorrecte, token mal formé, etc.)

# Point d'entrée de l'application Flask
if __name__ == "__main__":  # ⚠️ Correction ici aussi
    app.run(debug=True)  # Démarrage de l'application en mode debug (pratique pour tester)
