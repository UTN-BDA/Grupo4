import unittest
from sqlalchemy import text
from app import create_app, db

class DBConnectionTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_db_connection(self):
        """Testea que se pueda hacer una consulta simple a la base de datos."""
        result = db.session.execute(text("SELECT 'Hello world'")).fetchone()
        self.assertEqual(result[0], 'Hello world')

if __name__ == '__main__':
    unittest.main()
