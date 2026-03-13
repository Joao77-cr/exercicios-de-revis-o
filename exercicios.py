'''
#exercicios

#1
notas = ['7.5' ,'8.0', '6.0','9.5', '5.0']

#b
notas.append('8.5')

#c
notas.remove('5.0')
notas.insert(4, '6.5') 



#d
notas.sort(reverse=True) 

#e
print(max(notas))
print(min(notas))
'''
'''
#2
nomes=['maira','Bruna','guilherme','heitor','caze']
x=0

for x in range(0,5):
    print (x+1,nomes[x])


    x+=1

for i, nomes in enumerate(nomes):
    print(f'{i+1}: {nomes}')

'''
'''
#3
numeros = [3, 17, 8, 42, 5, 100, 23, 66, 11, 99]
Listapar=[]
for n in numeros:
    if n %2 ==0:
        Listapar.append(n)
print(Listapar)


Listamaior=[]
for n in numeros:
    if n >20:
        Listamaior.append(n)
print(Listamaior)
'''

'''
#4
num = []

for x in range(0,10):
    num.append(x+1)

    x+=1

print(num)
print(num[:4])
print(num[7:])
print(num[1:10:2])
'''
