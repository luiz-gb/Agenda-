from flask import Flask, render_template, request, redirect, url_for, flash, session
from usuarios import *
import json
from datetime import datetime
import yagmail


# img
from secrets import token_hex
from PIL import Image
import os

# email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.secret_key = "NSNS2UQ8Q6FDQ6FSBA6"

lideres = {
    "3º de Informática": "202214610020",
    "2º de Informática A": "202314610040",
    "2º de Informática B": "202314610012",
    "2º de de Meio Ambiente A": "202314710020",
    "2º de de Meio Ambiente B": "202314710019",
    "1º de Informática A": "202414610033",
    "1º de Informática B": "202414610080",
    "1º de Meio Ambiente A": "202414710015",
    "1º de Meio Ambiente B": "202414710068",
}


@app.route("/", methods=["GET", "POST"])
def landing_page():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        mensagem = request.form.get("descricao")

        suporte1 = Suporte(nome, email, mensagem)
        suporte1.guardar_suporte()

        return render_template("landing_page.html")
    else:
        return render_template("landing_page.html")


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

        lider = False
        for turmas in lideres:
            if lideres[turmas] == matricula:
                lider = True

        if lider:

            cliente1 = Cliente(nome, matricula, email, senha, turma, "s", "")
        else:
            cliente1 = Cliente(nome, matricula, email, senha, turma, "n", "")

        cliente1.guardar_usuario()

        flash("USUÁRIO CADASTRADO")
        return redirect(url_for("cadastro"))

    else:
        return render_template("cadastro.html")


@app.route("/Home")
def home_page():
    if session.get("usuario_logado"):

        # pegando o current
        usuarios = Cliente.pegar_usuarios()
        usuario_logado = session.get("usuario_logado")
        current_user = None

        # pegando usuário logado para enviar informações pra tela de login
        for usuario in usuarios:
            if usuario["matricula"] == usuario_logado:
                current_user = usuario
            else:
                pass

        usuario_logado = session.get("usuario_logado")
        atividades = Atividade.pegar_atividades()

        dicionario = {}

        # filtrando as atividades por data
        for atividade in atividades:
            if atividade["criador"] == usuario_logado:
                data_atividade = atividade["data"]

                if data_atividade not in dicionario:
                    dicionario[data_atividade] = {
                        "lista_atividades": [atividade],
                        "tipo": "privada",
                    }
                else:
                    dicionario[data_atividade]["lista_atividades"].append(atividade)
            elif atividade["visibilidade"] == "Público":
                dono_atividade = atividade["criador"]
                for turma in lideres:
                    if (
                        turma == current_user["turma"]
                        and lideres[turma] == dono_atividade
                    ):
                        data_atividade = atividade["data"]

                        if data_atividade not in dicionario:
                            dicionario[data_atividade] = {
                                "lista_atividades": [atividade],
                                "tipo": "publica",
                            }
                        else:
                            dicionario[data_atividade]["lista_atividades"].append(
                                atividade
                            )
                    else:
                        pass
            else:
                pass
        # pegando as atividades e tempo que falta para elas chegarem

        data_de_hoje = datetime.now()

        dia_atual = int(data_de_hoje.day)
        mes_atual = int(data_de_hoje.month)
        ano_atual = int(data_de_hoje.year)

        lista_atividades_dias = []

        for atividade in atividades:

            if (
                atividade["criador"] == usuario_logado
                and atividade["status"] == "Pendente"
            ):
                data_atividade = atividade["data"]

                dia_atividade = int(data_atividade[:2])
                mes_atividade = int(data_atividade[3:5])
                ano_atividade = int(data_atividade[6:])

                if (
                    ano_atividade == ano_atual
                    and mes_atividade == mes_atual
                    and dia_atividade >= dia_atual
                ):
                    tempo_falta = int(dia_atividade) - int(dia_atual)

                    lista_atividades_dias.append(
                        (atividade["titulo"], tempo_falta, "privada")
                    )

            elif (
                atividade["visibilidade"] == "Público"
                and atividade["status"] == "Pendente"
            ):
                dono_atividade = atividade["criador"]
                for turma in lideres:
                    if (
                        turma == current_user["turma"]
                        and lideres[turma] == dono_atividade
                    ):
                        data_atividade = atividade["data"]

                        dia_atividade = int(data_atividade[:2])
                        mes_atividade = int(data_atividade[3:5])
                        ano_atividade = int(data_atividade[6:])

                        if (
                            ano_atividade == ano_atual
                            and mes_atividade == mes_atual
                            and dia_atividade >= dia_atual
                        ):
                            tempo_falta = int(dia_atividade) - int(dia_atual)

                            lista_atividades_dias.append(
                                (atividade["titulo"], tempo_falta, "publica")
                            )
                    else:
                        pass

        if lista_atividades_dias:
            # organiza pelas atividades com menos dias
            lista_atividades_dias.sort(key=lambda x: x[1])

        # lista final
        lista_atividades = {}
        for titulo, tempo_falta, tipo in lista_atividades_dias[:5]:
            lista_atividades[titulo] = {"dias_falta": str(tempo_falta), "tipo": tipo}

        # Adicionar "..." caso tenha mais de 5 atividades
        if len(lista_atividades_dias) > 5:
            lista_atividades["..."] = ""

        return render_template(
            "home.html",
            atividades=atividades,
            usuario_logado=usuario_logado,
            dicionario=dicionario,
            lista_atividades=lista_atividades,
            current_user=current_user,
            usuarios=usuarios,
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
        return redirect(url_for("login_page"))


@app.route("/Perfil-edit", methods=["GET", "POST"])
def perfil_edit():
    if session.get("usuario_logado"):
        if request.method == "POST":
            nome = request.form.get("input-nome")
            email = request.form.get("input-email")
            nova_senha = request.form.get("input-senha")
            img = request.files["input-file"]

            users = Cliente.pegar_usuarios()
            for user in users:
                if session.get("usuario_logado") == user["matricula"]:
                    user["nome"] = nome
                    user["email"] = email
                    if nova_senha:
                        user["senha"] = nova_senha
                    if img:
                        nome_arquivo = salvar_imagem(img)
                        user["foto-perfil"] = nome_arquivo
                else:
                    pass

            Cliente.atualizar_usuarios(users)

            flash("Dados atualizados!")
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
        return redirect(url_for("login_page"))


@app.route("/Cadastro-Atividades", methods=["GET", "POST"])
def cadastro_atividades():

    if session.get("usuario_logado"):
        if request.method == "POST":
            # pegando o current
            usuarios = Cliente.pegar_usuarios()
            usuario_logado = session.get("usuario_logado")
            current_user = None

            # pegando usuário logado para enviar informações pra tela de login
            for usuario in usuarios:
                if usuario["matricula"] == usuario_logado:
                    current_user = usuario
                else:
                    pass

            # pegando o current
            usuarios = Cliente.pegar_usuarios()
            usuario_logado = session.get("usuario_logado")
            current_user = None

            # pegando usuário logado para enviar informações pra tela de login
            for usuario in usuarios:
                if usuario["matricula"] == usuario_logado:
                    current_user = usuario
                else:
                    pass

            titulo = request.form.get("titulo")
            descricao = request.form.get("descricao")
            data = request.form.get("data")

            # reforma da data
            dia = data[-2:]
            mes = data[-5:-3]
            ano = data[:4]
            data_reformada = dia + "/" + mes + "/" + ano

            usuario_logado = session.get("usuario_logado")

            if current_user["lider"] == "s":

                visibilidade = request.form.get("selecionarvisibilidade")
            else:
                visibilidade = "Privado"

            flash("ATIVIDADE ADICIONADA")
            atividade1 = Atividade(
                titulo, descricao, data_reformada, visibilidade, usuario_logado
            )

            atividade1.guardar_atividade()
            return render_template(
                "cadastro-atividades.html",
                current_user=current_user,
            )

        else:
            # pegando o current
            usuarios = Cliente.pegar_usuarios()
            usuario_logado = session.get("usuario_logado")
            current_user = None

            # pegando usuário logado para enviar informações pra tela de login
            for usuario in usuarios:
                if usuario["matricula"] == usuario_logado:
                    current_user = usuario
                else:
                    pass
            return render_template(
                "cadastro-atividades.html", current_user=current_user
            )

    else:
        return redirect(url_for("login_page"))


@app.route("/Atividade/<string:codigo_atividade>")
def tela_atividades(codigo_atividade):
    if session.get("usuario_logado"):
        # pegando o current
        usuarios = Cliente.pegar_usuarios()
        usuario_logado = session.get("usuario_logado")
        current_user = None

        # pegando usuário logado para enviar informações pra tela de login
        for usuario in usuarios:
            if usuario["matricula"] == usuario_logado:
                current_user = usuario
            else:
                pass

        # atividades
        atividades = Atividade.pegar_atividades()
        atvd = None
        tem_atividade = False

        for atividade in atividades:
            if (
                atividade["cod"] == codigo_atividade
                and atividade["criador"] == current_user["matricula"]
            ):
                tem_atividade = True
                atvd = atividade
            else:
                pass

        if tem_atividade:
            return render_template(
                "tela-atividade.html", current_user=current_user, atvd=atvd
            )
        else:
            flash("ACESSO RESTRITO")
            return redirect(url_for("home_page"))
    else:
        return redirect(url_for("login_page"))


@app.route("/Atividade-Edit/<string:codigo_atividade>", methods=["GET", "POST"])
def tela_atividades_edit(codigo_atividade):
    if session.get("usuario_logado"):
        if request.method == "POST":
            # pegando o current
            usuarios = Cliente.pegar_usuarios()
            usuario_logado = session.get("usuario_logado")
            current_user = None

            # pegando usuário logado para enviar informações pra tela de login
            for usuario in usuarios:
                if usuario["matricula"] == usuario_logado:
                    current_user = usuario
                else:
                    pass

            titulo = request.form.get("titulo")
            descricao = request.form.get("descricao")
            data = request.form.get("data")
            status = request.form.get("selecionarstatus")

            # reforma da data
            dia = data[-2:]
            mes = data[-5:-3]
            ano = data[:4]
            data_reformada = dia + "/" + mes + "/" + ano

            usuario_logado = session.get("usuario_logado")

            if current_user["lider"] == "s":

                visibilidade = request.form.get("selecionarvisibilidade")
            else:
                visibilidade = "Privado"

            atividades = Atividade.pegar_atividades()

            for atividade in atividades:
                if atividade["cod"] == codigo_atividade:
                    atividade["titulo"] = titulo
                    atividade["descricao"] = descricao
                    atividade["data"] = data_reformada
                    atividade["visibilidade"] = visibilidade
                    atividade["status"] = status

            Atividade.atualizar_atividades(atividades)

            flash("ATIVIDADE ATUALIZADA")
            return redirect(
                url_for("tela_atividades", codigo_atividade=codigo_atividade)
            )

        else:
            # pegando o current
            usuarios = Cliente.pegar_usuarios()
            usuario_logado = session.get("usuario_logado")
            current_user = None

            # pegando usuário logado para enviar informações pra tela de login
            for usuario in usuarios:
                if usuario["matricula"] == usuario_logado:
                    current_user = usuario
                else:
                    pass

            # atividades
            atividades = Atividade.pegar_atividades()
            atvd = None
            tem_atividade = False

            for atividade in atividades:
                if (
                    atividade["cod"] == codigo_atividade
                    and atividade["criador"] == current_user["matricula"]
                ):
                    tem_atividade = True
                    atvd = atividade
                else:
                    pass

            if tem_atividade:
                data = atvd["data"]

                ano = data[-4:]
                mes = data[-7:-5]
                dia = data[0:2]

                nova_data = ano + "-" + mes + "-" + dia

                return render_template(
                    "tela-atividade-edit.html",
                    current_user=current_user,
                    atvd=atvd,
                    nova_data=nova_data,
                )
            else:
                return redirect(url_for("home_page"))
    else:
        return redirect(url_for("login_page"))


@app.route("/Excluir-atividade/<string:codigo>")
def excluir_atividade(codigo):
    if session.get("usuario_logado"):
        atividades = Atividade.pegar_atividades()

        for atividade in atividades:
            if atividade["cod"] == codigo:
                atividades.remove(atividade)
                Atividade.atualizar_atividades(atividades)
                flash("ATIVIDADE DELETADA")
                return redirect(url_for("home_page"))
            else:
                pass

        return redirect(url_for("home_page"))

    else:
        return redirect(url_for("login_page"))


def salvar_imagem(imagem):
    codigo = token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_arquivo = nome + codigo + extensao
    caminho = os.path.join(app.root_path, "static/fotos_perfil", nome_arquivo)

    imagem_original = Image.open(imagem)

    largura, altura = imagem_original.size
    if largura > altura:
        diferenca = (largura - altura) // 2
        box = (diferenca, 0, largura - diferenca, altura)
    else:
        diferenca = (altura - largura) // 2
        box = (0, diferenca, largura, altura - diferenca)

    imagem_quadrada = imagem_original.crop(box)
    tamanho = (200, 200)
    imagem_quadrada.thumbnail(tamanho)
    imagem_quadrada.save(caminho)

    return nome_arquivo


if __name__ == "__main__":
    app.run(debug=True)
