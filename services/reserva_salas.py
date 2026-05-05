from models.solicitacao import Solicitacao
from models.usuario import Usuario
from models.reserva import Reserva
from services.admin import Admin

def menu(usuario: Usuario, solicitacoes: list[Solicitacao], reservas: list[Reserva], salas: list[dict], datas: list[str], horarios: list[str], usuarios: list[Usuario]) -> None:
    #Menu de opções
    print("\nMENU")

    # Caso o usuário seja um admin, ele tem acesso a todas as funcionalidades, caso contrário, ele tem acesso apenas a algumas funcionalidades.
    if usuario.get_nivel() == 3:
        while(True):
            print("""\n1 - Verificar solicitações de reserva\n2 - Visualizar histórico\n3 - Restringir acesso\n4 - Sair\n
                  """)
            
            opcao = int(input("\nDigite a opção que deseja executar:\n"))

            admin = Admin(usuario.get_nome(), usuario.get_email(), usuario.get_senha(), usuario.get_nivel())

            match opcao:
                case 1:
                    admin.reservar_sala(solicitacoes, reservas, usuarios, salas)
                
                case 2:
                    admin.historico(reservas, solicitacoes, usuario, salas)
                    
                case 3:
                    admin.restringir_sala(salas)
            
                case 4:
                    print("Saindo...")
                    break
                
                case _:
                    print("Opção invalida, tente novamente.")
                    
    else:
        while(True):
            print("""1 - Buscar salas\n2 - Visualizar histórico\n3 - Sair\n
                  """)
            
            opcao = int(input("Digite a opção que deseja executar: "))

            match opcao:
                case 1:
                    buscar_salas(reservas, solicitacoes, salas, usuario, datas, horarios)
                
                case 2:  
                    usuario.historico(reservas, solicitacoes, usuario, salas)
                    
                case 3:
                    
                    print("Saindo...")
                    break
                
                case _:
                    
                    print("Opção invalida, tente novamente.")

#UC-03: Buscar salas
def buscar_salas(reservas: list[Reserva], solicitacoes: list[Solicitacao], salas: list[dict], usuario: Usuario, datas: list[str], horarios: list[str]) -> None:
    # Usuário faz a solicitação de reserva
    while(True):
        print()

        # sala é uma lista contendo dicionários
        for _id, unidade in enumerate(salas):
            print(f"({_id}) - {unidade['nome']}")
        print("\nEm qual unidade deseja reservar?")
        id_unidade = int(input("Opção: "))
        print("")

        try:
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

                    # Persistência/JSON usa unidade como inteiro (1..N), e usuário como id (int)
                    solicitacao = Solicitacao(id_unidade + 1, sala, data, horario, usuario.get_id())
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
        except IndexError:
            print("Opção invalida, tente novamente.")
        #Saída esperada:
        #Solicitação feita, aguarde a aprovação.")
                        
#UC-03                   
def verificar_disponibilidade(reservas: list[Reserva], solicitacao: Solicitacao) -> bool:
    #Verifica se a sala da solicitação esta disponivel
    disponivel = True
    
    for reserva in reservas:
        if (
            reserva.get_id_unidade() == solicitacao.get_unidade()
            and reserva.get_nome_sala() == solicitacao.get_sala()
            and reserva.get_data() == solicitacao.get_data()
            and reserva.get_horario() == solicitacao.get_horario()
        ):
            disponivel = False
    
    return disponivel  

