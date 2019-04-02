from flask import Flask, render_template, request
from classe import Pessoa

app = Flask(__name__)

pessoas = [
		Pessoa("Carlos","Rua Mantiqueira"),
		Pessoa("Aline", "Rua 7 de Setembro")
	]

@app.route("/")
def inicio():
	return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
	return render_template("listar_pessoas.html", lista = pessoas)

@app.route("/form_cadastrar_pessoa")
def form_cadastrar_pessoa():
	return render_template("form_cadastrar_pessoa.html")

@app.route("/cadastrar_pessoa", methods=['GET'])
def cadastrar_pessoa():
	nome = request.form.get("nome")
	endereco = request.form.get("endereco")
	dados = Pessoa(nome, endereco)
	pessoas.append(dados)

	return render_template("exibir_mensagem.html", mensagem="Cadastro bem sucedido!")

@app.route("/deletar_pessoa", methods=['POST'])
def deletar_pessoa():
	nome = request.form["nome"]
	endereco = request.form["endereco"]
	dados = Pessoa(nome, endereco)

	for pessoa in pessoas:
		if pessoa.nome == dados.nome:
			pessoas.remove(pessoa)

	return render_template("exibir_mensagem.html", mensagem = "Pessoa removida com sucesso!")

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
	return render_template("form_alterar_pessoa.html")

@app.route("/alterar_pessoa", methods=['POST'])
def alterar_pessoa():
	nome = request.form["nome"]
	endereco = request.form["endereco"]
	dados = Pessoa(nome, endereco)

	for pessoa in pessoas:
		if pessoa.nome == dados.nome:
			pessoas.append(dados)

	return render_template("exibir_mensagem.html", mensagem="Alteração feita com sucesso!")

app.run(host="0.0.0.0", debug=True)
