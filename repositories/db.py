from models.solicitacao import Solicitacao
from models.reserva import Reserva
from models.usuario import Usuario
from pathlib import Path
import json

""" Arquivo para simular um banco de dados, utilizando um arquivo JSON para armazenar os dados. """
""" O arquivo JSON é carregado na inicialização da classe db e salvo ao final do programa. """

diretorio = Path(__file__).parent.parent

class db:
    def __init__(self):
        self.__usuarios: list[Usuario] = []
        self.__solicitacoes: list[Solicitacao] = []
        self.__reservas: list[Reserva] = []
        self.__salas: list[dict] = []
        self.__datas: list[str] = []
        self.__horarios: list[str] = []

        self.load_database()

        print("Banco de dados carregado com sucesso!")
        print(f"Usuários cadastrados: {self.get_usuarios()}")

    def get_salas(self) -> list[dict]:
        return self.__salas

    def set_salas(self, salas: list[dict]):
        self.__salas = salas

    def get_solicitacoes(self) -> list[Solicitacao]:
        return self.__solicitacoes

    def set_solicitacoes(self, solicitacoes: list[Solicitacao]):
        self.__solicitacoes = solicitacoes

    def get_reservas(self) -> list[Reserva]:
        return self.__reservas

    def set_reservas(self, reservas: list[Reserva]):
        self.__reservas = reservas

    def get_usuarios(self) -> list[Usuario]:
        return self.__usuarios
    
    def set_usuarios(self, usuarios: list[Usuario]):
        self.__usuarios = usuarios

    def set_datas(self, datas: list[str]):
        self.__datas = datas
    
    def get_datas(self) -> list[str]:
        return self.__datas

    def set_horarios(self, horarios: list[str]):
        self.__horarios = horarios

    def get_horarios(self) -> list[str]:
        return self.__horarios

    def load_database(self):
        """ Carrega os dados do arquivo JSON para as variáveis da classe. """

        with open(diretorio / "data" / "database.json", "r") as f:
            data = json.load(f)

        load_users: list[Usuario] = []
        load_solicitacao: list[Solicitacao] = []
        load_reservas: list[Reserva] = []

        for email, usuario in data["usuarios"].items():
            load_usuario = Usuario(usuario["id"], usuario["nome"], email, usuario["senha"], usuario["nivel"])
            load_users.append(load_usuario)        

        for solicitacao in data["solicitacoes"]:
            unidade = solicitacao.get("unidade")
            # tolera arquivos já "corrompidos" onde unidade foi salva como dict
            if isinstance(unidade, dict):
                unidade = unidade.get("id")

            obj = Solicitacao(unidade, solicitacao["sala"], solicitacao["data"], solicitacao["horario"], solicitacao["usuario"])
            if "status" in solicitacao:
                obj.set_status(solicitacao["status"])
            load_solicitacao.append(obj)

        for reserva in data["reservas"]:
            reserva = Reserva(reserva["id"], reserva["unidade"], reserva["usuario"], reserva["sala"], reserva["data"], reserva["horario"])
            load_reservas.append(reserva)

        self.set_reservas(load_reservas)
        self.set_salas(data["salas"])
        self.set_datas(data["datas"])
        self.set_horarios(data["horarios"])
        self.set_usuarios(load_users)
        self.set_solicitacoes(load_solicitacao)

    def save_database(self, reservas: list[Reserva], solicitacoes: list[Solicitacao], usuarios: list[Usuario], salas: list[dict]):
        """ Salva os dados das variáveis da classe no arquivo JSON. """

        with open(diretorio / "data" / "database.json", "r") as f:
            data = json.load(f)

        data["usuarios"] = {}
        data["solicitacoes"] = []
        data["reservas"] = []
        data["salas"] = []

        for usuario in usuarios:
            data["usuarios"][usuario.get_email()] = {
                "id": usuario.get_id(),
                "nome": usuario.get_nome(),
                "senha": usuario.get_senha(),
                "nivel": usuario.get_nivel()
            }

        for solicitacao in solicitacoes:
            unidade = solicitacao.get_unidade()
            if isinstance(unidade, dict):
                unidade = unidade.get("id")
            data["solicitacoes"].append({
                "unidade": int(unidade) if unidade is not None else unidade,
                "sala": solicitacao.get_sala(),
                "data": solicitacao.get_data(),
                "horario": solicitacao.get_horario(),
                "usuario": int(solicitacao.get_usuario()),
                "status": solicitacao.get_status()
            })
        
        for reserva in reservas:
            data["reservas"].append({
                "id": reserva.get_id_reserva(),
                "unidade": int(reserva.get_id_unidade()),
                "usuario": int(reserva.get_usuario()),
                "sala": reserva.get_nome_sala(),
                "data": reserva.get_data(),
                "horario": reserva.get_horario()
            })
        
        for sala in salas:
            data["salas"].append({
                "id": sala['id'],
                "nome": sala['nome'],
                "salas": sala['salas']
            })

        with open(diretorio / "data" / "database.json", "w") as f:
            json.dump(data, f, indent=4)