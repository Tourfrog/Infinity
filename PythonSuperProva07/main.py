listasDeAlunos = []

# Exemplo
# dicionarioDeAluno = {
#     'matricula': 123456,
#     'nome': 'Fulano da Silva'
# }

def adicionarAluno():
    
    nomeDoAluno = str(input('Digite o nome do aluno que vai ser adicionado: '))

    for aluno in listasDeAlunos:
        if aluno['nome'] == nomeDoAluno:
            print('Já existe aluno com esse nome.')
            return

    matriculaDoAluno = int(input('Digite qual será o número da matrícula dele: '))

    for aluno in listasDeAlunos:
        if aluno['matricula'] == matriculaDoAluno:
            print('Essa matrícula já está em uso.')
            return

    dicionarioDeAluno = {
        'nome': nomeDoAluno,
        'matricula': matriculaDoAluno
    }
    listasDeAlunos.append(dicionarioDeAluno)
    print('Aluno adicionado com sucesso!')
                   

def removerAluno():
    
    if len(listasDeAlunos) == 0:
        print('Você ainda não tem alunos!')
    else:
        for aluno in listasDeAlunos:
            print(f'''
            {aluno['nome']} - {aluno['matricula']}''')
        
        numeroDaMatricula = int(input('Digite o número da matricula do aluno para ser removido: '))

        for i, aluno in enumerate(listasDeAlunos):
            if aluno['matricula'] == numeroDaMatricula:
                listasDeAlunos.pop(i)
                print('Aluno removido com sucesso.')
                break
        else: 
            print('Aluno não encontrado.')
 

def atualizarNomeDoAluno():
    
    if len(listasDeAlunos) == 0:
        print('Você ainda não tem alunos!')
    else:
        for aluno in listasDeAlunos:
            print(f'''
            {aluno['nome']} - {aluno['matricula']}''')
        
        atualizarNome = int(input('Digite o número da matricula do aluno para atualizar o nome: '))

        matriculaExiste = False
        for aluno in listasDeAlunos:
            if aluno['matricula'] == atualizarNome:
                matriculaExiste = True
                aluno['nome'] = str(input('Digite o novo nome deste aluno: '))
                print('Nome atualizado com sucesso.')
                break
        if not matriculaExiste:
            print('Não foi encontrada essa matricula.')
    


def verListaDeAlunos():

    if len(listasDeAlunos) == 0:
        print('Você ainda não tem alunos!')
    else:
        for i, aluno in enumerate(listasDeAlunos):
            print(f'''
        {i + 1}º Aluno 
        {aluno['nome']} - {aluno['matricula']}
        ''')   
        

while True:
    menu = int(input('''
            Menu de Alunos:
        1 - Adicionar aluno
        2 - Remover aluno
        3 - Atualizar aluno
        4 - Ver a lista de todos os alunos
        0 - Encerrar o programa
        
        Digite aqui o número da opção desejada => '''))
    
    match menu:
        case 1:
            adicionarAluno()
        
        case 2:
            removerAluno()

        case 3:
            atualizarNomeDoAluno()

        case 4:
            verListaDeAlunos()

        case 0:
            print('Programa Encerrado.')
            break
            
        case _:
            print('Opção Invalida! Digite apenas os números de 0 à 4.')