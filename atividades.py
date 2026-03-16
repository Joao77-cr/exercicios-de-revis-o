'''
##11
contato = {
    'nome':'Lucas',
    'telefone': 3299675,
    'telefone' : 3212345,
    'email':'joaovictro@gmail',
    'cidade':'Rio pomba'
    
}

contato['Instagram'] = 'Guilherme_GK'
del contato['telefone']
if 'nome' in contato:
    print('Chave existe!')


print(contato)

'''
#12
'''
frase = 'o rato roeu a roupa do rei de roma'

palavras = frase.split()

contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)
'''
#13
'''
turma = {
    'Guilherme':[9.0, 10.0, 6.0],
    'João': [10.0, 9.5, 9.0],
    'Maíra' : [8.0, 7.5, 9.0],
    'Cazé': [8.0, 7.5, 9.0],
    'Bruna': [8.0, 7.5, 9.0] 
}

for aluno, notas in turma.items():
    media = sum(notas) / len(notas)
    
    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    print(f"{aluno} – Média: {media:.1f} – Situação: {situacao}")
'''
