# Elabore que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#À vista dinheiro/ cheque: 10% de desconto 
#À vista cartão: 5% de desconto 
# Em até duas vezes no cartão : Preço normal 
# 3x ou mais no cartão: 20% de juros 
produto = float(input('Informe o preço do produto :'))

print('Digite um dos números abaixo para informar a condição de pagamento')
print('1  À vista dinheiro/ cheque: 10% de desconto') 
print('2 - À vista cartão: 5% de desconto ')
print('3 - Em até duas vezes no cartão : Preço normal') 
print('4 - 3x ou mais no cartão: 20% de juros')
condicao = int(input())
if condicao == 1:
    print('O valor final é {}'.format(produto - (10*produto)/100))
elif condicao == 2:
    print('O valor final é {}'.format(produto - (5*produto)/100))
elif condicao == 3:
     print('O valor final é {}'.format(produto))
else: 
    print('Sua compra receberá juros de 20%, o valor final é {}'.format(produto + ((produto*20)/100)))

    