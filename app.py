import json
from flask import Flask, jsonify, request

# data
from books import books

# init app
app = Flask(__name__)

# mock data
books = books

# routes
@app.route('/books', methods=['GET'])

# return books list as json data
def getBooks():
    return jsonify(books);

# run app
if __name__ == '__main__':
    app.run(port=3002)