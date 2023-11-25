// Criar um programa, onde deve solicitar o numero total de alunos,
// depois deve pedir as notas de cada aluno. Apos receber todas as notas,
// o programa deve calcular a media da turma e identificar tanto a maior e 
// menor nota obtida.

let aluno = 0
let total_De_Alunos = parseInt(prompt('Digite quantos alunos fez a prova: '))
let soma_Das_Notas = 0

while (aluno < total_De_Alunos){
    let nota = parseFloat(prompt('Digite a nota do aluno: '))
    if (nota < 0 || nota > 10){
        alert('Digite as notas verdadeiras, maior que 0 e menor que 10.')
        console.log('Programa Cancelado');
        break
    } else{
        soma_Das_Notas = soma_Das_Notas + nota
        aluno ++
    }
    
}

let media = soma_Das_Notas/total_De_Alunos
console.log(media);