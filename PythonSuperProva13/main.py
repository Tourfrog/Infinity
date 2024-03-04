class BombaDeCombustivel:
    def __init__(self) -> None:
        self.tipoDeCombustivel = None
        self.valorLitro = None
        self.quantidadeCombustivel = 1000

    # Escolha do tipo de abastecimento
    def abastecerPor(self):
        menuAbastecer = int(input('''
            Menu
        1 - Abastecer por valor
        2 - Abastecer por litro
                                  
        Digite a opção desejada -> '''))

        match menuAbastecer:
            case 1:
                bomba.abastecerPorValor()
            case 2:
                bomba.abastecerPorLitro()
            case _:
                print('Opção Invalida.')

    # abastecer por valor
    def abastecerPorValor(self):
        valorTotal = float(input('Quantos reais, tu quer colocar na bomba? -> '))
        if self.tipoDeCombustivel == 'alcool':
            retiradaDeCombustivel = valorTotal / self.valorLitro
            if retiradaDeCombustivel > self.quantidadeCombustivel:
                print(f'Não foi possivel fazer a retirada de combustivel, você está pedindo mais do que podemos ofertar')
            else:
                print(f'Você retirou {retiradaDeCombustivel:.2f} l de alcool')
                self.alterarQuantidadeCombustivel(retiradaDeCombustivel) 
                print(f'{self.quantidadeCombustivel}')
        elif self.tipoDeCombustivel == 'diesel':
            retiradaDeCombustivel = valorTotal / self.valorLitro
            if retiradaDeCombustivel > self.quantidadeCombustivel:
                print(f'Não foi possivel fazer a retirada de combustivel, você está pedindo mais do que podemos ofertar')
            else:
                print(f'Você retirou {retiradaDeCombustivel:.2f} l de diesel')
                self.alterarQuantidadeCombustivel(retiradaDeCombustivel) 
                print(f'{self.quantidadeCombustivel}')
        elif self.tipoDeCombustivel == 'gasolina':
            retiradaDeCombustivel = valorTotal / self.valorLitro
            if retiradaDeCombustivel > self.quantidadeCombustivel:
                print(f'Não foi possivel fazer a retirada de combustivel, você está pedindo mais do que podemos ofertar')
            else:
                print(f'Você retirou {retiradaDeCombustivel:.2f} l de gasolina')
                self.alterarQuantidadeCombustivel(retiradaDeCombustivel) 
                print(f'{self.quantidadeCombustivel}')
    
    # abastecer por litro
    def abastecerPorLitro(self):
        litroTotal = int(input('Quantos litros você quer retirar -> '))
        if litroTotal > self.quantidadeCombustivel:
            print(f'Não temos essa quantidade de combustivel, resta na bomba: {self.quantidadeCombustivel} litros')
        else:
            if self.tipoDeCombustivel == 'alcool':
                custoTotalDoCombustivel = litroTotal * self.valorLitro
                self.alterarQuantidadeCombustivel(litroTotal)
                print(f'{self.quantidadeCombustivel}')
                print(f'Você pagou R${custoTotalDoCombustivel:.2f}.')
            elif self.tipoDeCombustivel == 'diesel':
                custoTotalDoCombustivel = litroTotal * self.valorLitro
                self.alterarQuantidadeCombustivel(litroTotal)
                print(f'{self.quantidadeCombustivel}')
                print(f'Você pagou R${custoTotalDoCombustivel:.2f}.')
            elif self.tipoDeCombustivel == 'gasolina':
                custoTotalDoCombustivel = litroTotal * self.valorLitro
                self.alterarQuantidadeCombustivel(litroTotal)
                print(f'{self.quantidadeCombustivel}')
                print(f'Você pagou R${custoTotalDoCombustivel:.2f}.')

    # Atualizar o valor do combustivel
    def alterarValor(self):
        if self.tipoDeCombustivel == 'alcool':
            novoValor = float(input('Declare qual vai ser o novo valor por litro do alcool -> '))
            print(f'O combustivel {self.tipoDeCombustivel}, teve o valor atualizado para {novoValor}')
            self.valorLitro = novoValor
            bomba.abastecerPor()

        elif self.tipoDeCombustivel == 'diesel':
            novoValor = float(input('Declare qual vai ser o novo valor por litro do diesel -> '))
            print(f'O combustivel {self.tipoDeCombustivel}, teve o valor atualizado para {novoValor}')
            self.valorLitro = novoValor
            bomba.abastecerPor()

        elif self.tipoDeCombustivel == 'gasolina':
            novoValor = float(input('Declare qual vai ser o novo valor por litro da gasolina -> '))
            print(f'O combustivel {self.tipoDeCombustivel}, teve o valor atualizado para {novoValor}')
            self.valorLitro = novoValor
            bomba.abastecerPor()

    # Escolher o tipo de combustivel
    def alterarTipoDeCombustivel(self):
        menuTipoDeCombustivel = int(input('''
            Menu Tipo de Combustivel
    1 - Alcool
    2 - Gasolina
    3 - Diesel
    
    Digite o número do combustivel que você quer -> '''))
        match menuTipoDeCombustivel:
            case 1:
                self.tipoDeCombustivel = 'alcool'
                print(f'Você escolheu {self.tipoDeCombustivel}.')
                bomba.alterarValor()

            case 2:
                self.tipoDeCombustivel = 'gasolina'
                print(f'Você escolheu {self.tipoDeCombustivel}.')
                bomba.alterarValor()

            case 3:
                self.tipoDeCombustivel = 'diesel'
                print(f'Você escolheu {self.tipoDeCombustivel}.')
                bomba.alterarValor()

            case _:
                print(f'Opção Invalida.')

    # diminuir a quantidade de combustivel na bomba
    def alterarQuantidadeCombustivel(self, retirarCombustivel):
        reserva =  self.quantidadeCombustivel - retirarCombustivel
        self.quantidadeCombustivel = reserva
        print(f'Agora resta {self.quantidadeCombustivel} na bomba.')


bomba = BombaDeCombustivel()
while True:
    menu = int(input('''
            Menu
    1 - Escolher Combustivel
    0 - Encerrar programa
                     
    Digite a opção desejada -> '''))

    match menu:
        case 1:
            bomba.alterarTipoDeCombustivel()

        case 0:
            print('Programa Encerrado')
            break

        case _:
            print('Opção Invalida')



    

        
