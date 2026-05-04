import bcrypt
from models.solicitacao import Solicitacao
from models.usuario import Usuario

#UC-01: Fazer login
def login(usuarios: list[Usuario], solicitacoes: list[Solicitacao], reservas: list[dict], salas: list[dict]):
    #Faz o login no sistema
    continuar = True
    while(continuar):
        print("\nLOGIN")
        email = input("\nEmail: ")
        senha = input("Senha: ")
        
        for usuario in usuarios:
            if usuario.get_email() == email:
                hash_salvo = usuario.get_senha().encode('utf-8')
                if bcrypt.checkpw(senha.encode('utf-8'), hash_salvo):
                    print("Logado com sucesso. Sejam bem-vindo(a)!")
                    continuar = False
                    return True, usuario
                else:
                    print("Email e/ou senha incorretos, tente novamente.")
                    break

        else:
            print("Email e/ou senha incorretos, tente novamente.")