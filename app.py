from flask import Flask, Response, request
import base64

app = Flask(__name__)

answer = 42

@app.route('/')
def hello():
    return 'Hello, World!'
	
@app.route('/exercise')
def get_exercise():
    return 'Your objective is to blablabla'

@app.route('/test')
def get_file():
	with open("file.txt", "rb") as file:
		string = base64.b64encode(file.read())
		return Response(string, status=200, mimetype='application/json')
		

@app.route('/answer', methods = ['POST'])
def submit_answer():
	data = request.get_json()
	if int(data['answer']) == answer:
		return Response('{"valid":true}', status=201, mimetype='application/json')
	else:
		return Response('{"valid":false}', status=418, mimetype='application/json')

if __name__ == '__main__':
	app.run()