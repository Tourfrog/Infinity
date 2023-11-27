

const resultado = document.querySelector('#resultado')
const button = document.querySelector('#button')

function calcularIMC(){
    const altura = document.querySelector('#altura').value
    const peso = document.querySelector('#peso').value
    let imc = peso /(altura * altura)
    resultado.innerText = `O seu IMC é ${imc.toFixed(2)}.`
    console.log(imc, altura, peso);
}

button.addEventListener('click', ()=>{
    calcularIMC()
    
})