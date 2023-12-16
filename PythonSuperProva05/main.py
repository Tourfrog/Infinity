
from functools import reduce


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado = list(map(lambda num : num ** 2, numeros))
print(quadrado)

numerosPares = list(filter(lambda num : num % 2 == 0, numeros))
print(numerosPares)

somasDosNumeros = reduce(lambda x,y : x + y, numeros)
print(somasDosNumeros)