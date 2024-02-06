
# Lambda Function
#     É uma função (pequena) sem nome
#     Pode ter varios argumentos mas somente 1 expressão
#     Muito utilizada dentro de outras funções
#     Código mais 'Clean'



somar10 = lambda x: x + 10
print(somar10(2))

somar_2_args = lambda x, y: x + y + 10
print(somar_2_args(10,2))

# def soma(x):
#     return x + 10
#
# print(soma(2))