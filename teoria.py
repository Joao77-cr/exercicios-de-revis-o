#Sobrescreve com "w" 
with open ('teste.txt','w',encoding='utf-8') as arquivo :
    arquivo.write("primeira linha\n")
    arquivo.write("segunda linha\n")



#adiciona no fim com "a" append
with open ('teste.txt','a',encoding='utf-8') as arquivo :
    arquivo.write("primeira linha\n")
    arquivo.write("segunda linha\n")






#lendo  com "r" 
with open ('teste.txt','r',encoding='utf-8') as arquivo :

    conteudo=arquivo.read()
print (conteudo)

#lendo com "r" e "for"

with open ('teste.txt','r',encoding='utf-8') as arquivo :

    for linha in arquivo:
        print (linha.strip())

#lendo como lista
with open ('teste.txt','r',encoding='utf-8') as arquivo :

    linhas=arquivo.readlines()
    print(linhas)