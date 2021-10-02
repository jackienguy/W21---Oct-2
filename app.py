import mariadb
from flask import Flask, request, Response 
import json
import sys

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"

@app.route('/fruit', methods=['GET', 'POST', 'PATCH'])
def fruit():
    fruit_name = 'dragonfruit'
    if (request.method == 'GET'):
        resp = {
            "fruitName" : fruit_name
        }
        return Response (json.dumps(resp),
                        mimetype="application/json",
                        status=200)

    elif (request.method == 'POST'):
        data = request.json #this will give you the dictionary
        print(data)
        if (data.get('fruitName') != None): #to get disctionary data in python, use data.get('pass expected list). and return not None
            #Deafult response values and won't require multiple return points/ method
            resp = "Wrong fruit"
            code = 400
            if (data.get('fruitName') == fruit_name): #if the response data is what expect, change the data response and the code
                resp = "Correct fruit"
                code = 201

            return Response (resp,
                            mimetype="text/plain",
                            status=code)
                
        else:
            return Response("ERROR, MISSING ARGUEMENTS",
                            mimetype="text/plain", #if expected to return a json, should return a json instead of text
                            status=400) 

    elif (request.method == 'PATCH'):
        return Response("Endpoint under maintencance",
                        mimetype="text/plain",
                        status=503)
    else:
        print("something went wrong")


if(len(sys.argv) > 1):
    mode = sys.argv[1]
    if (mode == "production"):
        import bjoern
        host = "0.0.0.0"
        port = 5000
        print("Server is running in production")
        bjoern.run(app, host, port)
    elif(mode == "testing"):
        from flask_cors import CORS
        CORS(app)
        print("Server is running in testing mode, switch to production")
        app.run(debug=True)
    else:
        print("Invalid mode arguement, exiting")
        exit()
else:
    print("No arguement was provided")
    exit()
