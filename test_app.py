import unittest
from app import create_app

class TestApplicationInitiale(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_accueil(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        self.assertIn("application", response.get_json())
        self.assertIn("version", response.get_json())

    def test_route_inconnue(self):
        response = self.client.get("/route-inexistante")
        self.assertEqual(response.status_code, 404)
        self.assertIn("erreur", response.get_json())

if __name__ == "__main__":
    unittest.main()