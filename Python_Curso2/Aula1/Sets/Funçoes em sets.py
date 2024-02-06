
# Sets (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = set([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6}

s1.add(7)
print(s1)
s1.update([7, 8, 9, 10])

print(list1)
print(s1)
print(type(list1))
print(type(s1))