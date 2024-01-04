from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

slots_vector =[]
count = [0]

@app.post("/predict")
def predict():
     text = request.get_json().get("message")
     response = get_response(text,slots_vector,count)
     message = {"answer":response}
     return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
