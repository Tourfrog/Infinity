class Biblioteca:
    def __init__(self) -> None:
        self.biblioteca_Catalogo = []
        self.registro_Membros = []

    # Fazer emprestimo, tornando livro do catalogo True ou False para disponivel e colocando no historico
    def loanBook(self):
        if len(self.biblioteca_Catalogo) < 1:
            print('Estamos sem livros no momento, tente mais tarde.')
        else:
            quemEstaLevando = str(input('Digite o seu número ou seu nome: '))
            contarLoopPorMembro = 1
            for membro in self.registro_Membros:
                if quemEstaLevando == membro.membro_Nome or int(quemEstaLevando) == membro.membro_Numero:
                    print('Emprestimo autorizado.')
                    pegarLivro = str(input('Qual é o livro que você quer alugar, digite o id ou o título: '))
                    contarLoopPorLivro = 1
                    for livro in self.biblioteca_Catalogo:
                        if pegarLivro == livro.livro_Titulo or int(pegarLivro) == livro.livro_ID:
                            if livro.livro_Disponivel == True:
                                membro.membro_Historico.append(livro)
                                livro.livro_Disponivel = False
                                print(f'O {membro.membro_Nome} alugou o livro {livro.livro_Titulo}.')
                                break
                            else:
                                print('Este livro já está alugado.')
                                break
                        else:
                            while contarLoopPorLivro < len(self.biblioteca_Catalogo):
                                contarLoopPorLivro += 1
                            else:
                                print('Não temos este livro especifico na biblioteca... Tente em outra biblioteca.')
                else:
                    while contarLoopPorMembro < len(self.registro_Membros):
                        contarLoopPorMembro += 1
                    else:
                        print('Usuario não identificado. Se registre antes, para alugar um livro.')
                                                                          
    # Devolver livro, recolocando livro no catalogo
    def returnBook(self):
        quemEstaDevolvendo = str(input('Digite ou o seu nome ou o seu número: '))
        contadorLoopDeMembro = 1
        for membro in self.registro_Membros:
            if quemEstaDevolvendo == membro.membro_Nome or int(quemEstaDevolvendo) == membro.membro_Numero:
                print('Membro encontrado')
                devolver = str(input('Digite o id do livro, que você quer devolver: '))
                contadorLoopDeLivro = 1
                for livro in self.biblioteca_Catalogo:
                    if devolver == livro.livro_Titulo or int(devolver) == livro.livro_ID:
                        livro.livro_Disponivel = True
                        print('O livro foi devolvido.')
                        break
                    else:
                        while contadorLoopDeLivro < len(self.biblioteca_Catalogo):
                            contadorLoopDeLivro += 1
                        else:
                            print('ID não localizado. Este livro provavelmente não pertence a esta biblioteca.')
            else:
                while contadorLoopDeMembro < len(self.registro_Membros):
                    contadorLoopDeMembro += 1
                else:
                    print('Usuario não registrado.')

    # pesquisar por Id, titulo ou autor
    def pesquisarLivro(self):
        if len(self.biblioteca_Catalogo) < 1:
            print('Estamos sem livros no momento, tente mais tarde.')
        else:
            pesquisar = str(input('Qual é o livro que você procura, digite o id ou o título ou o autor: '))
            contadorDePesquisar = 1
            for livro in self.biblioteca_Catalogo:
                if pesquisar == livro.livro_Titulo or pesquisar == livro.livro_Autor or int(pesquisar) == livro.livro_ID:
                    if livro.livro_Disponivel == True:
                        print(f'''
            --- Livro Encontrado ---
            ID: {livro.livro_ID}
            Título: {livro.livro_Titulo}
            Autor: {livro.livro_Autor}
            Disponevel para emprestimo: Sim''')
                        break
                    else:
                        print(f'''
            --- Livro Encontrado ---
            ID: {livro.livro_ID}
            Título: {livro.livro_Titulo}
            Autor: {livro.livro_Autor}
            Disponevel para emprestimo: Não''')
                        break
                else:
                    while contadorDePesquisar < len(self.biblioteca_Catalogo):
                        contadorDePesquisar += 1
                    else:
                        print('Não localizamos o livro que você procura, provavelmente não temos ele.')
                

    # adicionar livro no Catalogo
    def add_Livro_to_Biblioteca(self):
        idLivro = 1
        for i in self.biblioteca_Catalogo:
            idLivro += 1
        tituloDoLivro = str(input('Digite o titulo do livro: '))
        autorDoLivro = str(input('Digite o nome do(a) autor(a) do livro: '))
        livro = Livro(id=idLivro, titulo=tituloDoLivro, autor=autorDoLivro)
        contarVerificar_Livro = 1
        if len(self.biblioteca_Catalogo) == 0:
            self.biblioteca_Catalogo.append(livro)
            print('O livro foi adicionado com sucesso')
        else:
            for verificarSeTemosIgual in self.biblioteca_Catalogo:
                if verificarSeTemosIgual.livro_Titulo == livro.livro_Titulo:
                    print('Já temos esse livro, cancelando cadastro para evitar duplicação.')
                else:
                    while contarVerificar_Livro < len(self.biblioteca_Catalogo):
                        contarVerificar_Livro += 1
                    else:
                        self.biblioteca_Catalogo.append(livro)
                        print('O livro foi adicionado com sucesso')
        

    # adicionar membro no registro
    def add_Membro_to_Biblioteca(self):
        numeroMembro = 1
        for i in self.registro_Membros:
            numeroMembro += 1
        nomeDoMembro = str(input('Digite o nome do novo Membro: '))
        membro = Membro(numero=numeroMembro, nome=nomeDoMembro)
        contarVerificar_Membro = 1
        if len(self.registro_Membros) == 0:
            self.registro_Membros.append(membro)
            print('O membro foi cadastrado com sucesso')
        else:
            for verificarMembroIgual in self.registro_Membros:
                if verificarMembroIgual.membro_Nome == membro.membro_Nome:
                    print('O membro já está cadastrado, cancelando cadastro para evitar duplicação.')
                else:
                    while contarVerificar_Membro < len(self.registro_Membros):
                        contarVerificar_Membro += 1
                    else:
                        self.registro_Membros.append(membro)
                        print('O membro foi cadastrado com sucesso')


class Livro:
    def __init__(self, id:int, titulo:str, autor:str) -> None:
        self.livro_ID = id
        self.livro_Titulo = titulo
        self.livro_Autor = autor
        self.livro_Disponivel = True

class Membro:
    def __init__(self, numero:int, nome:str) -> None:
        self.membro_Numero = numero
        self.membro_Nome = nome
        self.membro_Historico = []


numeroMembro = 1
biblioteca = Biblioteca()

while True:
    menu = int(input('''
        Menu
    1 - Adicionar livro
    2 - Adicionar Membro
    3 - Pesquisar Livro
    4 - Alugar Livro 
    5 - Devolver Livro
    0 - Encerrar Programa
        
    Digite aqui a opção desejada -> '''))

    match menu:
        case 1:
            biblioteca.add_Livro_to_Biblioteca()
        case 2:
            biblioteca.add_Membro_to_Biblioteca()
        case 3:
            biblioteca.pesquisarLivro()
        case 4:
            biblioteca.loanBook()
        case 5:
            biblioteca.returnBook()
        case 0:
            print('Programa Biblioteca Encerrado')
            break
        case _:
            print('Opção Invalida')