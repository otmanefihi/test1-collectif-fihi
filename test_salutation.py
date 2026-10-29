import unittest
from app import create_app


class TestSalutation(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_nom_valide(self):
        response = self.client.get("/salutation", query_string={"nom": "Sara"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Bonjour Sara"})

    def test_espaces_autour_du_nom(self):
        response = self.client.get("/salutation", query_string={"nom": "  Sara  "})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Bonjour Sara"})

    def test_nom_absent(self):
        response = self.client.get("/salutation")
        self.assertEqual(response.status_code, 400)
        self.assertIn("erreur", response.get_json())

    def test_nom_vide(self):
        response = self.client.get("/salutation", query_string={"nom": ""})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erreur", response.get_json())

    def test_nom_uniquement_espaces(self):
        response = self.client.get("/salutation", query_string={"nom": "   "})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erreur", response.get_json())

    def test_nom_trop_long(self):
        response = self.client.get("/salutation", query_string={"nom": "a" * 31})
        self.assertEqual(response.status_code, 400)
        self.assertIn("erreur", response.get_json())

    def test_nom_limite_30_caracteres(self):
        response = self.client.get("/salutation", query_string={"nom": "a" * 30})
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
