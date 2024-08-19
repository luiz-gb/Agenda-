from flask import Flask, render_template, request, redirect, url_for, flash
from usuarios import *
import json

app = Flask(__name__)
app.secret_key = "NSNS2UQ8Q6FDQ6FSBA6"


@app.route("/Login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        cpf = request.form.get("cpf")
        senha = request.form.get("senha")

        with open("usuarios.json") as usuariosA:
            usuarios = json.load(usuariosA)

            usuario_valido = False
            for usuario in usuarios:
                if usuario["matricula"] == cpf and usuario["senha"] == senha:
                    usuario_valido = True
                    break

            if usuario_valido:
                return redirect(url_for("home_page"))

            else:
                # Se não encontrar o usuário, mostrar mensagem de erro
                flash("Usuário inválido", "error")
                return redirect(url_for("login_page"))

    else:
        return render_template("login.html")


@app.route("/Home")
def home_page():
    return render_template("home.html")


@app.route("/Cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form.get("nome_usuario")
        matricula = request.form.get("cpf")
        email = request.form.get("email")
        senha = request.form.get("senha")
        turma = request.form.get("selecionarturma")

        cliente1 = Cliente(nome, matricula, email, senha, turma)

        cliente1.guardar_usuario()
        return render_template("cadastro.html")

    else:
        return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)
