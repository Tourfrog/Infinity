// Escreva um programa em JavaScript que solicite ao usuário o nome, altura em centímetros e peso de uma pessoa.
// O programa deve calcular o índice de massa corporal (IMC) dessa pessoa, considerando a fórmula IMC = peso / (altura * altura),
// onde a altura deve ser convertida de centímetros para metros. Em seguida, o programa deve classificar o peso com base no IMC calculado, 
// de acordo com a tabela a seguir:

// Menor que 16: Baixo peso muito grave
// De 16 a 16.99: Baixo peso grave
// De 17 a 18.49: Baixo peso
// De 18.50 a 24.99: Peso normal
// De 25 a 29.99: Sobrepeso
// De 30 a 34.99: Obesidade grau I
// De 35 a 39.99: Obesidade grau II
// Maior ou igual a 40: Obesidade grau III
// O programa deve exibir o nome da pessoa, o índice de massa corporal calculado e a classificação correspondente.


let nome = prompt('Digite o seu nome: ')
let peso = prompt('Digite o seu peso em kg: ')
let altura = prompt('Digite a sua altura em cm: ')

let nova_Altura = altura/100

let IMC = (peso/(nova_Altura * nova_Altura)).toFixed(2)

if (IMC < 16){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com Baixo peso muito grave!`);
} 
 else if (IMC < 17){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com Baixo peso grave!`);
} 
 else if (IMC < 18.50){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com Baixo peso!`);
}
 else if (IMC < 25){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com peso normal!`);
}
 else if (IMC < 30){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com sobrepeso!`);
}
 else if (IMC < 35){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com Obesidade grau I!`);
}
 else if (IMC < 40){
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com Obesidade grau II!`);
}
 else{
    console.log(`Olá ${nome}, o seu IMC é ${IMC} e você está com Obesidade grau III!`);
}

