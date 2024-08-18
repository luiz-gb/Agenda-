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
