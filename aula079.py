# Crie um programa onde o usuário possa digitas varios valores númericos e os cadastre em uma lista,
# Caso o número já exista lá dentro ele não ficará adcionado, e pergunte se a pessoa quer continuar, se sim o programa se repete
# No final serão exibidos todos os valores unicos digitados, em ordem crescente
# Se o valor foi duplicado o programa deve informar, e também listar os números em ordem
n = 0
valores = []

while n != 'n':
    num = int(input('Digite um valor: '))
    n = str(input('Quer continuar [s] ou [n]? '))
    if num in valores:
        print('valor já informado')
    else:
        valores.append(num)
        valores.sort()
    
print(valores)

    