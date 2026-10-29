import os
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def accueil():
        return jsonify({
            "application": "Atelier DevOps",
            "version": os.environ.get("APP_VERSION", "0.2.0")
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok",
            "version": os.environ.get("APP_VERSION", "0.2.0")
        }), 200

    @app.errorhandler(404)
    def non_trouve(e):
        return jsonify({"erreur": "Ressource introuvable"}), 404

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)