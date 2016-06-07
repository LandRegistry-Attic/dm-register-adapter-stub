import os


from flask import Flask, jsonify


app = Flask(__name__)


app.config.from_object(os.environ.get('SETTINGS'))


@app.route("/")
def index():
    return "regad_stub"


@app.route('/get-proprietor-names/<title_number>', methods=["GET"])
def get_proprietor_names(title_number):
    proprietor_names  = {'CYM123456' : ["Ann Smith", "Ann Smith"],
	                 'CYM123457' : ["Ann Smith"],
	                 'CYM123458' : ["Ann Marie-Jones Smith", "Belinda Blue", "Charles John Morris Smith Jones"],
                     'CYM123459' : ["Lisa I'anson", "Ann Other"],
                     'CYM123461' : ["Ann-Marie Stacey Jane -Jones66 A'thénaïs* de Ligne de la Trémoïlle"],
                     'CYM123460' : ["Liam Tremoille"]}.get(title_number, ["Ann Smith"])
    print(proprietor_names)
    return jsonify({'proprietor_names': proprietor_names})
