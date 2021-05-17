import DAO
from cadastro import Cadastro

def main():
    while True:
        DAO.menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError as e:
            print("Valor inváldo!", e)
            continue
        
        if (opcao == 1):
            Cadastro.nome_anuncio = str(input("Nome do anúncio: "))
            Cadastro.cliente = str(input("Cliente: "))
            dias = DAO.valida_data()
            Cadastro.valor_diario = float(input("Valor diario investido: R$"))
            valor_total = Cadastro.valor_diario * dias
            DAO.calculador_vizualiza(valor_total)
            
        elif (opcao == 2):
            DAO.listar_anuncio()
        elif (opcao == 3):
            print("Obrigado por usar nosso sistema!!")
            break
        else:
            print("Opção inválida, tente novamente.")
            DAO.limpa_tela(2)
            continue
        DAO.limpa_tela_key()

if __name__ == "__main__":
    main()