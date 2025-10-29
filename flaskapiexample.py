from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John Doe", "position": "Developer"},
    {"id": 2, "name": "Jane Smith", "position": "Manager"},
    {"id": 3, "name": "Emily Davis", "position": "Designer"}
]

@app.route("/employees", methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route("/employees", methods=['POST'])
def add_employees():
    emp = request.get_json()
    employees.append(emp)
    return jsonify({"message": "Employee added successfully"}), 201



@app.route("/hello", methods=['POST','GET'])
def greet():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Hello, World..!, see you again!"

@app.route("/put", methods=['PUT'])
def put():
    return "Put method is called..!"

@app.route("/del", methods=['DELETE'])
def deleted():
    return "Delete method is called..!"


if __name__ == "__main__":
        app.run(debug=True, port=5000)