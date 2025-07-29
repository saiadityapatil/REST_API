import unittest
from flask_app.app import create_app
from unittest.mock import patch

class ApiTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    @patch('flask_app.customer.table')
    def test_get_missing_customer(self, mock_table):
        mock_table.get_item.return_value = {}
        resp = self.app.get('/customers/ABCDE')
        self.assertEqual(resp.status_code, 404)

    @patch('flask_app.customer.table')
    def test_create_customer(self, mock_table):
        mock_table.put_item.return_value = {}
        resp = self.app.post('/customers', json={'CustomerID':'X1','CompanyName':'TestCo'})
        self.assertEqual(resp.status_code, 201)
