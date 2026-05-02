
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