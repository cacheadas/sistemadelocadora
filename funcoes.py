# funcoes.py
from time import sleep

# Listas para armazenar dados
lista_veiculos = []
lista_clientes = []
lista_locacoes = []

def cadastrar_veiculo():
    placa = input("Digite a placa do veículo: ").upper()
    modelo = input("Digite o modelo do veículo: ").capitalize()
    fabricante = input("Digite o fabricante do veículo: ").capitalize()

    if any(veiculo['placa'] == placa for veiculo in lista_veiculos):
        print("Veículo já cadastrado no sistema!")
        return

    veiculo = {'placa': placa, 'modelo': modelo, 'fabricante': fabricante}
    lista_veiculos.append(veiculo)
    print("Carregando...")
    sleep(1)
    print("Veículo cadastrado com sucesso!")

def excluir_veiculo():
    listar_veiculos()
    try:
        veiculo_excluir = int(input("Qual índice do veículo que deseja excluir: "))
        if 1 <= veiculo_excluir <= len(lista_veiculos):
            veiculo_removido = lista_veiculos.pop(veiculo_excluir - 1)
            print(f"Veículo com placa {veiculo_removido['placa']} excluído com sucesso!")
        else:
            print("Índice inválido")
    except ValueError:
        print("Digite apenas o índice, não o nome ou qualquer outra informação")

def listar_veiculos():
    print("Carregando veículos...")
    sleep(1)
    if not lista_veiculos:
        print("Nenhum veículo cadastrado no sistema!")
        return
    print('Veículos disponíveis:')
    for i, veiculo in enumerate(lista_veiculos, start=1):
        print(f"{i} - Placa: {veiculo['placa']}, Modelo: {veiculo['modelo']}, Fabricante: {veiculo['fabricante']}")

def pesquisar_veiculo():
    placa = input("Digite a placa do veículo que deseja pesquisar: ").upper()
    print("Procurando veículo...")
    sleep(1)
    veiculo = next((v for v in lista_veiculos if v['placa'] == placa), None)
    if veiculo:
        print(f"Veículo: Placa {veiculo['placa']}, Modelo: {veiculo['modelo']}, Fabricante: {veiculo['fabricante']}")
    else:
        print("Veículo não encontrado!")

def cadastrar_cliente():
    cpf = input("Digite o CPF do cliente (somente números): ")
    nome = input("Digite o nome do cliente: ").capitalize()
    email = input("Digite o email do cliente: ")

    if any(cliente['cpf'] == cpf for cliente in lista_clientes):
        print("Cliente já cadastrado no sistema!")
        return

    cliente = {'cpf': cpf, 'nome': nome, 'email': email}
    lista_clientes.append(cliente)
    print("Carregando...")
    sleep(1)
    print("Cliente cadastrado com sucesso!")

def excluir_cliente():
    listar_clientes()
    try:
        cliente_excluir = int(input("Qual índice do cliente que deseja excluir: "))
        if 1 <= cliente_excluir <= len(lista_clientes):
            cliente_removido = lista_clientes.pop(cliente_excluir - 1)
            print(f"Cliente com CPF {cliente_removido['cpf']} excluído com sucesso!")
        else:
            print("Índice inválido")
    except ValueError:
        print("Digite apenas o índice, não o nome ou qualquer outra informação")

def listar_clientes():
    print("Carregando clientes...")
    sleep(1)
    if not lista_clientes:
        print("Nenhum cliente cadastrado no sistema!")
        return
    print('Clientes cadastrados:')
    for i, cliente in enumerate(lista_clientes, start=1):
        print(f"{i} - Nome: {cliente['nome']}, CPF: {cliente['cpf']}, Email: {cliente['email']}")

def pesquisar_cliente():
    cpf = input("Digite o CPF do cliente que deseja pesquisar: ")
    print("Procurando cliente...")
    sleep(1)
    cliente = next((c for c in lista_clientes if c['cpf'] == cpf), None)
    if cliente:
        print(f"Cliente: Nome {cliente['nome']}, CPF: {cliente['cpf']}, Email: {cliente['email']}")
    else:
        print("Cliente não encontrado!")

def locar_veiculo():
    placa = input("Digite a placa do veículo que deseja locar: ").upper()
    cpf = input("Digite o CPF do cliente: ")

    veiculo = next((v for v in lista_veiculos if v['placa'] == placa), None)
    cliente = next((c for c in lista_clientes if c['cpf'] == cpf), None)

    if not veiculo:
        print("Veículo não encontrado!")
        return
    if not cliente:
        print("Cliente não encontrado!")
        return

    try:
        tempo_locacao = int(input("Quantos dias o cliente vai locar o veículo: "))
        valor = float(input("Qual será o valor da locação (R$): "))
    except ValueError:
        print("Tempo de locação e valor devem ser números!")
        return

    locacao = {'placa_veiculo': placa, 'nome_cliente': cliente['nome'], 'tempo_locacao': tempo_locacao, 'valor': valor}
    lista_locacoes.append(locacao)
    print("Locação realizada com sucesso!")

def devolver_veiculo():
    listar_locacoes()
    try:
        locacao_excluir = int(input("Qual índice da locação que deseja excluir: "))
        if 1 <= locacao_excluir <= len(lista_locacoes):
            locacao_removida = lista_locacoes.pop(locacao_excluir - 1)
            print(f"Locação do veículo {locacao_removida['placa_veiculo']} excluída com sucesso!")
        else:
            print("Índice inválido")
    except ValueError:
        print("Digite apenas o índice, não o nome ou qualquer outra informação")

def listar_locacoes():
    print("Carregando locações...")
    sleep(1)
    if not lista_locacoes:
        print("Nenhuma locação realizada!")
        return
    for i, locacao in enumerate(lista_locacoes, start=1):
        print(f"{i} - Veículo: {locacao['placa_veiculo']}, Cliente: {locacao['nome_cliente']}, Tempo: {locacao['tempo_locacao']} dias, Valor: R${locacao['valor']:.2f}")

def pesquisar_locacao():
    cpf = input("Digite o CPF do cliente que fez a locação: ")
    print("Procurando locação...")
    sleep(1)
    locacao_encontrada = False
    for locacao in lista_locacoes:
        if any(cliente['cpf'] == cpf for cliente in lista_clientes if cliente['nome'] == locacao['nome_cliente']):
            print(f"Locação: Veículo: {locacao['placa_veiculo']}, Cliente: {locacao['nome_cliente']}, Tempo: {locacao['tempo_locacao']} dias, Valor: R${locacao['valor']:.2f}")
            locacao_encontrada = True
            break
    if not locacao_encontrada:
        print("Locação não encontrada!")

