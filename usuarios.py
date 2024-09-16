import json


class Cliente:
    def __init__(self, nome, cpf, email, senha, turma, lider):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.turma = turma
        self.lider = lider

    def guardar_usuario(self):
        novo_usuario = {
            "nome": self.nome,
            "matricula": self.cpf,
            "email": self.email,
            "senha": self.senha,
            "turma": self.turma,
            "lider": self.lider,
        }

        try:
            with open("usuarios.json", "r") as arquivo:
                clientes = json.load(arquivo)
        except FileNotFoundError:
            clientes = []

        clientes.append(novo_usuario)

        with open("usuarios.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)

    def pegar_usuarios():
        try:
            with open("usuarios.json", "r") as arquivo:
                usuarios = json.load(arquivo)
        except FileNotFoundError:
            usuarios = []

        return usuarios

    def atualizar_usuarios(nova_lista):
        with open("usuarios.json", "w") as arquivo:
            json.dump(nova_lista, arquivo, indent=4)


class Atividade:
    def __init__(self, titulo, descricao, data, visibilidade, criador):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.visibilidade = visibilidade
        self.criador = criador

    def guardar_atividade(self):
        nova_atividade = {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data": self.data,
            "visibilidade": self.visibilidade,
            "criador": self.criador,
        }

        try:
            with open("atividades.json", "r") as arquivo:
                atividades = json.load(arquivo)
        except FileNotFoundError:
            atividades = []

        atividades.append(nova_atividade)

        with open("atividades.json", "w") as arquivo:
            json.dump(atividades, arquivo, indent=4)

    def pegar_atividades():
        try:
            with open("atividades.json", "r") as arquivo:
                atividades = json.load(arquivo)
        except FileNotFoundError:
            atividades = []

        return atividades
