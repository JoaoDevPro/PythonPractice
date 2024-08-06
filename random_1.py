import random
# Função objetivo: f(x) = x^2
def funcao_objetiva(x):
    #f=[]
    #f.append (100*(x[i] **2-x[i +1])**2+(x[i]-1)**2)
    #return np.sum(f)

maximo_interaçao = 1000 #critério de parada

x = 2
 #loop de busca aleatória
for i in range(maximo_interaçao):
    fx = funcao_objetiva() #avaliação da solução atual

    new_x = x + (random.random() - 0.5) * 0.1 #geração de uma nova solução proxima a x, estudar mais essa parte

    new_fx = funcao_objetiva(new_x) #avaliação da nova solução

    if new_fx < fx:  #aceitação
        x = new_x    #da nova solução se ela for melhor
print("O valor de x que minimiza a função é:", x)
print("O valor mínimo da função é:", funcao_objetiva(x))