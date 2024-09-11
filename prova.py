class Locadora:
    def __init__(self):
        # Inicializa as listas para armazenar veículos, clientes e locações
        self.veiculos = []  # Lista para armazenar veículos
        self.clientes = []  # Lista para armazenar clientes
        self.locacoes = []  # Lista para armazenar locações

    def cadastrar_veiculo(self):
        # Solicita informações sobre o veículo e o adiciona à lista de veículos
        placa = input("Digite a placa do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        veiculo = {'placa': placa, 'modelo': modelo}  # Cria um dicionário para o veículo
        self.veiculos.append(veiculo)  # Adiciona o veículo à lista
        print("Veículo cadastrado com sucesso!")

    def cadastrar_cliente(self):
        # Solicita informações sobre o cliente e o adiciona à lista de clientes
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o e-mail do cliente: ")
        cliente = {'cpf': cpf, 'nome': nome, 'email': email}  # Cria um dicionário para o cliente
        self.clientes.append(cliente)  # Adiciona o cliente à lista
        print("Cliente cadastrado com sucesso!")

    def locar_veiculo(self):
        # Solicita informações para locar um veículo e registra a locação
        cpf = input("Digite o CPF do cliente: ")
        veiculo_placa = input("Digite a placa do veículo: ")
        dias = int(input("Quantos dias o cliente vai locar o veículo? "))  # Número de dias da locação
        
        # Definir o valor por dia (valor fixo)
        valor_por_dia = 120  # Valor fixo por dia de locação (exemplo: R$120 por dia)
        valor_total = dias * valor_por_dia  # Calcula o valor total da locação

        # Busca o cliente e o veículo pelo CPF e placa, respectivamente
        cliente = next((c for c in self.clientes if c['cpf'] == cpf), None)
        veiculo = next((v for v in self.veiculos if v['placa'] == veiculo_placa), None)

        # Verifica se o cliente e o veículo foram encontrados
        if cliente and veiculo:
            locacao = {
                'veiculo': veiculo,
                'cliente': cliente,
                'dias': dias,
                'valor': valor_total
            }  # Cria um dicionário para a locação
            self.locacoes.append(locacao)  # Adiciona a locação à lista
            print("Locação registrada com sucesso!")
        else:
            print("Cliente ou veículo não encontrado.")

    def gerar_relatorio(self):
        # Gera e imprime um relatório de todas as locações
        print("\nRelatório de Locações:")
        for locacao in self.locacoes:
            veiculo = locacao['veiculo']
            cliente = locacao['cliente']
            # Imprime os detalhes da locação
            print(f"Veículo: {veiculo['modelo']} ({veiculo['placa']})")
            print(f"Cliente: {cliente['nome']} (CPF: {cliente['cpf']})")
            print(f"Dias de locação: {locacao['dias']} dias")
            print(f"Valor cobrado: R${locacao['valor']:.2f}")
            print("-" * 30)

def menu():
    # Função principal que exibe o menu e processa as opções do usuário
    locadora = Locadora()  # Cria uma instância da classe Locadora
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar veículo")
        print("2. Cadastrar cliente")
        print("3. Locar veículo")
        print("4. Gerar relatório")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        # Executa a opção escolhida pelo usuário
        if escolha == '1':
            locadora.cadastrar_veiculo()
        elif escolha == '2':
            locadora.cadastrar_cliente()
        elif escolha == '3':
            locadora.locar_veiculo()
        elif escolha == '4':
            locadora.gerar_relatorio()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()  # Executa a função menu se o script for executado diretamente
