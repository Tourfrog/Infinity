# [PY-A01] Faça um programa em python que determine em duas variáveis (senha e email)
# e que contenha uma senha e um email cadastrados antecipadamente,
# em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição
# juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email
# e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email
# e senha cadastrados ele continue em um loop.

loginCadastrado = 'Fulano'
senhaCadastrada = 'abc123'

while True:
    login = str(input('Digite o seu login: '))
    senha = str(input('Digite a sua senha: '))
    if login == loginCadastrado and senha == senhaCadastrada:
        print('Bem-vindo')
        break
    elif login == loginCadastrado and senha != senhaCadastrada:
        print('Tu errou a senha.')
    elif login != loginCadastrado and senha == senhaCadastrada:
        print('Tu errou o login')
    else:
        print('Login e senha erradas')

