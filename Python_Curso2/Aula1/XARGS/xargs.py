
# Functions (Funções)
    # DRY - Don't repeat yourself
    # Varios argumentos (XARGS)

# Criar uma função que soma varios numeros

def soma(*numeros):
    result = 0
    for num in numeros:
        result += num
    return result


x = soma(2,3,4,7)
print(x)

def sub(*numeros):
    result = 0
    for num in numeros:
        result -= num
    return result

x = sub(10, 20, -50)
print(x)