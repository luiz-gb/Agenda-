import json, random


class Cliente:
    def __init__(self, nome, cpf, email, senha, turma, lider, foto_perfil):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.turma = turma
        self.lider = lider
        self.foto_perfil = None

    def guardar_usuario(self):
        novo_usuario = {
            "nome": self.nome,
            "matricula": self.cpf,
            "email": self.email,
            "senha": self.senha,
            "turma": self.turma,
            "lider": self.lider,
            "foto-perfil": "",
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
        self.cod = None
        self.status = "Pendente"
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.visibilidade = visibilidade
        self.criador = criador

    def guardar_atividade(self):
        try:
            with open("atividades.json", "r") as arquivo:
                atividades = json.load(arquivo)
        except FileNotFoundError:
            atividades = []

        # verufica se ja tem alguma atividade com o mesmo codigo
        if atividades:
            while True:
                codigo = str(random.randint(1000, 9999))

                tem_igual = False
                for atividade in atividades:
                    if atividade["cod"] == codigo:
                        tem_igual = True
                    else:
                        pass

                if tem_igual:
                    continue
                else:
                    break
        else:
            codigo = str(random.randint(1000, 9999))

        nova_atividade = {
            "cod": codigo,
            "status": self.status,  # pendente ou concluida
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data": self.data,
            "visibilidade": self.visibilidade,
            "criador": self.criador,
        }

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

    def atualizar_atividades(nova_lista):
        with open("atividades.json", "w") as arquivo:
            json.dump(nova_lista, arquivo, indent=4)


class Suporte:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

    def guardar_suporte(self):
        novo_usuario = {
            "nome": self.nome,
            "email": self.email,
            "mensagem": self.mensagem,
        }

        try:
            with open("suportes.json", "r") as arquivo:
                suportes = json.load(arquivo)
        except FileNotFoundError:
            suportes = []

        suportes.append(novo_usuario)

        with open("suportes.json", "w") as arquivo:
            json.dump(suportes, arquivo, indent=4)
