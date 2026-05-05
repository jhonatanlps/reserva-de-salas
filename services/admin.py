from models.usuario import Usuario
from models.solicitacao import Solicitacao
from models.reserva import Reserva

class Admin(Usuario):
    def __init__(self, nome, email, senha, nivel):
        super().__init__(nome, email, senha, nivel)
        
    #UC-05
    def reservar_sala(self, solicitacoes: list[Solicitacao], reservas: list[Reserva], usuarios: list[Usuario], salas: list[dict]) -> None:
        if len(solicitacoes) > 0:

            for i, solicitacao in enumerate(solicitacoes):
                unidade_idx = solicitacao.get_unidade() - 1
                print(f"\n({i}) - Detalhes: \n\t - Unidade: {salas[unidade_idx]['nome']} \n\t - Sala: {solicitacao.get_sala()} \n\t - Data: {solicitacao.get_data()} \n\t - Horário: {solicitacao.get_horario()} \n\t - Status: {solicitacao.get_status()}")

            solicitacao = int(input("\nQual solicitação deseja aprovar ou negar?\n"))

            if solicitacao in range(len(solicitacoes)):
                for i, usuario in enumerate(usuarios):
                    if solicitacoes[solicitacao].get_usuario() == usuario.get_id():
                        print(f"\n({i}) - Detalhes do usuário: \n\t - Nome: {usuario.get_nome()} \n\t - Email: {usuario.get_email()} \n\t - Nível: {usuario.get_nivel()}")
                        break

                print("\nO que deseja fazer com essa solicitação?\n1 - Aprovar\n2 - Negar\n")
                aprovacao = int(input("Opção:"))

                if aprovacao == 1:
                    solic = solicitacoes[solicitacao]
                    solic.set_status("Aprovado")

                    prox_id = max((r.get_id_reserva() for r in reservas), default=0) + 1
                    nova_reserva = Reserva(
                        prox_id,
                        solic.get_unidade(),
                        solic.get_usuario(),
                        solic.get_sala(),
                        solic.get_data(),
                        solic.get_horario()
                    )
                    reservas.append(nova_reserva)
                    solicitacoes.pop(solicitacao)
                    print("\nSolicitação aprovada!")

                elif aprovacao == 2:
                    solicitacoes[solicitacao].set_status("Negado")
                    solicitacoes.pop(solicitacao)
                    print("\nSolicitação negada!")

                else:
                    print("Opção inválida.")
            else:
                print("Solicitação inválida.")
        else:
            print("Sem solicitações no momento.")
    
    #UC-06: Restrigir sala
    def restringir_sala(self, salas: list[dict]) -> None:
        while(True):
            print()
            
            for _id, unidade in enumerate(salas):
                print(f"({_id}) - {unidade['nome']}")
            print("\nEm qual unidade deseja restringir acesso?")
            id_unidade = int(input("Opção: "))
            print("")

            try:
                if salas[id_unidade]:
                    for _id, sala in enumerate(salas[id_unidade]['salas']):
                        print(f"({_id}) - {sala}")
                                                
                    print("\nQual sala deseja restringir acesso?")
                    sala = int(input("Opção: "))

                    try:
                        sala = list(salas[id_unidade]['salas'].keys())[sala]
                        
                        print("\nQual restrição deseja? \n1 - Todos\n2 - Apenas professores\n3 - Sem possibilidade de reserva\n")
                        nivel = int(input("Opção: "))
                        if nivel in (1, 2, 3):
                            salas[id_unidade]["salas"][sala] = nivel
                            print("Acesso restringido!")
                            break
                        else:
                            print("Nivel invalido")
                    except IndexError:
                        print("Opção invalida, tente novamente.")
                        continue
            except IndexError:
                print("Opção invalida, tente novamente.")
                