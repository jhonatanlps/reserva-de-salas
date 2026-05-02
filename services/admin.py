from models.usuario import Usuario

class Admin(Usuario):
    def __init__(self, nome, email, senha, nivel):
        super().__init__(nome, email, senha, nivel)
        
    #UC-05
    def reservar_sala(self, solicitacoes: list, reservas: list, usuarios: list, salas: dict) -> None:
        if len(solicitacoes) > 0:

            for i, solicitacao in enumerate(solicitacoes):
                print(f"\n({i}) - Detalhes: \n\t - Unidade: {salas[solicitacao.get_unidade()]['nome']} \n\t - Sala: {solicitacao.get_sala()} \n\t - Data: {solicitacao.get_data()} \n\t - Horário: {solicitacao.get_horario()} \n\t - Status: {solicitacao.get_status()}")

            solicitacao = int(input("\nQual solicitação deseja aprovar ou negar?\n"))

            if solicitacao in range(len(solicitacoes)):
                for i, usuario in enumerate(usuarios):
                    if solicitacoes[solicitacao].get_usuario() == usuario.get_id():
                        print(f"\n({i}) - Detalhes do usuário: \n\t - Nome: {usuario.get_nome()} \n\t - Email: {usuario.get_email()} \n\t - Nível: {usuario.get_nivel()}")
                        break

                print("\nO que deseja fazer com essa solicitação?\n1 - Aprovar\n2 - Negar\n")
                aprovacao = int(input("Opção:"))

                if aprovacao == 1:
                    solicitacoes[solicitacao].set_status("Aprovado")
                    reservas.append(solicitacoes[solicitacao])
                    solicitacoes.pop(solicitacao)
                    print("\nSolicitação aprovada!")

                elif aprovacao == 2:
                    solicitacoes[solicitacao].set_status("Negado")
                    solicitacoes[solicitacao].get_usuario().set_reservas(solicitacoes[solicitacao])
                    solicitacoes.pop(solicitacao)
                    print("\nSolicitação negada!")

                else:
                    print("Opção inválida.")
            else:
                print("Solicitação inválida.")
        else:
            print("Sem solicitações no momento.")
    
    #UC-06: Restrigir sala
    def restringir_sala(self, salas: dict) -> None:
        while(True):
            print()
            for k in salas.keys():
                print(f"{k}")
            unidade = input("\nDe qual unidade é a sala que deseja gerenciar restricoes?\n").capitalize()
            
            if unidade in salas:
                print()
                for v in salas[unidade].keys():
                    print(f"- {v}")
                
                sala = input("\nQual sala deseja gerenciar a restrição?\n").lower()
                if sala in salas[unidade]:
                    nivel = -1
                    while nivel not in (0, 1, 2):
                        nivel = int(input("""\nO que deseja fazer:\n0 - Bloquear\n1 - Deixar apenas para professores\n2 - Deixar para todos\n"""))
                        
                        if nivel in (0, 1, 2):
                            salas[unidade][sala] = nivel
                            print("\nRestrições alterada!")
                            break    
                        else:
                            print("Opção inválida.")
                    break
                else:
                    print("Essa sala não existe, tente novamente.")
            else:
                print("Essa unidade não existe, tente novamente.")
            
    def consulta_historico(self, historico: list) -> None:
        if len(historico) > 0:
            for i in historico:
                print(f"{i.get_unidade()} - {i.get_sala()} - {i.get_data()} - {i.get_horario()} - {i.get_usuario().get_nome()} - {i.get_usuario().get_email()} - {i.get_status()}")
        else:
            print("Sem historico no momento.")
        