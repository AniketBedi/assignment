from flask import Flask ,jsonify, request ,render_template 
from datetime import datetime
from dotenv import load_dotenv
import json
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client =  pymongo.MongoClient(MONGO_URI)
db = client.Assignment
collection = db['FLASK_ASSIGNMENT']

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A') 
    current_time = datetime.now().strftime('%H:%M:%S')

    print(day_of_week)

    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)  

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)        
    collection.insert_one(form_data)
    return 'Data Submitted Successfully'


if __name__ == '__main__':    

    app.run(debug=True)       