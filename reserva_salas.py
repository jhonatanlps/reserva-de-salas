from usuario import Usuario
from solicitacao import Solicitacao

#UC-02: Cadastrar conta
def cadastrar(banco_dados, solicitacoes, reservas, salas):
    #Cadastra a conta no sistema
    print("\nCADASTRO")
    nivel = int(input("""\nVocê é:\n1 - Professor\n2 - Aluno\n"""))
    
    nome = input("\nDigite o seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ") 
    
    usuario = Usuario(nome, email, senha, nivel)
        
    banco_dados.append(usuario)
    print("Usuário cadastrado com sucesso!")
    login(banco_dados, solicitacoes, reservas, salas)
    
    #Saída esperada:
    #Usuário cadastrado com sucesso!

#UC-01
def login(banco_dados, solicitacoes, reservas, salas):
    #Faz o login no sistema
    continuar = True
    while(continuar):
        print("\nLOGIN")
        email = input("\nEmail: ")
        senha = input("Senha: ")
        
        for user in banco_dados:
            if len(banco_dados) >= 1:
                if user.get_email() == email and user.get_senha() == senha:
                    print("Logado com sucesso. Sejam bem-vindo(a)!")
                    menu(user, solicitacoes, reservas, salas)
                    continuar = False
    
            else:
                print("Usuario não encontrado, tente novamente.")
         
    #Saída esperada:
    #Logado com sucesso. Sejam bem-vindo(a)!

def menu(usuario, solicitacoes, reservas, salas):
    #Menu de opções
    print("\nMENU")
    if usuario.get_nivel() == 0:
        while(True):
            print("""\n1 - Reservar sala\n2 - Cancelar reserva\n3 - Restringir acesso\n4 - Sair\n
                  """)
            
            opcao = int(input("\nDigite a opção que deseja executar:\n"))

            match opcao:
                case 1:
                     
                    usuario.reservar_sala(solicitacoes, reservas)
                
                case 2:
                    
                    cancelar_reservas(reservas, usuario)
                    
                case 3:
                    
                    usuario.restringir_sala(salas)
            
                case 4:
                    
                    break
                
                case _:
                    print("Opção invalida, tente novamente.")
                    
       
    else:
        while(True):
            print("""1 - Buscar salas\n2 - Cancelar reserva\n3 - Sair\n
                  """)
            
            opcao = int(input("Digite a opção que deseja executar: "))

            match opcao:
                case 1:
                     
                    buscar_salas(reservas, solicitacoes, salas, usuario)
                
                case 2:
                    
                    cancelar_reservas(reservas, usuario)
                    
                case 3:
                    
                    break
                
                case _:
                    
                    print("Opção invalida, tente novamente.")
