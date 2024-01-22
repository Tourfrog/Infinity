listaDeProdutos = []

# produtos = {
#     'nome': nome,
#     'quantidade': quantidade,
#     'valorUnidadeDoProduto': valorUnidadeDoProduto,
#     'valorTotalDoProfduto': valorTotalDoProduto
#     }


def adicionarProduto():
    nome = str(input('Digite o nome do produto: '))
    quantidade = int(input(f'Digite a quantidade de {nome} que temos no estoque: '))
    valorUnidadeDoProduto = float(input('Digite o preço da unidade deste produto: '))
    valorTotalDoProduto = valorUnidadeDoProduto * quantidade
    

    produto = {
        'nomeDoProduto': nome,
        'quantidadeDoProduto' : quantidade,
        'valorUnidadeDoProduto' : valorUnidadeDoProduto,
        'valorTotalDoProduto' : valorTotalDoProduto 

    }
    listaDeProdutos.append(produto)


def atualizarProduto():

    if len(listaDeProdutos) == 0:
        print('O estoque está vazio. Declare alguns produtos antes de realizar esta ação.')
    else:
        for produto in listaDeProdutos:
            print(produto['nomeDoProduto'])

        nomeDoProdutoParaSerMudado = str(input('Digite o nome do produto, que tu quer mudar:'))

        for produto in listaDeProdutos: 
            if produto['nomeDoProduto'] == nomeDoProdutoParaSerMudado:
                nome = str(input('Digite qual vai ser o novo nome do produto: '))
                quantidade = int(input(f'Digite a quantidade de {nome} que temos no estoque: '))
                valorUnidadeDoProduto = float(input('Digite o preço da unidade deste produto: '))
                valorTotalDoProduto = valorUnidadeDoProduto * quantidade

                produto['nomeDoProduto'] = nome
                produto['quantidadeDoProduto'] = quantidade
                produto['valorUnidadeDoProduto'] = valorUnidadeDoProduto
                produto['valorTotalDoProduto'] = valorTotalDoProduto 
            
        
        valorTotalDoEstoque() 


def excluirProduto() :
    
    if len(listaDeProdutos) == 0:
        print('O estoque está vazio. Declare alguns produtos antes de realizar esta ação.')
    else:
        for produto in listaDeProdutos:
            print(produto['nomeDoProduto'])

        produtoRemover = str(input('Digite o nome do produto a ser excluido: '))

        for produto in listaDeProdutos:
            if produto['nomeDoProduto'] == produtoRemover:
                listaDeProdutos.remove(produto)

        valorTotalDoEstoque()       


def verListadeProdutos():
    if len(listaDeProdutos) == 0:
        print('O estoque está vazio. Declare alguns produtos antes de realizar esta ação.')
    else:
        for i, produto in enumerate(listaDeProdutos):
            print(f'''
            {i+1} 
            Nome: {produto["nomeDoProduto"]}
            Quantidade: {produto["quantidadeDoProduto"]}
            Valor da unidade: {produto["valorUnidadeDoProduto"]}
            Valor total do produto: {produto["valorTotalDoProduto"]}
        ''')
            
        valorTotalDoEstoque()


def valorTotalDoEstoque():
    valorTotalDoEstoque = 0
    for produto in listaDeProdutos:
        valorTotalDoEstoque += produto['valorTotalDoProduto']

    print(f'O valor total de tudo que temos no estoque é R${valorTotalDoEstoque} reais.')


while True:
    try:
        menu = int(input("""
        Menu
                    
    1 - Adicionar produto
    2 - Atualizar o produto
    3 - Excluir o produto
    4 - Ver a lista o produto
    0 - Encerrar o programs
    Digite aqui, a opção desejada -> """))

        match menu:  
            case 1:
                adicionarProduto()
            
            case 2:
                atualizarProduto()

            case 3:
                excluirProduto()

            case 4:
                verListadeProdutos()

            case 0:
                print('Programa Encerrado!')
                break
        
            case _:
                print('Opção Invalida')
        

    except ValueError:
        print('Deu erro. Selecione apenas os números mostado no Menu.')
