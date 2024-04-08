# conexão com banco de Dados MySql

import mysql.connector

db_config = {
    'host' : 'localhost',
    'user' : 'root',
    'password': 'abcd1234',
    'database' : 'estoque'
}
# coloquei um password aleatorio, atualize colocando o seu para funcionar no seu computador


# Programa para gerenciamento de estoque
# Funções

def adicionar_no_Banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()
    

def atualizar_Banco(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    conexao.commit()
    cursor.close()
    conexao.close()

def ver_Relatorio(query):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(query)
    lista_Resposta = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista_Resposta


# Menu

while True:
    menu = int(input('''
                Menu
                    
        1 - Adicionar produto
        2 - Gerar relatorio de estoque
        3 - Adicionar venda            
        4 - Gerar relatorio das vendas
        0 - Encerrar programa

        Escolha a opção desejada pelo número: '''))

    match menu:
        case 1:
            nome_Produto = str(input('Qual é o nome do produto: '))
            descricao_Produto = str(input('Descreva o produto ou coloque uma categoria: '))
            quantidade_Produto = int(input('Digite a quantidade dele no estoque:'))
            preco_Protudo = float(input('Digite o preço do produto: '))

            adicionar_no_Banco(f'''INSERT INTO produtos
                              (nome, descricao, quantidade, preco)
                              VALUES
                              ("{nome_Produto}", "{descricao_Produto}", {quantidade_Produto}, {preco_Protudo})''')

        case 2: 
            print(ver_Relatorio("SELECT * FROM produtos"))

        case 3:
            id_produto = int(input("Digite o id do produto: "))
            quantidade_vendida = int(input("Digite a quantidade vendida: "))
            data_venda = str(input("Digite a data da venda: "))

            adicionar_no_Banco(f'''INSERT INTO vendas
                            (id_produto, quantidade_vendidas, data_venda) 
                            VALUES
                            ({id_produto}, {quantidade_vendida}, "{data_venda}")''')
            
            atualizar_Banco(f'''UPDATE produtos
                                SET quantidade = {(quantidade_Produto)-(quantidade_vendida)}
                                WHERE id = {id_produto} ''')

        case 4:
            print(ver_Relatorio('SELECT * FROM vendas'))

        case 0:
            print('Programa Encerrado')
            break

        case _:
            print('Opção Invalida.')

