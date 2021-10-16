from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/gateway', methods=['POST'])
def gateway():
    n1 = request.form['n1']
    n2 = request.form['n2']
    opr = request.form['opr']
    if opr == "seno":
      response = requests.post('http://localhost:5003/seno', data={'n1': n1})
    elif opr == "soma":
      response = requests.post('http://localhost:5002/soma', data={'n1': n1, 'n2': n2})
    else:
      response = requests.post('http://localhost:5002/subt', data={'n1': n1, 'n2': n2})

    return jsonify({'resultado': response.text})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)