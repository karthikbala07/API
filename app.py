from flask import Flask, request 
app = Flask(__name__) 

languages = "Hello"

@app.route('/', methods=['GET'])
def returnAll():
	return "Hello GuruJi"

@app.route('/', methods=['POST'])
def addOne():
	language = request.json['name']
	
	return (languages +' '+ str(language))

if __name__ == '__main__':
	app.run() 
