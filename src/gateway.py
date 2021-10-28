from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/gateway', methods=['POST', 'GET'])
def gateway():
  if request.method == 'POST':
    n1 = request.form['n1']
    n2 = request.form['n2']
    opr = request.form['opr']
    if opr == "seno":
      response = requests.post('http://localhost:5003/seno', data={'n1': n1})
    elif opr == "soma":
      response = requests.post('http://localhost:5002/soma', data={'n1': n1, 'n2': n2})
    else:
      response = requests.post('http://localhost:5002/subt', data={'n1': n1, 'n2': n2})
      
    requests.post('http://localhost:5005/logs', data={'n1': n1, 'n2': n2, 'opr': opr})
    return jsonify({'resultado': response.text})
  else:
    response = requests.get('http://localhost:5005/logs')
    return response.text

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)