from flask import Flask, render_template, request, redirect, url_for, flash, session
from usuarios import *
import json
from datetime import datetime


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
                session["usuario_logado"] = cpf
                return redirect(url_for("home_page"))

            else:
                # Se não encontrar o usuário, mostrar mensagem de erro
                flash("Usuário inválido", "error")
                return redirect(url_for("login_page"))

    else:
        return render_template("login.html")


@app.route("/Cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        nome = request.form.get("nome_usuario")
        matricula = request.form.get("cpf")
        email = request.form.get("email")
        senha = request.form.get("senha")
        turma = request.form.get("selecionarturma")

        cliente1 = Cliente(nome, matricula, email, senha, turma, "Sim")

        cliente1.guardar_usuario()

        flash("Usuário cadastrado")
        return redirect(url_for("cadastro"))

    else:
        return render_template("cadastro.html")


@app.route("/Home")
def home_page():
    if session.get("usuario_logado"):

        usuario_logado = session.get("usuario_logado")
        atividades = Atividade.pegar_atividades()

        dicionario = {}

        # filtrando as atividades por data
        for atividade in atividades:
            if atividade["criador"] == usuario_logado:
                data_atividade = atividade["data"]

                if data_atividade not in dicionario:
                    dicionario[data_atividade] = [atividade]
                else:
                    dicionario[data_atividade].append(atividade)
            else:
                pass
        # pegando as atividades e tempo que falta para elas chegarem

        data_de_hoje = datetime.now()

        dia_atual = int(data_de_hoje.day)
        mes_atual = int(data_de_hoje.month)
        ano_atual = int(data_de_hoje.year)

        lista_atividades_dias = []

        for atividade in atividades:

            if atividade["criador"] == usuario_logado:
                data_atividade = atividade["data"]
                print("oi")

                dia_atividade = int(data_atividade[:2])
                mes_atividade = int(data_atividade[3:5])
                ano_atividade = int(data_atividade[6:])

                if ano_atividade == ano_atual and mes_atividade == mes_atual:
                    tempo_falta = int(dia_atividade) - int(dia_atual)

                    lista_atividades_dias.append((atividade["titulo"], tempo_falta))

        if lista_atividades_dias:
            # organiza pelas atividades com menos dias
            lista_atividades_dias.sort(key=lambda x: x[1])

        # lista final
        lista_atividades = {}
        for titulo, tempo_falta in lista_atividades_dias[:5]:
            lista_atividades[titulo] = str(tempo_falta)

        # Adicionar "..." caso tenha mais de 5 atividades
        if len(lista_atividades_dias) > 5:
            lista_atividades["..."] = ""

        return render_template(
            "home.html",
            atividades=atividades,
            usuario_logado=usuario_logado,
            dicionario=dicionario,
            lista_atividades=lista_atividades,
        )

    else:
        return redirect(url_for("login_page"))


@app.route("/logout")
def logout():
    session.pop("usuario_logado", None)
    return redirect(url_for("login_page"))


@app.route("/Perfil")
def perfil():
    if session.get("usuario_logado"):

        usuarios = Cliente.pegar_usuarios()
        usuario_logado = session.get("usuario_logado")
        current_user = None

        # pegando usuário logado para enviar informações pra tela de login
        for usuario in usuarios:
            if usuario["matricula"] == usuario_logado:
                current_user = usuario
            else:
                pass

        # fazendo a senha em *
        caracteres_senha = len(current_user["senha"])
        senha_apresentavel = "*" * caracteres_senha

        # pegando quantidade de atividades do usuário
        atividades = Atividade.pegar_atividades()

        quantidade_atividades = 0
        for atividade in atividades:
            if atividade["criador"] == current_user["matricula"]:
                quantidade_atividades += 1
            else:
                pass

        print(current_user)
        return render_template(
            "perfil.html",
            current_user=current_user,
            senha_apresentavel=senha_apresentavel,
            quantidade_atividades=quantidade_atividades,
        )
    else:
        redirect(url_for("login_page"))


@app.route("/Perfil-edit", methods=["GET", "POST"])
def perfil_edit():
    if session.get("usuario_logado"):
        if request.method == "POST":
            nome = request.form.get("input-nome")
            email = request.form.get("input-email")
            nova_senha = request.form.get("input-senha")

            users = Cliente.pegar_usuarios()
            for user in users:
                if session.get("usuario_logado") == user["matricula"]:
                    user["nome"] = nome
                    user["email"] = email
                    if nova_senha:
                        user["senha"] = nova_senha
                else:
                    pass

            Cliente.atualizar_usuarios(users)

            flash("Usuário Atualizado")
            return redirect(url_for("perfil"))

        else:
            usuarios = Cliente.pegar_usuarios()
            usuario_logado = session.get("usuario_logado")
            current_user = None

            # pegando usuário logado para enviar informações pra tela de login
            for usuario in usuarios:
                if usuario["matricula"] == usuario_logado:
                    current_user = usuario
                else:
                    pass

            # fazendo a senha em *
            caracteres_senha = len(current_user["senha"])
            senha_apresentavel = "*" * caracteres_senha

            # pegando quantidade de atividades do usuário
            atividades = Atividade.pegar_atividades()

            quantidade_atividades = 0
            for atividade in atividades:
                if atividade["criador"] == current_user["matricula"]:
                    quantidade_atividades += 1
                else:
                    pass

            print(current_user)
            return render_template(
                "perfil-edit.html",
                current_user=current_user,
                senha_apresentavel=senha_apresentavel,
                quantidade_atividades=quantidade_atividades,
            )
    else:
        redirect(url_for("login_page"))


@app.route("/Cadastro-Atividades", methods=["GET", "POST"])
def cadastro_atividades():

    if session.get("usuario_logado"):
        if request.method == "POST":
            titulo = request.form.get("titulo")
            descricao = request.form.get("descricao")
            data = request.form.get("data")

            # reforma da data
            dia = data[-2:]
            mes = data[-5:-3]
            ano = data[:4]
            data_reformada = dia + "/" + mes + "/" + ano

            visibilidade = request.form.get("selecionarvisibilidade")

            usuario_logado = session.get("usuario_logado")

            atividade1 = Atividade(
                titulo, descricao, data_reformada, visibilidade, usuario_logado
            )

            atividade1.guardar_atividade()
            return render_template("cadastro-atividades.html")

        else:
            return render_template("cadastro-atividades.html")

    else:
        redirect(url_for("login_page"))


if __name__ == "__main__":
    app.run(debug=True)
