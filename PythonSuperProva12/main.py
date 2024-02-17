class Material:
    def __init__(self, titulo:str, autor_Ou_Editora:str) -> None:
        self.tituloDoMaterial = titulo
        self.autorOuEditoraDoMaterial = autor_Ou_Editora

    def exibir_Informacoes(self):
        return f"""
        Titulo : {self.tituloDoMaterial},
        Autor ou Editora : {self.autorOuEditoraDoMaterial}
        """
    
class Livro(Material):
    def __init__(self, titulo: str, autor_Ou_Editora: str, genero:str) -> None:
        super().__init__(titulo, autor_Ou_Editora)
        self.generoDoLivro = genero

    def exibir_Informacoes(self):
        return f"""
        Titulo : {self.tituloDoMaterial},
        Autor ou Editora : {self.autorOuEditoraDoMaterial},
        Gênero : {self.generoDoLivro}
        """
    
class Revista(Material):
    def __init__(self, titulo: str, autor_Ou_Editora: str, edicao:int) -> None:
        super().__init__(titulo, autor_Ou_Editora)
        self.edicaoDaRevista = edicao

    def exibir_Informacoes(self):
        return f"""
        Titulo : {self.tituloDoMaterial},
        Autor ou Editora : {self.autorOuEditoraDoMaterial},
        Edição : {self.edicaoDaRevista}
        """
    

# Livro
livro1 = Livro(titulo='Beren and Luthien', autor_Ou_Editora='JR.R.Tolkien', genero='Fantasia')

# Revista
revista1 = Revista(titulo='Superinteressante', autor_Ou_Editora='Ed.April', edicao=448)


print('Testando classe Livro:')
print(livro1.exibir_Informacoes())

print('')

print('Testando classe Revista:')
print(revista1.exibir_Informacoes())


    