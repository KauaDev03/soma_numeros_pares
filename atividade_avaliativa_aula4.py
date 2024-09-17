inicio = int(input('Qual número inicial? '))
fim = int(input('Qual número final? '))
somaPar = 0
for c in range(inicio, fim+1):
    print(c)
    if c % 2 == 0:
        somaPar += c

if somaPar>0:
    print(f'A soma dos números pares é {somaPar}')
else:
    print('Não existe número par no intervalo!')
