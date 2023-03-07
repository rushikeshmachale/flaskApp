from flask import Flask, jsonify,request


import pickle
import numpy as np
app = Flask(__name__)


@app.route('/')
def index():
    return "Chalu ahe"

@app.route('/predict')
def home():
#     return "Chalu ahe ha pn route"
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')


    input_query = np.array([[cgpa,iq,profile_score]])
    result = model.predict(input_query)[0]
    
    return jsonify({'placement':result})

if __name__ == '__main__':
    app.run(debug=True)
