from flask import Flask, request 
app = Flask(__name__) 

languages = "Hello"

@app.route('/lang', methods=['GET'])
def returnAll():
	return "Hello Gamer"

@app.route('/lang', methods=['POST'])
def addOne():
	language = request.json['name']
	
	return (languages +' '+ str(language))


app.run() 