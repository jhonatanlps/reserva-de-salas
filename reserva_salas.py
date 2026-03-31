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

#UC-03: Buscar salas
def buscar_salas(reservas, solicitacoes, salas, usuario):
    #usuario faz a solicitação de reserva
    while(True):
        print()
        for k in salas.keys():
            print(f"{k}")
        unidade = input("\nEm qual unidade deseja reservar?\n").capitalize()
        
        if unidade in salas:
            for v in salas[unidade].keys():
                if salas[unidade][v] >= usuario.get_nivel():
                    print(f"- {v}")
            
            sala = input("\nQual sala deseja reservar?\n").lower()
            if sala in salas[unidade]:
                if usuario.get_nivel() <= salas[unidade][sala]:
                    data = input("\nQual seria a data?\n")
                    horario = input("\nQual seria o horario?\n")
                    
                    solicitacao = Solicitacao(unidade, sala, data, horario, usuario)
                    if verificar_disponibilidade(reservas, solicitacao):
                        solicitacoes.append(solicitacao)
                        print("\nSolicitação feita, aguarde a aprovação.")
                        break
                    else:
                        print("Nenhuma sala encontrada para os critérios informados.")
                else:
                    print("Sem permissão para reservar essa sala, tente novamente.")
            else:
                print("Essa sala não existe, tente novamente.")
        else:
            print("Essa unidade não existe, tente novamente.")
            
        #Saída esperada:
        #Solicitação feita, aguarde a aprovação.")
                        
#UC-04: Verificar disponibilidade                  
def verificar_disponibilidade(reservas, solicitacao):
    #Verifica se a solicitação esta disponivel
    disponivel = True
    
    for i in reservas:
        if i.get_unidade() == solicitacao.get_unidade() and i.get_sala() == solicitacao.get_sala() and i.get_mes() == solicitacao.get_mes() and i.get_dia() == solicitacao.get_dia() and i.get_horario() == solicitacao.get_horario():
            disponivel = False
    
    return disponivel

    #UC-07: Cancelar reserva
def cancelar_reservas(reservas, usuario):
    #cancela a reserva
    if len(reservas) > 0:
        c = 1
        for i in reservas:
            if usuario.get_email() == i.get_usuario().get_email() and usuario.get_nivel() in (1, 2):
                print(f"{c} - {i.get_unidade()} - {i.get_sala()} - {i.get_data()} - {i.get_horario()} - {i.get_usuario().get_nome()} - {i.get_status()}\n")
            elif usuario.get_nivel() == 0:
                print(f"{c} - {i.get_unidade()} - {i.get_sala()} - {i.get_data()} - {i.get_horario()} - {i.get_usuario().get_nome()} - {i.get_status()}\n")
            c =+ 1  
            
        reserva = int(input("Qual reserva deseja cancelar?\n"))
        reservas.pop(reserva-1)
        print("Reserva cancelada com sucesso!\n")
            
    else:
        print("\nSem solicitações no momento.\n")
        
    #Saída esperada:
    #Reserva cancelada com sucesso!