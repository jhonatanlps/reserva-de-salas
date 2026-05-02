
class Reserva:
    def __init__(self, id_reserva, id_unidade, id_usuario, sala, data, horario):
        self.__id = id_reserva
        self.__unidade = id_unidade
        self.__usuario = id_usuario
        self.__sala = sala
        self.__data = data
        self.__horario = horario

    def get_id_reserva(self):
        return self.__id

    def get_id_unidade(self):
        return self.__unidade

    def get_nome_sala(self):
        return self.__sala

    def get_data(self):
        return self.__data

    def get_horario(self):
        return self.__horario

    def get_usuario(self):
        return self.__usuario

    def set_id_reserva(self, id_reserva):
        self.__id = id_reserva
    
    def set_id_unidade(self, id_unidade):
        self.__unidade = id_unidade

    def set_nome_sala(self, nome_sala):
        self.__sala = nome_sala

    def set_data(self, data):
        self.__data = data

    def set_horario(self, horario):
        self.__horario = horario

    def set_usuario(self, usuario):
        self.__usuario = usuario