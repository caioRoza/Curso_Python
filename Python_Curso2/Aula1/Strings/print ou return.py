
# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Realizam uma tarefa.
    # Calcula e retorna um valor.

def cliente1(nome):
    print(f'Ola {nome}')

def cliente2(nome):
    return f'Ola {nome}'


x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)
