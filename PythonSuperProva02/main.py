# Faça um programa que solicite ao usuário que digite 10 valores para
# preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista,
# e a soma de todos os números pares e ímpares, respectivamente.


list = []
list_Par = []
list_Impar = []
tuplaPar = ()
tuplaImpar = ()
somaPar = 0
somaImpar = 0

for i in range(10):
    number = int(input('Digite qualquer número inteiro: '))
    list.append(number)
    if number % 2 == 0 and number != 0:
        list_Par.append(number)
        tuplaPar += (number, )
        somaPar = somaPar + number
    elif number % 2 == 1 : 
        list_Impar.append(number)
        tuplaImpar += (number, )
        somaImpar = somaImpar + number
    else:
        print('Zero é neutro.')
        

print(f'Números pares em uma tupla: {tuplaPar}.')
print(f'Números impar em uma tupla: {tuplaImpar}.')
print('================')
print(f'Tem {len(tuplaPar)} números pares na tuplaPar.')
print(f'Tem {len(tuplaImpar)} números impares na tuplaImpar.')
print('=================')
print(f'A soma total da tuplaPar é {somaPar}')
print(f'A soma total da tuplaImpar é {somaImpar}')

print(type(tuplaImpar))
print(type(tuplaPar))
