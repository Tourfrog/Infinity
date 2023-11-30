
const perguntas = [
    //Dom Pedro II
    {
        pergunta: "Qual foi o principal legado do imperador Dom Pedro II do Brasil?",
        escolhas: [
            "Abolição da escravidão",
            "Proclamação da República",
            "Independência do Brasil",
            "Modernização e estabilidade política"
        ],
        reposta: 3
    },
    {
        pergunta: "Em que ano ocorreu a Proclamação da República, que resultou na queda de Dom Pedro II do trono?",
        escolhas: [
          "1889",
          "1822",
          "1900",
          "1848"
        ],
        resposta: 0
    },
    {
        pergunta: "Qual era o título oficial de Dom Pedro II antes de se tornar imperador do Brasil?",
        escolhas: [
          "Conde de Ouro Preto",
          "Duque de Caxias",
          "Príncipe Regente",
          "Conde d'Eu"
        ],
        resposta: 2
    },
    {
        pergunta: "Qual era a área de interesse intelectual de Dom Pedro II?",
        escolhas: [
          "Matemática",
          "Literatura",
          "Astronomia",
          "Biologia"
        ],
        resposta: 2
    },

    //Albert Einstein
    {
        pergunta: "Qual cientista propôs a Teoria da Relatividade?",
        escolhas: [
            "Isaac Newton",
            "Galileu Galilei",
            "Albert Einstein",
            "Stephen Hawking"],
        resposta: 2 
    },
    {
        pergunta: "Em que ano Albert Einstein publicou sua Teoria da Relatividade Geral?",
        escolhas: [
          "1915",
          "1905",
          "1921",
          "1933"
        ],
        resposta: 0
    },
    {
        pergunta: "Em que país Albert Einstein nasceu?",
        escolhas: [
          "Alemanha",
          "Estados Unidos",
          "Áustria",
          "Suíça"
        ],
        resposta: 2
    },
    {
        pergunta: "Qual prêmio Nobel Albert Einstein ganhou?",
        escolhas: [
          "Paz",
          "Literatura",
          "Química",
          "Física"
        ],
        resposta: 3
    },

    //José Bonifácio
    {
        pergunta: "Qual foi o papel de José Bonifácio de Andrada e Silva no contexto da história do Brasil?",
        escolhas: [
            "Líder da Inconfidência Mineira",
            "Defensor da Independência do Brasil",
            "Primeiro presidente do Brasil",
            "General do Exército Brasileiro"
        ],
        reposta: 1 
    },
    {
        pergunta: "Qual era o apelido de José Bonifácio?",
        escolhas: [
          "Patriarca da Independência",
          "Libertador dos Escravos",
          "O Grande Político",
          "O Estadista"
        ],
        resposta: 0
    },
    {
        pergunta: "Qual foi o cargo oficial ocupado por José Bonifácio após a independência do Brasil?",
        escolhas: [
          "Presidente da República",
          "Ministro do Reino",
          "Imperador do Brasil",
          "Governador-geral"
        ],
        resposta: 1
    },
    {
        pergunta: "Qual era a área de interesse científico de José Bonifácio?",
        escolhas: [
          "Biologia marinha",
          "Astronomia",
          "Química",
          "Geologia"
        ],
        resposta: 3
    },

    //Calígula
    {
        pergunta: "Qual imperador romano ficou conhecido por sua extravagância e crueldade?",
        escolhas: [
            "Julio César", 
            "Calígula", 
            "Augusto", 
            "Nero"],
        resposta: 1 
    },
    {
        pergunta: "Qual foi o apelido original de Calígula?",
        escolhas: [
          "Gaius Julius Caesar",
          "Augustus",
          "Gaius Germanicus",
          "Tiberius"
        ],
        resposta: 2
    },
    {
        pergunta: "Qual evento político marcou o início do governo de Calígula?",
        escolhas: [
          "A guerra contra Cartago",
          "O assassinato de Júlio César",
          "A morte de Tibério",
          "A eleição para cônsul"
        ],
        resposta: 2
    },
    {
        pergunta: "Calígula foi assassinado por conspiradores em que ano?",
        escolhas: [
          "41 d.C.",
          "54 d.C.",
          "68 d.C.",
          "79 d.C."
        ],
        resposta: 0
    }

];

let perguntaAtual = null

let contarResposta = 1
let acertou = 0
let errou = 0



function perguntaAleatoria(){
    const indexAleotorio = Math.floor(Math.random() * perguntas.length)
    perguntaAtual = perguntas[indexAleotorio]
    document.querySelector('#pergunta').innerText = perguntaAtual.pergunta

    const escolhasDiv = document.querySelector('#escolhas')
    escolhasDiv.innerHTML = ''

    perguntaAtual.escolhas.forEach((escolha, index) =>{
        const botao = document.createElement('button')
        botao.innerText = escolha
        botao.classList.add('escolha')
        botao.addEventListener('click', ()=> checarResposta(index))
        escolhasDiv.appendChild(botao)
    })
    perguntas.splice(indexAleotorio, 1)
    // console.log(indexAleotorio);
}

function checarResposta(indexSelecionado){
    if (indexSelecionado === perguntaAtual.reposta){
        alert('Acertou!')
        acertou += 1
    } else{
        alert('Errou! Tente outra vez.')
        errou += 1
    }

    contarResposta += 1;
    if (contarResposta > 4) {
        alert(`Você acertou ${acertou} perguntas e errou ${errou}.`);
        const recarregar = document.querySelector('#questao')
        const buttonReload = document.createElement('button')
        buttonReload.innerText = 'Refazer o quiz'
        recarregar.innerText = ''
        recarregar.appendChild(buttonReload)
        buttonReload.addEventListener('click',()=> location.reload())
    } 
    cancelaEscolha()
}

function cancelaEscolha(){
    const escolhasOptions = document.querySelector('.escolhasOptions')
    document.querySelector('#pergunta').innerText = ''
    escolhasOptions.innerHTML = ''
}

document.querySelector('#reload').addEventListener('click', ()=>{
    perguntaAleatoria()
    console.log(`Tu acertou ${acertou} questões.`);
    console.log(`Tu errou ${errou} questões.`);
    console.log(`Esta é a ${contarResposta}ª questão.`);
    
})
    
perguntaAleatoria()




