import mysql.connector
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'acbd1234',
    'database': 'listaDeTarefas'
}
# Coloque o password certo que funcione no seu computador 

# Testando conexão com MySql
# try:
#     conexao = mysql.connector.connect(**db_config)
#     print('Conexão Estabelecida')
# except mysql.connector.Error as erro:
#     print(f'Erro de conexão: {erro}')
#     exit(1)


# FUNÇÂO

def siteAdicionar():
    if insideSubMainFrame:
        insideSubMainFrame.destroy()


    # Função para adicionar tarefas
    def adicionarTarefas():
        # pegando os valores dos inputs de tarefas e nomes 
        valorTarefa = str(tarefa_Input.get())
        valorNome = str(nome_Input.get())

        # abrindo conexão com MySql
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM tarefas')
        listaDeTarefas = cursor.fetchall()

        # Checar se já existe a tarefa na lista e impedir duplicação
        tarefa_Repetida = FALSE
        for item in listaDeTarefas:
            if item[1] == valorNome and item[2] == valorTarefa:
                tarefa_Repetida = TRUE

        if valorNome == '' or valorTarefa == '':
            confirmarAdicionar.configure(text='Não deixe espaço em branco antes de adicionar tarefa')
        else:
            if tarefa_Repetida == TRUE:
                confirmarAdicionar.configure(text='Já temos essa tarefa incluida na lista')
                cursor.close()
                conexao.close()

            else: 
                cursor.execute(f"INSERT INTO tarefas (nomePessoa, descricao, concluido) VALUES ('{valorNome}' , '{valorTarefa}' , FALSE) ")
                conexao.commit()

                # Verficando se deu certos
                # cursor.execute('SELECT * FROM tarefas')
                # listaNoMySQL = cursor.fetchall()

                # for itemTarefa in listaNoMySQL:
                #     print(itemTarefa)

                cursor.close()
                conexao.close()

                confirmarAdicionar.configure(text='Foi adicionada uma nova tarefa')

                tarefa_Input.delete(0,END)
                nome_Input.delete(0,END)
                nome_Input.focus()


    # Construção da 'pagina' Adicionar
    siteAdicionarFrame = Frame(subMainFrame)
    siteAdicionarFrame.pack(padx=5, pady=5)

    introTitle_Label = Label(siteAdicionarFrame, text='Adicionar Tarefas', bg='red', fg='white')
    introTitle_Label.pack()

    tarefa_Label = Label(siteAdicionarFrame, text='Escreva abaixo a tarefa')
    tarefa_Label.pack()
    tarefa_Input = Entry(siteAdicionarFrame)
    tarefa_Input.pack()

    afastar_Label = Label(siteAdicionarFrame)
    afastar_Label.pack(padx=3)

    nome_Label = Label(siteAdicionarFrame, text='Escreva abaixo o responsável dela')
    nome_Label.pack()
    nome_Input = Entry(siteAdicionarFrame)
    nome_Input.pack()


    btnAdicionarTarefa = Button(siteAdicionarFrame, text='Adicionar tarefa', command=adicionarTarefas)
    btnAdicionarTarefa.pack(pady=10)

    confirmarAdicionar = Label(siteAdicionarFrame, text='')
    confirmarAdicionar.pack(padx=10, pady=10)

    def voltarAoInicio():
        siteAdicionarFrame.destroy()
        firstFrame()

    btnVoltarAoInicio = Button(siteAdicionarFrame, text='Voltar ao inicio', command=voltarAoInicio)
    btnVoltarAoInicio.pack()

    


def siteVerLista():
    if insideSubMainFrame:
        insideSubMainFrame.destroy()

    # Construção do site Ver lista de Tarefas
    siteVerListaFrame = Frame(subMainFrame)
    siteVerListaFrame.pack()

    introTitle_LabelLista = Label(siteVerListaFrame, text='Ver lista de tarefas', bg='red', fg='white')
    introTitle_LabelLista.pack()

    areaDeListaFrame = Frame(siteVerListaFrame)
    areaDeListaFrame.pack()

    def limparTree():
        for item in tree.get_children():
            tree.delete(item)

    def criarTreeView():
        tree = ttk.Treeview(areaDeListaFrame, columns=['nome', 'tarefa', 'status'])
        tree.column('#0', width=50)
        tree.column('nome', width=100)
        tree.column('tarefa', width=200)
        tree.column('status', width=100)
        tree.heading('#0', text='ID')
        tree.heading('nome', text='Responsavel')
        tree.heading('tarefa', text='Tarefa')
        tree.heading('status', text='Status')

        lateral_Scrollbar = Scrollbar(areaDeListaFrame, orient='vertical', command=tree.yview)
        lateral_Scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=lateral_Scrollbar.set)
        tree.pack()

        return tree
    
    tree = criarTreeView()

    # Função para colocar lista do MySql no Tkinter
    def verListaNoFrame():
        limparTree()


        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM tarefas')
        listaNoMySQL = cursor.fetchall()

        for itemTarefa in listaNoMySQL:
            id_itemTarefa = itemTarefa[0]
            nome_itemTarefa = itemTarefa[1]
            descricao_itemTarefa = itemTarefa[2]
            concluido_itemTarefa = itemTarefa[3]

            if concluido_itemTarefa == 0:
                concluido_itemTarefa = 'Não concluido'
            else:
                concluido_itemTarefa = 'Concluido'

            tree.insert('', 'end', text=id_itemTarefa, values=[nome_itemTarefa, descricao_itemTarefa, concluido_itemTarefa])

        cursor.close()
        conexao.close()

    verListaNoFrame()

    mostrarPorNome_Label = Label(siteVerListaFrame, text='Digite o nome do resposavel para mostrar as tarefas dele')
    mostrarPorNome_Label.pack()
    mostrarPorNome_Input = Entry(siteVerListaFrame)
    mostrarPorNome_Input.pack()


    def filtrarPorNome():
        mostrarPorNome = str(mostrarPorNome_Input.get())
        limparTree()

        conexao =mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        cursor.execute(f'SELECT * FROM tarefas WHERE nomePessoa = "{mostrarPorNome}"')
        lista_por_Pesssoa_MySql = cursor.fetchall()

        for itemTarefaPorNome in lista_por_Pesssoa_MySql:
            id_itemTarefa = itemTarefaPorNome[0]
            nome_itemTarefa = itemTarefaPorNome[1]
            descricao_itemTarefa = itemTarefaPorNome[2]
            concluido_itemTarefa = itemTarefaPorNome[3]

            if concluido_itemTarefa == 0:
                concluido_itemTarefa = 'Não concluido'
            else:
                concluido_itemTarefa = 'Concluido'

            tree.insert('', 'end', text=id_itemTarefa, values=[nome_itemTarefa, descricao_itemTarefa, concluido_itemTarefa])

            cursor.close()
            conexao.close()

    btnFiltrarPorNome = Button(siteVerListaFrame, text='Filtrar por nome', command=filtrarPorNome)
    btnFiltrarPorNome.pack()

    def voltarAoInicio():
        siteVerListaFrame.destroy()
        firstFrame()

    btnVoltarAoInicio = Button(siteVerListaFrame, text='Voltar ao inicio', command=voltarAoInicio)
    btnVoltarAoInicio.pack(padx=10, pady=10)



radioButtonFrameAtualizar = None
areaDeMudar_Frame = None
def siteAtualizar():
    if insideSubMainFrame:
        insideSubMainFrame.destroy()


    def confirmarIdEscolhido():
        global radioButtonFrameAtualizar
        if radioButtonFrameAtualizar:
            radioButtonFrameAtualizar.destroy()

        # Prevenir quebra do programa, caso escreva letra ou deixe o espaço vazio
        is_Number = escolhaDoID_Input.get()

        if is_Number.isdigit():

            idEscolhido = int(is_Number)

            conexao = mysql.connector.connect(**db_config)
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
            idEscolhidoParaAtualizar = cursor.fetchall()

            cursor.execute('SELECT * FROM tarefas')
            pegarID = cursor.fetchall()

            cursor.close()
            conexao.close()
    

            # Verificar se o id existe na lista
            lista_deID = []
            for id in pegarID:
                lista_deID.append(id[0])

            idSele = 0
            for num in idEscolhidoParaAtualizar:
                idSele = num[0]


            if idSele in lista_deID:
                    
                for item in idEscolhidoParaAtualizar:
                        
                    nomeDo_item = item[1]
                    tarefaDo_item = item[2]
                    statusDo_item = item[3]

                    if statusDo_item == 0:
                        statusDo_item = 'Não concluido'
                    else:
                        statusDo_item = 'Concluido'
                    
                confirmacaoDaTarefa_Label.configure(text=f'Você escolheu o {nomeDo_item}, responsável por {tarefaDo_item}, {statusDo_item}')

                radioButtonFrameAtualizar = Frame(siteAtualizarFrame)
                radioButtonFrameAtualizar.pack()
                

                label_EscolherMudar = Label(radioButtonFrameAtualizar, text='Escolha o que quer mudar', bg='red', fg='white')
                label_EscolherMudar.pack()

                valor = IntVar()

                def pegarMudar():
                    mudar = valor.get()

                    def mudarNomeFunction():
                        atualizarNome = str(input_mudarNome.get())

                        conexao = mysql.connector.connect(**db_config)
                        cursor = conexao.cursor()
                        cursor.execute(f'UPDATE tarefas SET nomePessoa = "{atualizarNome}" WHERE id = "{idEscolhido}"')

                        cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
                        confirmarSeFuncionou = cursor.fetchall()
                        print(confirmarSeFuncionou) 

                        conexao.commit()
                        cursor.close()
                        conexao.close()

                        confirmacaoDaTarefa_Label.configure(text='O nome do responsavel foi atualizado.')
                        radioButtonFrameAtualizar.destroy()

                    def mudarTarefaFunction():
                        atualizarTarefa = str(input_mudarTarefa.get())

                        conexao = mysql.connector.connect(**db_config)
                        cursor = conexao.cursor()
                        cursor.execute(f'UPDATE tarefas SET tarefa = "{atualizarTarefa}" WHERE id = "{idEscolhido}"')

                        cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
                        confirmarSeFuncionou = cursor.fetchall()
                        print(confirmarSeFuncionou) 

                        conexao.commit()
                        cursor.close()
                        conexao.close()

                        confirmacaoDaTarefa_Label.configure(text='A tarefa foi modificada')
                        radioButtonFrameAtualizar.destroy()

                    def mudarStatusFunction():
                        atualizarStatus = mudarStatusButtonValue.get()

                        if atualizarStatus == 0:
                            # Atualizar tarefa concluida para não concluida

                            conexao = mysql.connector.connect(**db_config)
                            cursor = conexao.cursor()
                        
                            cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
                            verSeNaoEstaConcluido = cursor.fetchall()

                            cursor.close()
                            conexao.close()

                            for pegarNaoConcluido in verSeNaoEstaConcluido:
                                valorNaoConcluido = pegarNaoConcluido[0]

                            if valorNaoConcluido == atualizarStatus:
                                # informando a repetição da ação
                                confirmarAtualizarStatus_Label.configure(text='A tarefa ainda não está concluida')
                            else:
                                # Corrigindo para não concluida, em caso de engano de achar que foi concluida.
                                conexao = mysql.connector.connect(**db_config)
                                cursor = conexao.cursor()
                                cursor.execute(f'UPDATE tarefas SET concluido = {atualizarStatus} WHERE id = "{idEscolhido}"')
                                    
                                cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
                                confirmarSeMudou = cursor.fetchall()
                                print(confirmarSeMudou)

                                conexao.commit()
                                cursor.close()
                                conexao.close()

                                confirmarAtualizarStatus_Label.configure(text='A tarefa foi corrigida de volta para não concluida')
                                print(type(valorNaoConcluido))
                                print(type(atualizarStatus))

                        if atualizarStatus == 1:
                            # Atualizar a tarefa não concluida para concluida
                            
                            conexao = mysql.connector.connect(**db_config)
                            cursor = conexao.cursor()
                        
                            cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
                            verSeEstaConcluido = cursor.fetchall()

                            cursor.close()
                            conexao.close()

                            for pegarConcluido in verSeEstaConcluido:
                                valorConcluido = pegarConcluido[0]

                            if valorConcluido == atualizarStatus:
                                # informando a repetição da ação
                                confirmarAtualizarStatus_Label.configure(text='A tarefa já se encontra como Concluida')
                            else:
                                    # Atualizando para concluida
                                conexao = mysql.connector.connect(**db_config)
                                cursor = conexao.cursor()
                                cursor.execute(f'UPDATE tarefas SET concluido = {atualizarStatus} WHERE id = "{idEscolhido}"')
                                    
                                cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
                                confirmarSeMudou = cursor.fetchall()
                                print(confirmarSeMudou)

                                conexao.commit()
                                cursor.close()
                                conexao.close()

                                confirmarAtualizarStatus_Label.configure(text='A tarefa foi atualizada para concluida')

                    global areaDeMudar_Frame
                    if radioButtonFrameAtualizar:
                        if areaDeMudar_Frame:
                            areaDeMudar_Frame.destroy()

                    if mudar == 0:                        
                        areaDeMudar_Frame = Frame(radioButtonFrameAtualizar)
                        areaDeMudar_Frame.pack()
                        label_mudarNome = Label(areaDeMudar_Frame, text='Mudar nome do responsavel', bg='red', fg='white')
                        label_mudarNome.pack()
                        input_mudarNome = Entry(areaDeMudar_Frame)
                        input_mudarNome.pack()
                        btnMudarNome = Button(areaDeMudar_Frame, text='Mudar Nome', command=mudarNomeFunction)
                        btnMudarNome.pack()

                    elif mudar == 1:                        
                        areaDeMudar_Frame = Frame(radioButtonFrameAtualizar)
                        areaDeMudar_Frame.pack()
                        label_mudarTarefa = Label(areaDeMudar_Frame, text='Mudar tarefa', bg='red', fg='white')
                        label_mudarTarefa.pack()
                        input_mudarTarefa = Entry(areaDeMudar_Frame)
                        input_mudarTarefa.pack()
                        btnMudarTarefa = Button(areaDeMudar_Frame, text='Mudar tarefa', command=mudarTarefaFunction)
                        btnMudarTarefa.pack()

                    elif mudar == 2:                        
                        areaDeMudar_Frame = Frame(radioButtonFrameAtualizar)
                        areaDeMudar_Frame.pack()
                        label_mudarStatus = Label(areaDeMudar_Frame, text='Mudar Status', bg='red', fg='white')
                        label_mudarStatus.pack()

                        mudarStatusFrame = Frame(areaDeMudar_Frame)
                        mudarStatusFrame.pack()

                        mudarStatusButtonValue = IntVar()

                        status_Concluido = Radiobutton(mudarStatusFrame, text='Tarefa não  concluida', variable=mudarStatusButtonValue, value=0, pady=10, padx=10)
                        status_Concluido.grid(row=0, column=0)
                        status_Nao_Concluido = Radiobutton(mudarStatusFrame, text='Tarefa concluida', variable=mudarStatusButtonValue, value=1, padx=10, pady=10)
                        status_Nao_Concluido.grid(row=0, column=2)

                        btnMudarStatus = Button(mudarStatusFrame, text='Confirmar mudança', command=mudarStatusFunction)
                        btnMudarStatus.grid(row=1, column=1)

                        confirmarAtualizarStatus_Label = Label(mudarStatusFrame, text='')
                        confirmarAtualizarStatus_Label.grid(row=2, column=1)


                selectRadioButtonFrame = Frame(radioButtonFrameAtualizar)
                selectRadioButtonFrame.pack()

                mudarNome = Radiobutton(selectRadioButtonFrame, text='Nome', variable=valor, value=0, pady=10)
                mudarNome.grid(column=0, row=0)
                mudarTarefa = Radiobutton(selectRadioButtonFrame, text='Tarefa', variable=valor, value=1, pady=10)
                mudarTarefa.grid(column=1,row=0)
                mudarStatus = Radiobutton(selectRadioButtonFrame, text='Status', variable=valor, value=2, pady=10)
                mudarStatus.grid(column=2, row=0)
                btnSelectChange = Button(selectRadioButtonFrame, text='Selecionar', command=pegarMudar)
                btnSelectChange.grid(column=1,row=2)
                
            else:
                confirmacaoDaTarefa_Label.configure(text='Não tem tarefa com este id escolhido')
        
        elif is_Number == '':
            confirmacaoDaTarefa_Label.configure(text='Não deixe o espaço vazio')
    
        else:
            confirmacaoDaTarefa_Label.configure(text='Digite apenas numeros para procurar o id')
        
                 


    siteAtualizarFrame = Frame(subMainFrame)
    siteAtualizarFrame.pack()

    introTitle_LabelAtualizar = Label(siteAtualizarFrame, text='Atualizar', bg='red', fg='white')
    introTitle_LabelAtualizar.pack(padx=10, pady=10)

    escolhaDoID_Label = Label(siteAtualizarFrame, text='Escreva o id da tarefa que quer atualizar')
    escolhaDoID_Label.pack()
    escolhaDoID_Input = Entry(siteAtualizarFrame)
    escolhaDoID_Input.pack()

    btnConfirmarEscolhaID = Button(siteAtualizarFrame, text='Confirmar escolha', command=confirmarIdEscolhido)
    btnConfirmarEscolhaID.pack()

    confirmacaoDaTarefa_Label = Label(siteAtualizarFrame, text='')
    confirmacaoDaTarefa_Label.pack()

    def voltarAoInicio():
        siteAtualizarFrame.destroy()
        firstFrame()

    btnVoltarAoInicio = Button(siteAtualizarFrame, text='Voltar ao inicio', command=voltarAoInicio)
    btnVoltarAoInicio.pack(padx=10, pady=10)
    




def siteExcluir():
    if insideSubMainFrame:
        insideSubMainFrame.destroy()


    
    def confirmarIdEscolhido():

        is_Number = escolhaDoID_Input.get()

        if is_Number.isdigit():

            idEscolhido = int(escolhaDoID_Input.get())
            guardarIdParaExcluir = idEscolhido

            conexao = mysql.connector.connect(**db_config)
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM tarefas WHERE id = "{idEscolhido}"')
            idEscolhidoParaExcluir = cursor.fetchall()

            cursor.execute('SELECT * FROM tarefas')
            pegarID = cursor.fetchall()

            cursor.close()
            conexao.close()

            # Verificar se o id existe na lista
            lista_deID_paraExcluir = []
            for id in pegarID:
                lista_deID_paraExcluir.append(id[0])

            idSele_paraExcluir = 0
            for num in idEscolhidoParaExcluir:
                idSele_paraExcluir = num[0]

            if idSele_paraExcluir in lista_deID_paraExcluir:

                for item in idEscolhidoParaExcluir:
                    
                    nomeDo_item = item[1]
                    tarefaDo_item = item[2]
                    statusDo_item = item[3]

                if statusDo_item == 0:
                    statusDo_item = 'Não concluido'
                    confirmacaoDaTarefa_Label.configure(text=f'''Você escolheu o {nomeDo_item}, responsável por {tarefaDo_item}, {statusDo_item},
                não será possivel excluir ele, porque a tarefa ainda não foi concluida.''',  bg='red', fg='black')
                    escolhaDoID_Input.delete(0, END)
                    escolhaDoID_Input.focus()
                    

                else:
                    statusDo_item = 'Concluido'
                    confirmacaoDaTarefa_Label.configure(text=f'Você escolheu o {nomeDo_item}, responsável por {tarefaDo_item}, {statusDo_item}',  bg='black', fg='white')

                    def excluirTarefa():
                        conexao = mysql.connector.connect(**db_config)
                        cursor = conexao.cursor()
                        cursor.execute(f'DELETE FROM tarefas WHERE id = {guardarIdParaExcluir}')
                        conexao.commit()
                        cursor.close()
                        conexao.close()

                        confirmacaoDaTarefa_Label.configure(text='Tarefa excluida com sucesso')

                        excluirTarefa_Frame.destroy()

                    excluirTarefa_Frame = Frame(siteExcluirFrame)
                    excluirTarefa_Frame.pack()

                    btnExcluirTarefa = Button(excluirTarefa_Frame, text='Aperte este botão para excluir a tarefa', bg='red', fg='white', command=excluirTarefa)
                    btnExcluirTarefa.pack()
                
            else:
                confirmacaoDaTarefa_Label.configure(text='Não tem tarefa com este id selecionado')
                
        elif is_Number == '':
            confirmacaoDaTarefa_Label.configure(text='Não deixe o espaço vazio')
    
        else:
            confirmacaoDaTarefa_Label.configure(text='Digite apenas numeros para procurar o id')
        
        

    siteExcluirFrame = Frame(subMainFrame)
    siteExcluirFrame.pack()

    introTitle_LabelExcluir = Label(siteExcluirFrame, text='Excluir', bg='red', fg='white')
    introTitle_LabelExcluir.pack(padx=10, pady=10)

    escolhaDoID_Label = Label(siteExcluirFrame, text='Escreva o id da tarefa que quer excluir')
    escolhaDoID_Label.pack()
    escolhaDoID_Input = Entry(siteExcluirFrame)
    escolhaDoID_Input.pack()

    btnConfirmarEscolhaID = Button(siteExcluirFrame, text='Confirmar escolha', command=confirmarIdEscolhido, )
    btnConfirmarEscolhaID.pack()

    confirmacaoDaTarefa_Label = Label(siteExcluirFrame, text='')
    confirmacaoDaTarefa_Label.pack(padx=10, pady=10)

    def voltarAoInicio():
        siteExcluirFrame.destroy()
        firstFrame()

    btnVoltarAoInicio = Button(siteExcluirFrame, text='Voltar ao inicio', command=voltarAoInicio)
    btnVoltarAoInicio.pack(padx=10, pady=10)

    


def firstFrame():
    global insideSubMainFrame
    insideSubMainFrame = Frame(subMainFrame)
    insideSubMainFrame.pack()

    btnSiteAdicionar = Button(insideSubMainFrame, text='Para adicionar tarefas', command=siteAdicionar )
    btnSiteAdicionar.pack(pady=10)

    btnSiteVerLista = Button(insideSubMainFrame, text='Ver lista de tarefas', command=siteVerLista)
    btnSiteVerLista.pack(pady=10)

    btnSiteAtualizar = Button(insideSubMainFrame, text='Atualizar tarefas', command=siteAtualizar)
    btnSiteAtualizar.pack(pady=10)

    btnSiteExcluir = Button(insideSubMainFrame, text='Excluir tarefas', command=siteExcluir)
    btnSiteExcluir.pack(pady=10)

    btnEncerrarPrograma = Button(insideSubMainFrame, text='Fechar Programa', command=janela.destroy)
    btnEncerrarPrograma.pack(pady=10)



# =============================================
# TKINTER 
janela = Tk()

janela.title('Stark Enterprises')
janela.geometry('1200x500')

mainFrame = Frame(janela)
mainFrame.pack()

tituloLabel = Label(mainFrame, text='Stark Enterprises', fg='red',font=('Arial', 35), bg='black', )
tituloLabel.pack()

subMainFrame = Frame(mainFrame)
subMainFrame.pack()

insideSubMainFrame = Frame(subMainFrame)
insideSubMainFrame.pack()

btnSiteAdicionar = Button(insideSubMainFrame, text='Para adicionar tarefas', command=siteAdicionar )
btnSiteAdicionar.pack(pady=10)

btnSiteVerLista = Button(insideSubMainFrame, text='Ver lista de tarefas', command=siteVerLista)
btnSiteVerLista.pack(pady=10)

btnSiteAtualizar = Button(insideSubMainFrame, text='Atualizar tarefas', command=siteAtualizar)
btnSiteAtualizar.pack(pady=10)

btnSiteExcluir = Button(insideSubMainFrame, text='Excluir tarefas', command=siteExcluir)
btnSiteExcluir.pack(pady=10)

btnEncerrarPrograma = Button(insideSubMainFrame, text='Fechar Programa', command=janela.destroy)
btnEncerrarPrograma.pack(pady=10)




janela.mainloop()
