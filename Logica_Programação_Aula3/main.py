numero = int(input('Digite um numero qualquer, para ver na tabuada: '))

for i in range(10):
    resultado = numero * (i + 1)
    print(f'{numero} x {i + 1} = {resultado}' )