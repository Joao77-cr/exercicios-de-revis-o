'''
#1
import csv


nome=input("nome")
nota1=input("nota1")
nota2=input("nota2")

dados =[
     ['nome','nota1,','nota2'],
     [nome,nota1,nota2],
]

with open('turma.csv','w',
          encoding='utf-8',
          newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)


with open('turma.csv','r',
          encoding='utf-8') as arquivo:
    leitor=csv.reader(arquivo)
    for linha  in leitor:
        print(linha)
    '''
#2

import csv

notas = [ 
     ['nome','nota01','nota02'],
     ['ana',8,7], 
     ['beto',9,6],
     ['luan',9,5],
]

with open('notas.csv','w',
          encoding='utf-8',
          newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in notas:
        escritor.writerow(linha)

notas_media = [ 
     ['nome','nota01','nota02', 'media'],
]

with open('notas.csv','r', encoding='utf-8') as arquivo:
    leitor=csv.DictReader(arquivo)
    for registro in leitor:
        nota1=float(registro['nota01'])
        nota2=float(registro['nota02'])
        media = (nota1+nota2)/2

        notas_media.appennd([registro('nome')],[registro('nota1')],[registro('nota2')],[registro('media')])

notas_m = [ 
     ['nome','nota01','nota02','media'],
     ['ana',8,7,'media'], 
     ['beto',9,6,'media'],
     ['luan',9,5,'media'],
]

with open('notas.csv','w',
          encoding='utf-8',
          newline='') as arquivo:
    escritor=csv.writer(arquivo)
    for linha in notas:
        escritor.writerow(linha)


#3

