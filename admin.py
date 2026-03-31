from usuario import Usuario

class Admin(Usuario):
    def __init__(self, nome, email, senha, nivel):
        super().__init__(nome, email, senha, nivel)
        
    #UC-05
    def reservar_sala(self, solicitacoes, reservas):
        if len(solicitacoes) > 0:
            c = 1
            print("")
            for i in solicitacoes:
                print(f"{c} - {i.get_unidade()} - {i.get_sala()} - {i.get_data()} - {i.get_horario()} - {i.get_usuario().get_nome()} - {i.get_usuario().get_email()} - {i.get_status()}\n")
                c =+ 1
            
            solicitacao = int(input("Qual solicitação deseja aprovar ou negar?\n"))
            
            print(f"{solicitacoes[solicitacao-1].get_unidade()} - {solicitacoes[solicitacao-1].get_sala()} - {solicitacoes[solicitacao-1].get_data()} - {solicitacoes[solicitacao-1].get_horario()} - {solicitacoes[solicitacao-1].get_usuario().get_nome()} - {solicitacoes[solicitacao-1].get_usuario().get_email()} - {solicitacoes[solicitacao-1].get_status()}\n")
            
            aprovacao = int(input("""1 - Aprovar\n2 - Negar\n"""))
            
            if aprovacao == 1:
                solicitacoes[solicitacao-1].set_status("Aprovado")
                reservas.append(solicitacoes[solicitacao-1])
                solicitacoes.pop(solicitacao-1)
            elif aprovacao == 2:
                solicitacoes[solicitacao-1].set_status("Negado")
                solicitacoes[solicitacao-1].get_usuario().set_reservas(solicitacoes[solicitacao-1])
                solicitacoes.pop(solicitacao-1)
                
        else:
            print("Sem solicitações no momento.")

    #UC-06: Restrigir sala
    def restringir_sala(self, salas):
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
            
    def consulta_historico(self, historico):
        if len(historico) > 0:
            for i in historico:
                print(f"{i.get_unidade()} - {i.get_sala()} - {i.get_data()} - {i.get_horario()} - {i.get_usuario().get_nome()} - {i.get_usuario().get_email()} - {i.get_status()}")
        else:
            print("Sem historico no momento.")