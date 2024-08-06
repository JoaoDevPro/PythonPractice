lista = []
maior = 0
menor = 0
for c in range (1,3,+1):
    nome = str(input('Qual seu nome? {}'.format(c)))
    idade = float(input('Qual sua idade? {}'.format(c)))
    genero = str(input('Qual genero vc se identifica? {}'.format(c)))
    dic = {"nome": nome, "idade": idade, "genero": genero}
    lista.append(dic)

for dic in lista:
    print(dic["idade"])
    if idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade
print('nome', maior)  
print('nome',menor)


print(lista)
    