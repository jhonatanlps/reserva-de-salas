
class Usuario:
  def __init__(self, _id = None, nome = None, email = None, senha = None, nivel = None):
    self.__id = _id
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.__nivel = nivel
  
  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome
  
  def get_email(self):
    return self.__email
  
  def get_nivel(self):
    return self.__nivel

  def get_senha(self):
    return self.__senha

  def set_id(self, _id):
    self.__id = _id

  def set_nome(self, nome):
    self.__nome = nome

  def set_email(self, email):
    self.__email = email
    
  def set_senha(self, senha):
    self.__senha = senha
    
  def set_nome(self, nome):
    self.__nome = nome

    #UC-07       
  def cancelar_reservas(self, reservas, usuario, salas: list[dict]) -> None:
      #cancela a reserva
      if len(reservas) > 0:
          c = 1
          print("\nReservas:")
          for reserva in reservas:
            if usuario.get_id() == reserva.get_usuario() and usuario.get_nivel() in (1, 2):
              print(f"ID: {c} | Sala: {salas[reserva.get_id_unidade()-1]['nome']} | Reserva: {reserva.get_nome_sala()} | Data: {reserva.get_data()} | Horário: {reserva.get_horario()} | Usuário: {usuario.get_nome()}\n")
            elif usuario.get_nivel() == 3:
              print(f"ID: {c} | Sala: {salas[reserva.get_id_unidade()-1]['nome']} | Reserva: {reserva.get_nome_sala()} | Data: {reserva.get_data()} | Horário: {reserva.get_horario()} | Usuário: {usuario.get_nome()}\n")
            c = c + 1 
            
          reserva = str(input("Qual reserva deseja cancelar? [V] Voltar\n"))
          if reserva.upper() == "V":
              return

          reservas.pop(int(reserva)-1)
          print("Reserva cancelada com sucesso!\n")
              
      else:
          print("\nSem solicitações no momento.\n")
          
      #Saída esperada:
      #Reserva cancelada com sucesso!