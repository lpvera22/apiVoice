import flask
import requests
import base64
from flask import request, jsonify, Response
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>API root</h1>"


@app.route('/api/voice', methods=['POST'])
@cross_origin()
def voice():
    text = request.get_json()['text']
    headers = {'Ocp-Apim-Subscription-Key': '3f3062d98b5b4e66896a777d281632c0', 'Content-Type': 'application/ssml+xml',
               'X-Microsoft-OutputFormat': 'audio-16khz-64kbitrate-mono-mp3 '}
    xml = """<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR"><voice 
    name="pt-BR-HeloisaRUS">""" + text + """</voice></speak> """
    r = requests.post("https://brazilsouth.tts.speech.microsoft.com/cognitiveservices/v1",
                      data=xml, headers=headers)
    # r.encoding = r.apparent_encoding

    return Response(r.content, mimetype="audio/mp3")


app.run()
