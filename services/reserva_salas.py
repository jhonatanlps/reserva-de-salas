from models.solicitacao import Solicitacao
from models.usuario import Usuario
from models.reserva import Reserva
from services.admin import Admin

def menu(usuario: Usuario, solicitacoes: list[Solicitacao], reservas: list[Reserva], salas: list[dict], datas: list[str], horarios: list[str], usuarios: list[Usuario]) -> None:
    #Menu de opções
    print("\nMENU")

    #TODO: UC-03: Implementar a funcionalidade de buscar salas. A função buscar_salas deve receber a lista de reservas, a lista de solicitações, a lista de salas e o usuário logado, e deve permitir que o usuário busque por salas disponíveis para reserva, levando em consideração as reservas já feitas e as solicitações pendentes.
    #TODO: UC-07: Implementar a funcionalidade de cancelar reservas. A função cancelar_reservas deve receber a lista de reservas e o usuário logado, e deve permitir que o usuário cancele uma reserva que ele tenha feito.

    # Caso o usuário seja um admin, ele tem acesso a todas as funcionalidades, caso contrário, ele tem acesso apenas a algumas funcionalidades.
    if usuario.get_nivel() == 3:
        while(True):
            print("""\n1 - Verificar solicitações de reserva\n2 - Cancelar reserva\n3 - Restringir acesso\n4 - Sair\n
                  """)
            
            opcao = int(input("\nDigite a opção que deseja executar:\n"))

            admin = Admin(usuario.get_nome(), usuario.get_email(), usuario.get_senha(), usuario.get_nivel())

            match opcao:
                case 1:
                    admin.reservar_sala(solicitacoes, reservas, usuarios, salas)
                
                case 2:
                    admin.cancelar_reserva(reservas, usuario)
                    
                case 3:
                    admin.restringir_sala(salas)
            
                case 4:
                    print("Saindo...")
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
                    buscar_salas(reservas, solicitacoes, salas, usuario, datas, horarios)
                
                case 2:  
                    cancelar_reservas(reservas, usuario)
                    
                case 3:
                    print("Saindo...")
                    break
                
                case _:
                    
                    print("Opção invalida, tente novamente.")

# TODO: Implementar a funcionalidade de buscar salas
#UC-03: Buscar salas
def buscar_salas(reservas: list[Reserva], solicitacoes: list[Solicitacao], salas: list[dict], usuario: Usuario, datas: list[str], horarios: list[str]) -> None:
    # Usuário faz a solicitação de reserva
    while(True):
        print()

        # sala é uma lista contendo dicionarios
        for _id, unidade in enumerate(salas):
            print(f"({_id}) - {unidade['nome']}")
        print("\nEm qual unidade deseja reservar?")
        id_unidade = int(input("Opção: "))
        print("")

        if salas[id_unidade]:
            for _id, sala in enumerate(salas[id_unidade]['salas']):
                if salas[id_unidade]['salas'][sala] <= usuario.get_nivel():
                    print(f"({_id}) - {sala}")
            
            print("\nQual sala deseja reservar?")
            sala = int(input("Opção: "))

            try:
                sala = list(salas[id_unidade]['salas'].keys())[sala]
            except IndexError:
                print("Opção invalida, tente novamente.")
                continue

            if usuario.get_nivel() >= salas[id_unidade]['salas'][sala]:

                print("\nQual seria a data?\n")
                for i, data in enumerate(datas):
                    print(f"({i}) - {data}")

                id_data = int(input("\nDigite o número correspondente a data desejada:\n"))                    
                data = datas[id_data]

                print("\nQual seria o horário?\n")
                for i, horario in enumerate(horarios):
                    print(f"({i}) - {horario}")

                id_horario = int(input("\nDigite o número correspondente ao horário desejado:\n"))
                horario = horarios[id_horario]

                solicitacao = Solicitacao(unidade, sala, data, horario, usuario)
                if verificar_disponibilidade(reservas, solicitacao):
                    solicitacoes.append(solicitacao)
                    print("\nSolicitação feita, aguarde a aprovação.\n")
                    break
                else:
                    print("Nenhuma sala encontrada para os critérios informados.")
            else:
                print("Sem permissão para reservar essa sala, tente novamente.")
        else:
            print("Essa unidade não existe, tente novamente.")
            
        #Saída esperada:
        #Solicitação feita, aguarde a aprovação.")
                        
#UC-03                   
def verificar_disponibilidade(reservas: list[Reserva], solicitacao: Solicitacao) -> bool:
    #Verifica se a sala da solicitação esta disponivel
    disponivel = True
    
    for reserva in reservas:
        if reserva.get_id_unidade() == solicitacao.get_unidade() and reserva.get_sala() == solicitacao.get_sala() and reserva.get_data() == solicitacao.get_data() and reserva.get_horario() == solicitacao.get_horario():
            disponivel = False
    
    return disponivel  

#UC-07       
def cancelar_reservas(reservas, usuario):
    #cancela a reserva
    if len(reservas) > 0:
        c = 1
        for reserva in reservas:
            if usuario.get_email() == reserva.get_usuario().get_email() and usuario.get_nivel() in (1, 2):
                print(f"{c} - {reserva.get_unidade()} - {reserva.get_sala()} - {reserva.get_data()} - {reserva.get_horario()} - {reserva.get_usuario().get_nome()} - {reserva.get_status()}\n")
            elif usuario.get_nivel() == 0:
                print(f"{c} - {reserva.get_unidade()} - {reserva.get_sala()} - {reserva.get_data()} - {reserva.get_horario()} - {reserva.get_usuario().get_nome()} - {reserva.get_status()}\n")
            c =+ 1  
            
        reserva = int(input("Qual reserva deseja cancelar?\n"))
        reservas.pop(reserva-1)
        print("Reserva cancelada com sucesso!\n")
            
    else:
        print("\nSem solicitações no momento.\n")
        
    #Saída esperada:
    #Reserva cancelada com sucesso!