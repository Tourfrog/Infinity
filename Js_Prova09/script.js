

let iventario = [  

    { nome: "Camisa", preco: 50.0 },

    { nome: "Calça", preco: 80.0 },

    { nome: "Jaqueta", preco: 150.0 },

    { nome: "Meia", preco: 10.0 }

]

//Escreva uma função em JavaScript que calcule o preço total dos produtos desse array utilizando uma das funções agregadoras aprendidas em sala de aula.
//A função deve se chamar calcularTotal e receber o array como parâmetro. O resultado deve ser retornado com duas casas decimais.

function calcularTotal(iventario){
    const total = iventario.reduce((soma, item)=>{
        return soma + item.preco
    },0)
    return total.toFixed(2)
}

const preco_Total = calcularTotal(iventario)

console.log(preco_Total)


