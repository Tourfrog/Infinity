

const telaDeBaixo = document.querySelector('#telaDeBaixo')
telaDeBaixo.innerHTML = ''
const menu = document.querySelector('#menu')

let saldoFinal = 1000.00

function verSaldo(){
    telaDeBaixo.innerHTML = ''
    telaDeBaixo.innerText = `Você tem na sua conta, o saldo de R$${saldoFinal} reais.`

}

function verDepositar(){
    try{ 

        telaDeBaixo.innerHTML = ''
        const depositarLabel = document.createElement('label')
        const depositarInput = document.createElement('input')
        const buttonDepositar = document.createElement('button')
    
        depositarLabel.innerText = 'O quanto você vai depositar:'
        depositarInput.type = "number"
        depositarInput.id = 'saldoExtra'
        buttonDepositar.type = "button"
        buttonDepositar.innerText = 'Realizar deposito'
        buttonDepositar.onclick = function fazerDeposito(){
            try{

                let deposito = parseFloat(depositarInput.value)
                saldoFinal = saldoFinal + deposito
        
                if (deposito < 0.009){
                    throw new Error('Você deve colocar pelo menos 0.01 centavo.')
                } else{
                    const confirmacao = document.createElement('p')
                    confirmacao.innerText = `Deposito de R$${deposito} bem sucedido.`
                    telaDeBaixo.appendChild(confirmacao)
                    alert('Deposito feito');
                }
            } catch (erro){
                console.error('Deu erro, porque => ', erro.message);
                alert(`Deu erro, porque => ${erro.message}`);
            }
        }

        telaDeBaixo.appendChild(depositarLabel)
        telaDeBaixo.appendChild(depositarInput)
        telaDeBaixo.appendChild(buttonDepositar)
        
    } catch (err){
        console.error('Deu erro para abrir o menu do deposito: ', err.message);
    }

    
}


function verRetirar(){
    try{

        telaDeBaixo.innerHTML = '' 
        const retirarLabel = document.createElement('label')
        const retirarInput = document.createElement('input')
        const buttonRetirar = document.createElement('button')
    
        retirarLabel.innerText = 'O quanto você quer retirar: '
        retirarInput.type = 'number'
        retirarInput.id = 'retirada'
        buttonRetirar.type = 'button'
        buttonRetirar.innerText = 'Realizar retirada'
        buttonRetirar.onclick = function fazerRetirada(){
            try{

                let retirada = parseFloat(retirarInput.value)
                
                if(retirada > saldoFinal){
                    throw new Error('Você não tem esse saldo para retirar.')
                } else{
                    const confirmacao = document.createElement('p')
                    confirmacao.innerText = `Retirada de R$${retirada} bem sucedido.`
                    telaDeBaixo.appendChild(confirmacao)
                    saldoFinal = saldoFinal - retirada
                    alert('Sacou dinheiro.')
                }
            } catch(erro){
                console.error('Deu erro, porque => ', erro.message);
                alert(`Deu erro, porque => ${erro.message}`);
            }
        }
    
        telaDeBaixo.appendChild(retirarLabel)
        telaDeBaixo.appendChild(retirarInput)
        telaDeBaixo.appendChild(buttonRetirar)

    } catch(err){
        console.error('Deu erro para abrir o menu da retirada: ', err.message);
    }
}


try{

    menu.addEventListener('click',(e) => {
        if (e.target.value === 'saldo'){
            verSaldo()
        } else if (e.target.value === 'depositar'){
            verDepositar()
        } else if (e.target.value === 'retirar'){
            verRetirar()
        }
    })


} catch (err){
    console.error('Ocorreu um erro: ', err.message);
}






