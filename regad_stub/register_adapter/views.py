"""
The endpoint of the regad_stub application.
"""


import json


from flask import Blueprint


register_adapter = Blueprint('register_adapter',  __name__)


@register_adapter.route('/', methods=["GET"])
def index():
    return 'OK'


@register_adapter.route('/get-borrower-names', methods=["GET"])
def get_borrower_names():
    return json.dumps({'borrower_names':
                      ['Arrietty Clock', 'Pod Clock', ' Homily Clock',
                       'Hendreary Clock', 'Lupy Rain-Pipe Harpsichord Clock',
                       'Eggletina Clock']})
