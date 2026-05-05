
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

      id_reserva = int(input("Digite o ID da reserva que deseja cancelar:\n"))
      
      if id_reserva > 0 and id_reserva <= len(reservas):
        reserva = reservas[id_reserva-1]
        if usuario.get_id() == reserva.get_usuario() and usuario.get_nivel() in (1, 2):
          reservas.pop(id_reserva-1)
          print("Reserva cancelada com sucesso!")
        elif usuario.get_nivel() == 3:
          reservas.pop(id_reserva-1)
          print("Reserva cancelada com sucesso!")
        else:
          print("Você não tem permissão para cancelar essa reserva.")
          
      #Saída esperada:
      #Reserva cancelada com sucesso!

  def cancelar_solicitacao(self, solicitacoes, usuario, salas: list[dict]) -> None:
      #cancela a solicitação

      id_solicitacao = int(input("Digite o ID da solicitação que deseja cancelar:\n"))

      if id_solicitacao > 0 and id_solicitacao <= len(solicitacoes):
        solicitacao = solicitacoes[id_solicitacao-1]
        if usuario.get_id() == solicitacao.get_usuario() and usuario.get_nivel() in (1, 2):
          solicitacoes.pop(id_solicitacao-1)
          print("Solicitação cancelada com sucesso!")
        elif usuario.get_nivel() == 3:
          solicitacoes.pop(id_solicitacao-1)
          print("Solicitação cancelada com sucesso!")
        else:
          print("Você não tem permissão para cancelar essa solicitação.")
          
      #Saída esperada:
      #Solicitação cancelada com sucesso!

  def historico(self, reservas, solicitacoes, usuario, salas: list[dict]) -> None:
    # Exibe o histórico de reservas e solicitações do usuário
    print("\nHistórico de Reservas:")
    
    if len(reservas) > 0:
        c = 1
        cancelar = False
        for reserva in reservas:
          if usuario.get_id() == reserva.get_usuario() and usuario.get_nivel() in (1, 2):
            print(f"ID: {c} | Sala: {salas[reserva.get_id_unidade()-1]['nome']} | Reserva: {reserva.get_nome_sala()} | Data: {reserva.get_data()} | Horário: {reserva.get_horario()} | Usuário: {usuario.get_nome()}\n")
            cancelar = True
          elif usuario.get_nivel() == 3:
            print(f"ID: {c} | Sala: {salas[reserva.get_id_unidade()-1]['nome']} | Reserva: {reserva.get_nome_sala()} | Data: {reserva.get_data()} | Horário: {reserva.get_horario()} | Usuário: {usuario.get_nome()}\n")
            cancelar = True
          c = c + 1
        
        if cancelar:
          deletar = str(input("Deseja cancelar alguma reserva? [S/N]\n"))
          
          if deletar.upper() == "S":
            self.cancelar_reservas(reservas, usuario, salas)
        else:
          print("Você não tem reservas no momento.")
        
        print("\nProsseguindo...")
    else:
        print("Sem reservas no momento.\n")
    
    print("\nHistórico de Solicitações:")
    
    if len(solicitacoes) > 0:
        c = 1
        cancelar = False
        for solicitacao in solicitacoes:
          if usuario.get_id() == solicitacao.get_usuario() and usuario.get_nivel() in (1, 2):
            print(f"ID: {c} | Sala: {salas[solicitacao.get_unidade()-1]['nome']} | Solicitação: {solicitacao.get_sala()} | Data: {solicitacao.get_data()} | Horário: {solicitacao.get_horario()} | Usuário: {usuario.get_nome()}\n")
            cancelar = True
          elif usuario.get_nivel() == 3:
            print(f"ID: {c} | Sala: {salas[solicitacao.get_unidade()-1]['nome']} | Solicitação: {solicitacao.get_sala()} | Data: {solicitacao.get_data()} | Horário: {solicitacao.get_horario()} | Usuário: {usuario.get_nome()}\n")
            cancelar = True
          c = c + 1

          if cancelar:
            deletar = str(input("Deseja cancelar alguma solicitação? [S/N]\n"))

            if deletar.upper() == "S":
              self.cancelar_solicitacao(solicitacoes, usuario, salas)
          else:
            print("Você não tem solicitações no momento.") 
          
          print("\nRetornando ao menu principal...\n")
    else:
        print("Sem solicitações no momento.\n")
    