from flask import Flask , request ,render_template 
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client =  pymongo.MongoClient(MONGO_URI)
db = client.Assignment
collection = db['git data']

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/')
def home():

    return render_template('index1.html')  

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)        
    collection.insert_one(form_data)
    return 'Data Submitted Successfully'


if __name__ == '__main__':    

    app.run(debug=True)       