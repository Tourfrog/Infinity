# Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.

# O programa deve fornecer as seguintes funcionalidades:

# Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.

# Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.

# Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.

# O programa deve ser executado em um loop contínuo até que o usuário escolha sair.




listAlunos = []

while True:
    action = str(input('''O que deseja fazer: 
                       a - adicionar aluno(a),
                       r - remover aluno(a),
                       v - visualizar lista de alunos,
                       s - sair do programa, 
                       digite apenas a primeira letra para efetuar a ação desejada
                       aqui =>  ''')).strip().lower()
    print('')
    match action:
        case('a'):

            aluno = {
                'nome' : str(input('Digite o nome do(a) aluno(a): ')),
                'matricula' : int(input('Digite o número da matricula: ')),
            }
            listAlunos.append(aluno)
        
        case('r'):
            remover = int(input('Digite a matricula de quem deseja remover: '))
            for aluno in listAlunos:
                if aluno['matricula'] == remover:
                    listAlunos.remove(aluno)
                    print(f'O(A) estudante {aluno["nome"]} foi removido(a) da lista.')
                    break

        case('v'):
            for aluno in listAlunos:
                print(aluno)
            
        case('s'):
            print('Fechou o programa')
            break

        case _:
            print('Digite apenas as letras requeridas, (a), (r), (v) e (s).')

    print('    ----    ')


            
    