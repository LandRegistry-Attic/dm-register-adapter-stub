import os
import pkg_resources
from flask import Flask


app = Flask(__name__)

from .register_adapter import views

app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(views.register_adapter, url_prefix='/register-adapter')

@app.route("/")
def index():
    return "regad_stub"
