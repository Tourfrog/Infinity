velocidade = float(input('O quão rapido você estava dirigindo o seu carro? '))


conversor = velocidade - 80

multa = 20 * conversor

if velocidade > 80: 
    print(f'Você foi multado, terá que pagar R${multa}.')
else:
    print('Não tem nenhuma multa')


