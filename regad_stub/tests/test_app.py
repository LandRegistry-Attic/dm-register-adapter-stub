import json
import unittest

from regad_stub import app


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/register-adapter/')
        self.assertEquals(200, response.status_code)

    def test_get_proprietor_names(self):
        response = self.app.get('/register-adapter/get-proprietor-names')
        expected = ['John Smith', 'John Smith', 'Janet Smith']
        self.assertEquals(expected,
                          json.loads(response.data)['proprietor_names'])
