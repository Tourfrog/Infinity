
// [JS-A10]Crie uma função em JavaScript que divida um número por zero.
//  Utilize o bloco de código try/catch para capturar o erro
//   e exibir uma mensagem personalizada de erro para o usuário.


try{
    let num1 = parseInt(prompt('Digite um numero qualquer: '));
    let num2 = parseInt(prompt(`Digite outro numero para dividir o ${num1}: `))
    
    if(num2 !== 0){
        let divisão = num1 / num2
        console.log(divisão)
    } else{
        throw new Error ('Impossivel dividir por zero.')
    }
} catch (e){
    console.log(`Alguma coisa deu errado: ${e.message}`);
}