# lanche = (tupla), lanche = [lista], lanche = {dicionário}
'''lanche = ("hamburger", "suco", "pizza", "pudim", "batata frita")
#print(lanche[2])
#print(lanche[0:2]) #primeiro elemento até o 2, então o 2 é iguinorado
#print(lanche[1:]) # do 1 até o final
#print(lanche[-1]) # ao contrario
#len(lanche) #quantos elementos tem o lanche

for c in lanche:
    print(f'Eu vou comer comer {c}')
#outra maneira de fazer o for
for cont in range(0, len(lanche)):
    print(lanche[cont])
print(sorted(lanche)) # De maneira ordenada

a = (1, 2, 5, 8, 4, 2)
print(a)
print(a.count(2)) # quantas vezes aparece o número 2

print(a.index(2)) # A posição que aparece o número 2

pessoa = (32, "joão", True)
print(pessoa)
del(pessoa) # pra apagar a tubla'''

# Crie uma tupla preenchida com os 20 primeiros colocados da tabela Capeonato brasileiro de futebol, na ordem de colocação, depois mostre
# Os cinco primeiro colocados
# Os últimos 4 colocados 
# Uma lista com os times em ordem alfabética
# Em qual posição da tabela está o time da chapecoense

tupla = ("Botafogo", "Palmeiras", "Flamengo", "Atlético-MG", "Fluminense", "Grêmio", "Athletico-PR", "Internacional", "Fortaleza", "São Paulo", "Chapecoense", "Corinthians", "Santos", "Vasco da Gama", "Bahia", "Goiás", "Cuiabá", "Coritiba", "América-MG", "Red Bull Bragantino"
)
print(tupla[0:5])
print(tupla[-1],tupla[-2],tupla[-3],tupla[-4])
print(sorted(tupla))
#print(tupla.index("Chapecoense"))
n = tupla.index("Chapecoense")
print(f'A posição é {n + 1}')
