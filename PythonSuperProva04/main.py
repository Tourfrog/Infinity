

listaDeNotas = []


def calcularMedia():
    somaDasNotas = 0
    for nota in listaDeNotas:
        somaDasNotas += nota
    
    media = somaDasNotas/len(listaDeNotas)
    # print(media)

    def vericarSituacao():
        if media == 10:
            print('Parabens, sua média é 10.')
        elif media >= 7:
            print('Aprovado.')
        else:
            print('Reprovado.')
        
    vericarSituacao()

    return f'A média das notas é {media}'


prova = 1
while True:
    nota = int(input(f'''Digite a nota da {prova}ª prova, e caso não tenha mais nota,
                      digite 50 para ver a média das notas: '''))
    print('')
    if nota == 50:
        # print(listaDeNotas)
        # calcularMedia()
        print(calcularMedia())
        break
    elif nota >= 0 and nota <= 10:
        listaDeNotas.append(nota)
        prova += 1
    else: 
        print('Digite apenas as notas de 0 até 10.')
    


        
    
    

