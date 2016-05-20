import json
import unittest

from regad_stub import app

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_service(self):
        response = self.app.get('/register-adapter/')
        self.assertEquals(200, response.status_code)

    def test_get_borrower_names(self):
        response = self.app.get('/register-adapter/get-borrower-names')
        expected = ['Arrietty Clock', 'Pod Clock', ' Homily Clock',
                    'Hendreary Clock', 'Lupy Rain-Pipe Harpsichord Clock',
                    'Eggletina Clock']
        self.assertEquals(expected, json.loads(response.data)['borrower_names'])
