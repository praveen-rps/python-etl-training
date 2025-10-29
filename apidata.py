from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

@app.route("/posts", methods=['GET'])
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    return jsonify(posts)


@app.route("/posts/<int:id>", methods=['GET'])
def get_posts_id_data(id):
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url, params={'id': id})
    posts = response.json()
    return jsonify(posts)



if __name__ == "__main__":
    app.run(debug=True, port=5001)