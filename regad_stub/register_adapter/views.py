"""
The endpoint of the regad_stub application.
"""


from flask import Blueprint, jsonify


register_adapter = Blueprint('register_adapter',  __name__)


@register_adapter.route('/', methods=["GET"])
def index():
    return 'OK'


@register_adapter.route('/get-proprietor-names', methods=["GET"])
def get_proprietor_names():
    return jsonify({'proprietor_names':
                      ['John Smith', 'John Smith', 'Janet Smith']})
