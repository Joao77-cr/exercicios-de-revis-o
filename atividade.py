'''
#1
with open ('frutas.txt','w',encoding='utf-8') as arquivo :
    arquivo.write("maça\n")
    arquivo.write("abacaxi\n")
    arquivo.write("banana\n")
    arquivo.write("uva\n")
    arquivo.write("morango\n")




with open ('frutas.txt','r',encoding='utf-8') as arquivo :

    fruta=arquivo.read()
print (fruta)
'''
'''
#2
with open ('compras.txt','w',encoding='utf-8') as arquivo :
   pass


while True:
 
 produto1=input("digite o produto ou digite sair:")
 
 if produto1 =="sair":
    break
 with open ('compras.txt','a',encoding='utf-8') as arquivo :
    arquivo.write (produto1+"\n")


with open ('compras.txt','r',encoding='utf-8') as arquivo :

    linhas=arquivo.readlines()
    print(linhas)
  
'''
'''
#3
from datetime import datetime
while True:
    anotacao=input("anote")
    agenda=datetime.now().strftime('%d/%m/%Y  %H:%M')
    if anotacao=="fim":
     break
    with open ('diario.txt','a',encoding='utf-8') as arquivo :
     arquivo.write(anotacao)
     arquivo.write(agenda)

with open ('diario.txt','r',encoding='utf-8') as arquivo :

    conteudo=arquivo.read()
print (conteudo)
'''

#4 

with open ('nomes.txt','a',encoding='utf-8') as arquivo:
    arquivo.write("Guilherme\n")
    arquivo.write("João\n")
