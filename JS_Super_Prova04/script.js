
//Calculo Fatorial: Para representar o fatorial de um número, escrevemos o número seguido de um ponto de exclamação,
//ou seja, n! (lê-se “n fatorial”). Por exemplo, o fatorial do número 5 é 5!, que é a multiplicação de 5 pelos seus antecessores, ou seja, 5⋅4⋅3⋅2⋅1.

// Sequencia Fibbonaci: os números de Fibonacci são uma sequência ou sucessão definida como recursiva pela fórmula:
//  F(n + 2) = F(n + 1) + F(n) , com n ≥ 1 e F(1) = F(2) = 1 . Os primeiros números de Fibonacci são:
//   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, ...


let number = parseInt(prompt('Digite um número inteiro: '))
let old_numberFatorial = number
let new_numberFibonacci = number
let old_numberFibonacci = new_numberFibonacci

for (i = 1; i <= number; i++){
    console.log(" -- Calculo Fatorial -- ");
    let new_numberFatorial = old_numberFatorial * i
    console.log(`${new_numberFatorial} = ${old_numberFatorial} * ${i}`);
    old_numberFatorial = new_numberFatorial

    // console.log(" -- Sequencia Fibonacci -- ");
    // let last_numberFibonacci = new_numberFibonacci + old_numberFibonacci
    // console.log(`${last_numberFibonacci} = ${new_numberFibonacci} + ${old_numberFibonacci}`);
    // old_numberFibonacci = new_numberFibonacci
    // new_numberFibonacci = last_numberFibonacci
    
}

console.log(" ");
console.log(" ");

for (i = 1; i <= number; i++){
    // console.log(" -- Calculo Fatorial -- ");
    // let new_numberFatorial = old_numberFatorial * i
    // console.log(`${new_numberFatorial} = ${old_numberFatorial} * ${i}`);
    // old_numberFatorial = new_numberFatorial

    console.log(" -- Sequencia Fibonacci -- ");
    let last_numberFibonacci = new_numberFibonacci + old_numberFibonacci
    console.log(`${last_numberFibonacci} = ${new_numberFibonacci} + ${old_numberFibonacci}`);
    old_numberFibonacci = new_numberFibonacci
    new_numberFibonacci = last_numberFibonacci
    
}
