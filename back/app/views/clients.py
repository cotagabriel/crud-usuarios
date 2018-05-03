#coding:utf-8

from flask import request, jsonify
from app.models.clients import Usuario
from app import app
from app import db
from app.controllers.clients import ControllerClients

@app.route('/usuario/cadastrar', methods=['POST'])
def cadastrar():
	try:
		data = request.get_json()
		controller = ControllerClients()
		controller.cadastrar(data['nome'], data['cpf'], data['celular'], data['email'], data['senha'])
		user_id = Usuario.query.order_by('-id').first().id
		return jsonify({"status": "ok", "msg": "Usuário cadastrado com sucesso!", "extra": user_id})
	except Exception as error:
		return jsonify({"status": "erro", "msg": error.message})

@app.route('/usuarios', methods=['GET'])
def listar():
	usuarios = Usuario.query.all()
	usuarios_all = []
	for usuario in usuarios:
		usuarios_all.append({"id":usuario.id, "nome": usuario.nome, "cpf": usuario.cpf, "celular": usuario.celular, "email": usuario.email, "senha": usuario.senha})
	return jsonify(usuarios_all)

@app.route('/usuario/alterar/<int:user_id>', methods=['PUT'])
def alterar(user_id):
	try:
		data = request.get_json()
		controller = ControllerClients()
		controller.alterar(user_id, data['nome'], data['cpf'], data['celular'], data['email'], data['senha'])
		return jsonify({"status": "ok", "msg": "Usuário alterado com sucesso!"})
	except Exception as error:
		return jsonify({"status": "erro", "msg": error.message})

@app.route('/usuario/remover/<int:user_id>', methods=['DELETE'])
def remover(user_id):
	try:
		data = request.get_json()
		controller = ControllerClients()
		controller.remover(user_id)
		return jsonify({"status": "ok", "msg": "Usuário removido com sucesso!"})
	except Exception as error:
		return jsonify({"status": "erro", "msg": error.message})
