
# == While Loops ===

# Excelente para loop dependentes de uma condição.

# Publicar um produto com commissão de 10% se for acima de R$20.



valor = int(input('Digite o valor do seu produto: '))

while valor >= 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de r$ {valor}')
    break