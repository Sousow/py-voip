from flask import Flask, request, make_response
from plivo import plivoxml

app = Flask(__name__)

@app.route('/receive_call/', methods=['GET','POST'])
def speak_xml():
    # Generate a Speak XML with the details of the text to play on the call.
    response = (plivoxml.ResponseElement()
            .add(plivoxml.SpeakElement('Hello, you just received your first call')))
    return(response.to_string())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
