const numberFamilia = parseInt(prompt('Quantas pessoas estarão na lista: '))
const nomesNaLista = document.querySelector('#nomesNaLista')
const listaHTML = document.querySelector('#lista')
const buttonAdicionar = document.querySelector('#adicionar')

console.log(numberFamilia);


const lista = {}

for (i = 1; i <= numberFamilia; i++){
    const nomeDaPessoa = prompt(`Qual vai ser o ${i}º nome da lista`)
    lista[nomeDaPessoa] = []
}
console.log(lista);

for (let nome in lista){
    const pessoa = document.createElement('input')
    const labelPessoa = document.createElement('label')
    nomesNaLista.appendChild(pessoa)
    nomesNaLista.appendChild(labelPessoa)
    pessoa.name = 'selecionado'
    pessoa.type = 'radio'
    pessoa.value = nome
    labelPessoa.htmlFor = `${nome}`
    labelPessoa.innerText = `${nome}`
    
    const listaPessoa = document.createElement('div')
    const nomeDaLista = document.createElement('h1')
    listaPessoa.id = nome
    nomeDaLista.innerText = `${nome}`

    console.log(listaPessoa);

    listaPessoa.appendChild(nomeDaLista)
    listaHTML.appendChild(listaPessoa)

    

}
console.log(nomesNaLista);

function criarTarefas(){
        const nomeSelecionado = document.querySelector('input[name="selecionado"]:checked')
        const novaTarefas = document.querySelector('#novaTarefa').value

        if(nomeSelecionado !== null){
            const nomeSelecionadoValue = nomeSelecionado.value
            
            if (lista.hasOwnProperty(nomeSelecionadoValue)){
            lista[nomeSelecionadoValue].push(novaTarefas)
            console.log(`Nova tarefa adicionada para ${nomeSelecionadoValue}: ${novaTarefas}`);

            const listaPessoa = document.querySelector(`#${nomeSelecionadoValue}`)

            if(listaPessoa){
                const tarefaDaLista = document.createElement('p')
                tarefaDaLista.innerText = `${novaTarefas}`
    
                const alterar = document.createElement('button')
                alterar.innerText = "Nudar a tarefa"
                const excluir = document.createElement('button')
                excluir.innerText = "Excluir"
    
                listaPessoa.appendChild(tarefaDaLista)
                listaPessoa.appendChild(alterar)
                listaPessoa.appendChild(excluir)

                excluir.addEventListener('click', () => {
                    listaPessoa.removeChild(tarefaDaLista);
                    listaPessoa.removeChild(alterar);
                    listaPessoa.removeChild(excluir);
                    const index = lista[nomeSelecionadoValue].indexOf(novaTarefas);
                    if (index !== -1) {
                        lista[nomeSelecionadoValue].splice(index, 1);
                        console.log(`Tarefa excluída para ${nomeSelecionadoValue}: ${novaTarefas}`);
                    }
                });

                alterar.addEventListener('click', () => {
                    const novaTarefa = prompt('Insira a nova tarefa:');
                    if (novaTarefa !== null) {
                        tarefaDaLista.innerText = novaTarefa;
                        const index = lista[nomeSelecionadoValue].indexOf(novaTarefa);
                        if (index !== -1) {
                            lista[nomeSelecionadoValue][index] = novaTarefa;
                            console.log(`Tarefa alterada para ${nomeSelecionadoValue}: ${novaTarefa}`);
                        }
                    }
                });
                console.log(listaPessoa)
            } else{
                console.log('Div não encontrada.');
            }
        } else{
            console.log('Selecione um nome antes de adicionar a tarefa.');
        }
        
        
        console.log(novaTarefas);   
    }
    
}



buttonAdicionar.addEventListener('click', ()=>{
    criarTarefas()
})






