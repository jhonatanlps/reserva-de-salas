from reserva_salas import login, cadastrar
from usuario import Usuario
from admin import Admin

if __name__ == '__main__':
    solicitacoes = []
    reservas = []
    salas = {"Aclimação unidade 1": {"sala de jogos": 2, "laboratorio 1": 1, "laboratorio 2": 1, "laboratorio 3": 1, "maker lab":2},"Aclimação unidade 2": {"sala 101":1, "sala 102":1, "sala 103":1, "sala 104":1, "sala 201":1, "sala 202":1, "sala 203":1, "sala 204":1},
    "Paulista": {"sala 101":1, "sala 102":1, "sala 103":1, "sala 104":1, "sala 201":1, "sala 202":1, "sala 203":1, "sala 204":1, "laboratorio 1":1, "laboratorio 2":1, "laboratorio 3":1, "maker lab":2}}
    admin = Admin("admin", "admin@fiap.com.br", "adminsenha", 0)
    banco_dados = []
    banco_dados.append(admin)
    
    while(True):
        
        conta = input("\nVocê ja possui conta? (S/N)\n").upper()
        
        match conta:
            
            case "S":
                
                login(banco_dados, solicitacoes, reservas, salas)
            
            case "N":
                
                cadastrar(banco_dados, solicitacoes, reservas, salas)
            
            case _:
                
                print("Opção invalida, tente novamente")