from flask import request, jsonify
from app import app

from app.repository.user_repository import UserRepository

userRepository = UserRepository()


@app.route("/acesso", methods=['POST'])
def login():

    user = request.get_json()

    usuario = userRepository.getUserByLogin(user)

    if usuario is None:
        return "Usuario não encontrado", 404

    return True, 200


@app.route("/novousuario", methods=['POST'])
def new_user():
    try:
        user = request.get_json()
        userRepository.new_user(user)
        return "Ok", 200
    except:
        return "Ops, ocorreu um erro!", 500


@app.route("/usuarios", methods=['GET'])
def get_all_users():
    try:
        users = userRepository.get_all_users()
        return jsonify(users), 200
    except:
        return "Ops, ocorreu um erro!", 500
