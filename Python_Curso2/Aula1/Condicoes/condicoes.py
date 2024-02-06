
velocidade = input("Qual a velocidade? ")

if int(velocidade) > 100:
    print("Velocidade acima do permitido")
    print("Reduzir a velocidade")

elif int(velocidade) < 60:
    print("Aumentar a velocidade")
else:
    print("Boa viagem")
