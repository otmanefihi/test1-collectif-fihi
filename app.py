import math
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

    @app.get("/conversion")
    def conversion():
        valeur_txt = request.args.get("valeur")
        unite = request.args.get("unite")
        if valeur_txt is None or unite is None:
            return jsonify({"erreur": "Parametres valeur et unite obligatoires"}), 400
        unite = unite.strip().upper()
        try:
            valeur = float(valeur_txt)
        except ValueError:
            return jsonify({"erreur": "La valeur doit etre un nombre"}), 400
        if not math.isfinite(valeur):
            return jsonify({"erreur": "La valeur doit etre un nombre fini"}), 400
        if unite == "C":
            resultat, unite_resultat = valeur * 9 / 5 + 32, "F"
        elif unite == "F":
            resultat, unite_resultat = (valeur - 32) * 5 / 9, "C"
        else:
            return jsonify({"erreur": "Unite inconnue, utiliser C ou F"}), 400
        return jsonify({
            "valeur_initiale": valeur,
            "unite_initiale": unite,
            "resultat": round(resultat, 2),
            "unite_resultat": unite_resultat
        })

    # Les nouvelles routes seront insérées ici avant le return
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
