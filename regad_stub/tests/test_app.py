
import unittest

from flask import json

from regad_stub import app


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/')
        self.assertEquals(200, response.status_code)

    def test_get_proprietor_names(self):
        response = self.app.get('/get-proprietor-names/dn100')
        expected = ['Ann Smith']
        self.assertEquals(expected,
                          json.loads(response.data)['proprietor_names'])
