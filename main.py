# main.py
import funcoes as f
import utils as u

def menu():
    while True:
        print("\n--- Sistema de Locadora de Veículos ---")
        print("1. Cadastrar Veículo")
        print("2. Excluir Veículo")
        print("3. Listar Veículos")
        print("4. Pesquisar Veículo")
        print("5. Cadastrar Cliente")
        print("6. Excluir Cliente")
        print("7. Listar Clientes")
        print("8. Pesquisar Cliente")
        print("9. Locar Veículo")
        print("10. Devolver Veículo")
        print("11. Listar Locações")
        print("12. Pesquisar Locação")
        print("0. Sair")

        escolha = u.input_int("Escolha uma opção: ")

        if escolha == 1:
            f.cadastrar_veiculo()
        elif escolha == 2:
            f.excluir_veiculo()
        elif escolha == 3:
            f.listar_veiculos()
        elif escolha == 4:
            f.pesquisar_veiculo()
        elif escolha == 5:
            f.cadastrar_cliente()
        elif escolha == 6:
            f.excluir_cliente()
        elif escolha == 7:
            f.listar_clientes()
        elif escolha == 8:
            f.pesquisar_cliente()
        elif escolha == 9:
            f.locar_veiculo()
        elif escolha == 10:
            f.devolver_veiculo()
        elif escolha == 11:
            f.listar_locacoes()
        elif escolha == 12:
            f.pesquisar_locacao()
        elif escolha == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 0 e 12.")

if __name__ == "__main__":
    menu()

