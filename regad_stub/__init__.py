import os


from flask import Flask, jsonify


app = Flask(__name__)


app.config.from_object(os.environ.get('SETTINGS'))


@app.route("/")
def index():
    return "regad_stub"


@app.route('/get-proprietor-names/<title_number>', methods=["GET"])
def get_proprietor_names(title_number):
    proprietor_names = {'GR314108': ["Ann Smith", "Ann Smith"],
                        'GR515835': ["Ann Smith"],
                        'GR517788': ["Ann Marie-Jones Smith", "Belinda Blue", "Charles John Morris Smith Jones"],

                        'AV182773': ["Lisa I'anson", "Ann Other"],
                        'GR517730': ["Liam Tremoille"]}.get(title_number, ["Ann Smith"])
    return jsonify({'proprietor_names': proprietor_names})
