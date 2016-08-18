import unittest
import json
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_can_enter_city(self):
        resp = self.client.post('/', {'city': 'Nairobi'})
        self.assertEqual(resp.status_code, 200)
