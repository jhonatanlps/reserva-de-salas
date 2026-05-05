from services.reserva_salas import menu
from auth.signin import cadastrar
from repositories.db import db
from auth.login import login


def shutdown():
    """ Função para salvar os dados no banco de dados ao finalizar o programa. """
    reservas = conexao.get_reservas()
    solicitacoes = conexao.get_solicitacoes()
    usuarios = conexao.get_usuarios()
    salas = conexao.get_salas()
    conexao.save_database(reservas, solicitacoes, usuarios, salas)
    print("Alterações salvas no banco de dados.")

if __name__ == '__main__':
    conexao = db()
    
    solicitacoes: list = conexao.get_solicitacoes()
    reservas: list = conexao.get_reservas()
    salas: dict = conexao.get_salas()
    usuarios: dict = conexao.get_usuarios()
    datas: list = conexao.get_datas()
    horarios: list = conexao.get_horarios()

    try:  
        while(True):
            conta = input("\nVocê ja possui conta? (S/N) - Finalizar a sessão (F)\n").upper()
            
            match conta:
                case "S":
                    autenticado, user = login(usuarios, solicitacoes, reservas, salas)

                    if autenticado:
                        menu(user, solicitacoes, reservas, salas, datas, horarios, usuarios)

                case "N":
                    cadastrado, novos_usuarios = cadastrar(usuarios, solicitacoes, reservas, salas)
                    
                    if cadastrado:
                        conexao.set_usuarios(novos_usuarios)
                case "F":
                    print("\nFinalizando...")
                    break
                case _:
                    print("Opção invalida, tente novamente")
    finally:
        #TODO: Salvar os dados no banco de dados ao finalizar o programa.
        shutdown()