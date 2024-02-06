
# Functions (Funções)
    # DRY - Don't repeat yourself.
    # def (define) funções.
    # Parametro --> Argumento
    # Default = Aquele que você define o valor no parametro
    # Non-Default Aquele que você não define o valor no parametro

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} notebooks em estoque')

boas_vindas('Caio', 5)
boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 5)
'''
def boas_vindas_Caio():
    print('Olá Caio')
    print('Temos 5 notebooks em estoque')


def boas_vindas_Marcos():
    print('Olá Marcos')
    print('Temos 5 notebooks em estoque')


def boas_vindas_Ronaldo():
    print('Olá Ronaldo')
    print('Temos 5 notebooks em estoque')


boas_vindas_Caio()
boas_vindas_Marcos()
boas_vindas_Ronaldo()
'''