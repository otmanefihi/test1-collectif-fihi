import os
from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def accueil():
        return jsonify({
            "application": "Atelier DevOps",
            "version": os.environ.get("APP_VERSION", "0.2.0")
        })

    @app.errorhandler(404)
    def introuvable(error):
        return jsonify({"erreur": "Ressource introuvable"}), 404

    # Ajouter les nouvelles routes avant return app.
    @app.get("/salutation")
    def salutation():
        nom = request.args.get("nom", "").strip()
        if not 1 <= len(nom) <= 30:
            return jsonify({"erreur": "Le nom doit contenir entre 1 et 30 caracteres"}), 400
        return jsonify({"message": f"Bonjour {nom}"})
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
