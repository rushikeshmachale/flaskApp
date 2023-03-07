from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return "Chalu ahe"

@app.route('/predict')
def home():
    return "Chalu ahe ha pn route"


if __name__ == '__main__':
    app.run(debug=True)
