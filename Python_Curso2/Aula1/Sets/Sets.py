
# Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index


list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

# Set union ( Une listas e remove os valores repetidos)
print(num1 | num2)

# Set difference( Mostra os valores diferente entre as listas de acordo com a ordem do parametro)
print(num1 - num2)
print(num2 - num1)

# Set Symmetric difference ( Retira os valores duplicados nas 2 listas)
print(num1 ^ num2)

# Set And ( Mostra os valores duplicados nas 2 listas)
print(num1 & num2)

print(len(num1)) # Quantidade de intens da lista

