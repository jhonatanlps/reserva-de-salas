
class Solicitacao:
    def __init__(self, unidade, sala, data, horario, usuario):
        self.__id_unidade = unidade
        self.__sala = sala
        self.__data = data
        self.__horario = horario
        self.__id_usuario = usuario
        self.__status = "pendente"
        
    def get_unidade(self):
        return self.__id_unidade

    def get_sala(self):
        return self.__sala

    def get_data(self):
        return self.__data

    def get_horario(self):
        return self.__horario

    def get_usuario(self):
        return self.__id_usuario

    def get_status(self):
        return self.__status
    
    def set_unidade(self, unidade):
        self.__id_unidade = unidade
    
    def set_sala(self, sala):
        self.__sala = sala
    
    def set_data(self, data):
        self.__data = data

    def set_status(self, status):
        self.__status = status
        