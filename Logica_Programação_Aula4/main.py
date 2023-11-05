
quantidade_de_numeros = 0
soma = 0
media = 0

while True:
    numero = int(input('Digite um numero inteiro: '))
    if numero != 0:
        quantidade_de_numeros = quantidade_de_numeros + 1
        soma = soma + numero
        media = soma / quantidade_de_numeros
    else:
        print(f'Você digitou {quantidade_de_numeros} vezes, a soma deles é {soma} e por fim a media {media}.')