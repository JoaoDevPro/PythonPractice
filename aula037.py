#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolhar qual será a base de execução:
# 1 para binário 
# 2 para octal
# 3 para hexadecimal 
n = int(input("informe um número qualquer "))
b = int(input("1 para binário ; 2 para octal; 3 para hexadecimal "))
if b == 1 :
   print('O número em binário é {}'.format(bin(n)[2:]))
elif b == 2 :
   print('O número em octal é {}'.format(oct(n)[2:]))
elif b == 3 :
   print('O número em hexadecimal é {}'.format(hex(n)[2:]))
else :
   print('Opção invalida')
