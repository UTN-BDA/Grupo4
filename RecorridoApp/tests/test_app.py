import unittest
from flask import current_app
from app import create_app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        """Testea que la aplicación se haya creado correctamente."""
        self.assertIsNotNone(current_app)

if __name__ == '__main__':
    unittest.main()
