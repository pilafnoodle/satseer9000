# app.py
from flask import Flask, jsonify, render_template
from script import fetch_tle_data  # Import the function from script.py

app = Flask(__name__)

@app.route('/get_tle', methods=['GET'])
def get_tle():
    # Call the function from script.py
    coordinates = [1234, 5678]#fetch_tle_data()
    sublong, sublat = coordinates
    return jsonify({'sublong': 1234, 'sublat': 5678})

@app.route('/')
def index():
    return render_template('index.html')
   
if __name__ == '__main__':
    app.run(debug=True, port=5000)