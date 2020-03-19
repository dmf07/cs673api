from flask import Flask, jsonify, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

upcs = [
    {
        'upc': '0012345678905',
        'title': u'Sample UPC',
        'description': u'This is a sample UPC',
        'imageUrl': u'https://www.upccode.net/sample_codes/UPC%20Code%20sample.jpg',
        'stores': [
            {
                "name": u'Walmart',
                "price": 100.00
            },
            {
                "name": u'Amazon',
                "price": 95.00
            },
            {
                "name": u'Target',
                "price": 100.00
            }
        ]
    }
]


@app.route('/upc', methods=['GET'])
@cross_origin()
def get_upcs():
    return jsonify(upcs)


@app.route('/upc/<string:upc>', methods=['GET'])
@cross_origin()
def get_upc(upc):
    for x in upcs:
        if x['upc'] == upc:
            return jsonify(x)
            break
        else:
            abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
