
# Listas
    # Armazenar mais de uma informação em variaveis.
    # Manter a sequencia dos dados em uma variavel.

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro ', 'São Paulo', 'Salvador', 'Curitiba']
#                0                1            2          3

cidades.sort()
cidades[3] = 'Brasília'
print(cidades)

print(cidades[0])
print(cidades[-1])

cidades.append('Goiania')
print(cidades)

cidades.remove('Salvador')
print(cidades)

cidades.insert(1, 'Santa Catarina')
print(cidades)

cidades.pop(0)
print(cidades)

