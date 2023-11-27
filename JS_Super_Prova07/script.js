// Imagine que você está criando uma solução digital para restaurantes,
//  incluindo uma calculadora de gorjetas de fácil uso.
//   O objetivo é desenvolver uma página da web onde os clientes possam
// inserir o valor total da conta e escolher a qualidade do serviço:
//  "Bom", "Regular" ou "Ruim". Para isso, serão utilizadas arrow functions e funções de callback.

const resposta = document.querySelector('#resposta')

function boaGorjetas(){
    const dinheiro = document.querySelector('#valorTotal').value
    goodTip = dinheiro * 0.2
    resposta.innerText = `Foi um praser cervir-lo, vou pagar bem o garxom: ${goodTip} reias.` 
}

function mediaGorjetas(){
    const dinheiro = document.querySelector('#valorTotal').value
    mediaTip = dinheiro * 0.1
    resposta.innerText = `Obrigado pro reponder, o garxon vai recebé: ${mediaTip} reiais.`
}

function ruimGorjetas(){
    const dinheiro = document.querySelector('#valorTotal').value
    ruimTip = dinheiro * 0.3
    resposta.innerText = `Desculpe pelo péssimo atendimento, Sr(a).
    Retiraremos R$${ruimTip} reais do garçom e retornaremos a vós, 
    como pedido de perdão da nossa parte.`
}

const bom = document.querySelector('#bom')
bom.addEventListener('click', boaGorjetas)

const media = document.querySelector('#medio')
media.addEventListener('click', mediaGorjetas)

const ruim = document.querySelector('#ruim')
ruim.addEventListener('click', ()=>{
    ruimGorjetas()
})