import pip
pip.main(['install','flask'])
pip.main(['install','flask-jsonpify'])
pip.main(['install','flask-restful'])
os.chdir('Desktop/Social Sensing/')

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

result = {'sports': [], 'entertainment': []}

@app.route('/getLocations', methods=['GET'])
def get():
    global result
    return jsonify(result)
        
@app.route('/putLocations', methods=['PUT'])
def put():
    global result
    result = request.get_json()
    return jsonify(result)

if __name__ == '__main__':
     app.run(port=5002)

