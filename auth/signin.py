from models.solicitacao import Solicitacao
from models.usuario import Usuario

#UC-02: Cadastrar conta
def cadastrar(usuarios: list[Usuario], solicitacoes: list[Solicitacao], reservas: list[dict], salas: list[dict]):
    # Cadastra a conta no sistema
    print("\nCADASTRO")
    nivel = int(input("""\nVocê é:\n1 - Professor\n2 - Aluno\n"""))
    
    nome = input("\nDigite o seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ") 

    print("\nCadastrando usuário...")

    usuario = Usuario(len(usuarios)+1, nome, email, senha, nivel)

    usuarios.append(usuario)

    print("\nUsuário cadastrado com sucesso!")
    
    return True, usuarios
    
    #Saída esperada:
    #Usuário cadastrado com sucesso!