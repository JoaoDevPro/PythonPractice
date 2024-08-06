a = float(input("Qual a quantidade de km rodados pelo seu carro "))
b = float(input("Qual a quantidade de dia que voce usou seu carro "))
pk = a * 0.15
pc = b * 60
soma = pk + pc
print('O total que voce tem a pagar é {:.2f}'.format(soma))