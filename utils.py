# utils.py

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número decimal.")
