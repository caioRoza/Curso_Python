
# Functions (Funções)
    # DRY - Don't repeat yourself
    # Vários Argumentos (xargs) identificando o Parametro.

# Criar uma função que armazena numeros e strings (DADOS).


def agencia(**carro):
    return carro


print(agencia(marca='Volkswagen',modelo='Gol', cor='Branco', motor=1.0))
print(agencia(marca='Volkswagen',modelo='Gol', cor='Prata'))
print(agencia(marca='Volkswagen',modelo='Gol', cor='Preto', motor=1.6))