"""
The endpoint of the regad_stub application.
"""

from flask import request, Blueprint, Response
from regad_stub import app


helloworld = Blueprint('helloworld' , __name__)


@helloworld.route('/', methods=["GET"])
def index():
    """
    Say Hello.

    :return: The de-facto greeting.
    :rtype: str
    """
    app.logger.debug("Saying hello...")
    return 'Hello World!'
