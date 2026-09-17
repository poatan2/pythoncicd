from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.articles.fin({}, {'_id':False}))
    return jsonify({'all_articles':articles})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)