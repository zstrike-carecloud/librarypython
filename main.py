from flask import Flask, jsonify
from pymongo import MongoClient
import sys

# client = MongoClient('mongodb://104.198.210.7')
# db = client.books  # Select the database
# print(f'DB! {db}', file=sys.stderr)
# users_collection = db.users  # Select the collection name
# print(f'users! {users_collection}', file=sys.stderr)

# print(f'Values! {users_collection.find()}', file=sys.stderr)
# users = [user for user in users_collection.find()]

# print(db.list_collection_names())

# print(f'HEY! {users}', file=sys.stderr)


# DEBUG = True
# HOST = '0.0.0.0'
# PORT = 8001

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify('Hello World')


if __name__ == '__main__':
    app.run()
    # app.run(debug=DEBUG, host=HOST, port=PORT)
