
# Dicionários
    # Utiliza index no formato de Keys e Values
    # Aceita String, integer, float, boolean...



aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}


print(aluno.get('endereco', 'Não existe'))

# aluno.update({'nome':'Jose', 'nota_final': 'B'})
aluno.update({'endereco':'Rua A'})
# # aluno['nome'] = 'Jose'
print(aluno)

del aluno['endereco']

print(aluno)