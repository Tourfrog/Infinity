class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar) -> None:
        self.totalCapacidadeDoElevador = totalCapacidade
        self.atualCapacidadeDoElevador = atualCapacidade
        self.totalAndarDoElevador = totalAndar
        self.atualAndarDoElevador = atualAndar

    def subir(self):
        if self.atualAndarDoElevador == self.totalAndarDoElevador:
            return 'O elevador já está no topo.'
        else:
            self.atualAndarDoElevador += 1
            return f'Subindo para o {self.atualAndarDoElevador} andar.'
        
    def descer(self):
        if self.atualAndarDoElevador == 0:
            return 'O elevador já está no térreo.'
        else:
            self.atualAndarDoElevador -= 1
            return f'Descendo para o {self.atualAndarDoElevador} andar.'
        
    def entrar(self):
        if self.atualCapacidadeDoElevador == self.totalCapacidadeDoElevador:
            return 'O elevador já está cheio!'
        else:
            self.atualCapacidadeDoElevador += 1
            return f'Entrando uma pessoa, tem {self.atualCapacidadeDoElevador} pessoas no elevador.'
        
    def sair(self):
        if self.atualCapacidadeDoElevador == 0:
            return 'O elevador está vazio!'
        else:
            self.atualCapacidadeDoElevador -= 1
            return f'Saiu uma pessoa, sobrou {self.atualCapacidadeDoElevador} pessoa no elevador.'
        
elevador1 = Elevador(totalCapacidade=3, atualCapacidade=1, totalAndar=2, atualAndar=0)

print('Testando subir')

print(elevador1.subir())
print(elevador1.subir())
print(elevador1.subir())
print(elevador1.subir())

print('')
print('Testando descer')

print(elevador1.descer())
print(elevador1.descer())
print(elevador1.descer())
print(elevador1.descer())

print('')
print('Testando entrar')

print(elevador1.entrar())
print(elevador1.entrar())
print(elevador1.entrar())
print(elevador1.entrar())

print('')
print('Testando sair')

print(elevador1.sair())
print(elevador1.sair())
print(elevador1.sair())
print(elevador1.sair())
