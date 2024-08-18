from flask import Flask, render_template, request, redirect, url_for, flash
from usuarios import *
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
import json

app = Flask(__name__)
app.secret_key = "leticiaelucastransammuito"

login_manager = LoginManager(app)
login_manager.login_view = "login"


@app.route("/Login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        cpf = request.form.get("cpf")
        senha = request.form.get("senha")

        with open("usuarios.json") as usuariosA:
            usuarios = json.load(usuariosA)

            for usuario in usuarios:
                if usuario["matricula"] == cpf and usuario["senha"] == senha:
                    return redirect(url_for("home_page"))

            # Se não encontrar o usuário, mostrar mensagem de erro
            flash("Usuário inválido")
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
