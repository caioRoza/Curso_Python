
# == for loop nested ===

    # Outer loop
     # Inner loop
'''
Criar um retangulo 6x6
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''

linhas = 6
coluna = 6
simbol = 'ZZ'

for l in range(linhas):
    for c in range(coluna):
        print(simbol, end='')
    print()