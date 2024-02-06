numeros = [3, 5, 12, 2, 15, 6]
amigos = ['Marcos', 'Adriana', 'Pedro', 'Karina', 'Julia']
amigos.append('Joao')
amigos.insert(1, 'Joao')
amigos.remove('Adriana')
amigos.pop(0)


amigos.sort()

amigos.extend(numeros)
print(amigos)
print(amigos.index('Pedro'))
print(amigos.count('Joao'))


print(amigos)


