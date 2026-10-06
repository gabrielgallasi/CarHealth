import os

from banco.conexao import criar_tabela
from cadastro.veiculo import cadastrar_veiculo, listar_veiculos, excluir_veiculo, excluir_todos_veiculos
from servicos.temperatura import verificar_temperatura
from servicos.bateria import verificar_bateria
from servicos.combustivel import calcular_consumo
from servicos.pneus import verificar_pneus
def exibir_opcoes():
    print("===== SISTEMA AUTOMOTIVO =====\n")
    print("1. Cadastrar veículo")
    print("2. Listar veículos")
    print("3. Serviços automotivos")
    print("4. Excluir todos os veículos")
    print("5. Excluir veículo")
    print("6. Sair\n")

def finalizar_app():
    os.system("cls")
    print("Finalizando sistema...\n")


def menu_servicos():
    while True:
        os.system("cls")

        print("===== SERVIÇOS AUTOMOTIVOS =====\n")
        print("1. Temperatura do motor")
        print("2. Tensão da bateria")
        print("3. Consumo de combustível")
        print("4. Pressão dos pneus")
        print("5. Voltar\n")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                verificar_temperatura()

            elif opcao == 2:
                verificar_bateria()

            elif opcao == 3:
                calcular_consumo()

            elif opcao == 4:
                verificar_pneus()

            elif opcao == 5:
                break

            else:
                print("\nOpção inválida!")

        except ValueError:
            print("\nDigite apenas números!")

        input("\nPressione ENTER para continuar...")


def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_veiculo()

        elif opcao_escolhida == 2:
            listar_veiculos()
        
        elif opcao_escolhida == 3:
            menu_servicos()                                       
                               
        elif opcao_escolhida == 4:
            excluir_todos_veiculos()
        
        elif opcao_escolhida == 5:
            excluir_veiculo()

        elif opcao_escolhida == 6:
            finalizar_app()
            return False

        else:
            print("\nOpção inválida!")

    except ValueError:
        print("\nDigite apenas números!")

    return True

def main():
    criar_tabela()

    continuar = True

    while continuar:
        os.system("cls")
        exibir_opcoes()
        continuar = escolher_opcao()

        if continuar:
            input("\nPressione ENTER para voltar ao menu...")

if __name__ == "__main__":
    main()

