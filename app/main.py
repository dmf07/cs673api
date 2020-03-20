from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app)


@app.route('/upc/<string:upc>', methods=['GET'])
@cross_origin()
def get_upc(upc):
    r = requests.get(
        f'https://api.barcodespider.com/v1/lookup?token=df909e5de789bb50b764&upc={upc}')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
