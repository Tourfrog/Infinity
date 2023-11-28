

const listaNotas = []

function adicionarNotas(){
    const inputNotas = document.querySelector('#inputNotas').value

    if(listaNotas.includes(inputNotas)){
        alert('Esta nota já está aí embaixo.')
        return
    }

    listaNotas.push(inputNotas)

    const notaHtml = document.querySelector('#notasAdicionadas')
    notaHtml.innerHTML = ''

    for (let item in listaNotas){
        const nota = document.createElement('p')
        const buttonExcluir = document.createElement('button')
        const divNota = document.createElement('div')

        

        nota.innerText = `${listaNotas[item]}`
        buttonExcluir.innerText = 'Excluir'
        


        divNota.appendChild(nota)
        divNota.appendChild(buttonExcluir)
        notaHtml.appendChild(divNota)
        
        buttonExcluir.addEventListener('click', ()=>{
            const index = listaNotas.indexOf(listaNotas[item])
            listaNotas.splice(index , 1)
            notaHtml.removeChild(divNota)
        })

    }
}

document.querySelector('#inputNotas').addEventListener('keypress', (e)=>{
    if (e.key === 'Enter'){
        adicionarNotas()
        inputNotas.value = ''
    }
})

const buttonAdicionar = document.querySelector('#adicionarNotas')
buttonAdicionar.addEventListener('click', ()=>{
    adicionarNotas()
    console.log(listaNotas);
    inputNotas.value = ''
})
