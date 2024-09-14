import json


class Cliente:
    def __init__(self, nome, cpf, email, senha, turma):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.turma = turma

    def guardar_usuario(self):
        novo_usuario = {
            "nome": self.nome,
            "matricula": self.cpf,
            "email": self.email,
            "senha": self.senha,
            "turma": self.turma,
        }

        try:
            with open("usuarios.json", "r") as arquivo:
                clientes = json.load(arquivo)
        except FileNotFoundError:
            clientes = []

        clientes.append(novo_usuario)

        with open("usuarios.json", "w") as arquivo:
            json.dump(clientes, arquivo, indent=4)


class Atividade:
    def __init__(self, titulo, descricao, data, visibilidade):
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.visibilidade = visibilidade

    def guardar_atividade(self):
        nova_atividade = {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data": self.data,
            "visibilidade": self.visibilidade,
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
