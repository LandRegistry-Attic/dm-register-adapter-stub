import os


from flask import Flask, jsonify


app = Flask(__name__)


app.config.from_object(os.environ.get('SETTINGS'))


@app.route("/")
def index():
    return "regad_stub"


@app.route('/get-proprietor-names/<title_number>', methods=["GET"])
def get_proprietor_names(title_number):
    return jsonify({'proprietor_names':
                      ['John Smith', 'John Smith', 'Janet Smith']})
