from flask import Flask, request, jsonify
from loggin import login
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login_route():
    data = request.json
    username = data.get('user')
    password = data.get('password')
    if login(username, password):
        return jsonify({"success": True, "message": "Login exitoso"})
    else:
        return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"}), 401

if __name__ == '__main__':
    app.run(debug=True)