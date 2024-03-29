from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@localhost',27017)
db = client.flags

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/country', methods=['GET'])
def flag_get():
    country_receive = request.args.get('country_give')
    result = list(db.flags.find({'countryName': country_receive}, {'_id': False}))
    return jsonify({'result': 'success', 'flags_list': result})

# @app.route('/info', methods=['GET'])
# def send_country_info():

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)