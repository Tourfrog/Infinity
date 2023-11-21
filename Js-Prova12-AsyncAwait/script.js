// [JS-A12]Considere o seguinte cenário: você precisa criar uma aplicação em JavaScript que solicita ao usuário que informe um número e,
//  em seguida, realiza a verificação se este número é par ou ímpar. Caso seja par, a aplicação deve adicionar este número a um array.
//   Além disso, deve ser realizada a soma de todos os números pares que foram adicionados ao array.

// Utilizando os conceitos de Eventos: Addlistener, Click, Change; Funções; Arrays; Comandos de repetição;
//  Condicionais; Promises e carregamento ASSINC. FETCH; Tratamento de Erros - TRY CATCH; Funções Agregadoras;
//   e Objetos JSON, escreva um código que atenda aos requisitos acima.

const inputNumber = document.querySelector('#inputNumber')
const buttonNumber = document.querySelector('#buttonNumber')
const arrayNumber = document.querySelector('#arrayNumber')
const somaArray = document.querySelector('#somaArray')
const wrongNumber = document.querySelector('#wrongNumber')

const listNumber = []
const wrongList = []
let soma = 0


function par_ou_impar(){
    try{
        const number = parseInt(inputNumber.value)
        if(!isNaN(number)){
            if (number % 2 == 0){
                listNumber.push(number)
                arrayNumber.innerText = listNumber 
                console.log(typeof(number));
                let resultArray = listNumber.reduce((total , num) => total + num, 0)
                somaArray.innerText = resultArray
            } else{
                wrongList.push(number)
                wrongNumber.innerText = wrongList 
            }
        }else {
            alert('Coloque números!')
        }
    }catch(error){
        console.log("Deu erro," + error);
    }
}
buttonNumber.addEventListener('click', ()=>{
    par_ou_impar()
    
})