#refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos de uma progressão usando a estrutura while
termo = int(input('digite o primeiro termo: '))
pa = int(input('digite sua pa: '))
cont = 0
n1 = termo
print('{} ->'.format(termo))
while cont < 10 :
  n1  +=  pa
  cont = cont + 1
  print('Sua progressão é de {} '.format(n1), end= '->')
print('Fim do programa')
  
  