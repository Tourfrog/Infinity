// Em uma aplicação web, você precisa fazer uma requisição para uma API que retorna uma lista de usuários em formato JSON.
//  Utilize Promises e o método `fetch( )` para realizar a requisição e, em caso de sucesso,
//   exibir o nome de cada usuário em uma lista não ordenada (ul) na página HTML.
//    Caso ocorra algum erro na requisição, exiba uma mensagem de erro na página.


const dogList = document.querySelector('#dogList')
const erroMessage = document.querySelector('#errorMessage')

// Pegando todas as raças
function getDogBreeds(){
    fetch('https://dog.ceo/api/breeds/list/all')
    .then(response => {
        if(!response.ok){
            throw new Error('Erro ao carregar lista')
        }
        return response.json()
    })
    .then(breeds =>{
        const breedsDog = breeds.message;
        console.log('Raças de cachorro disponíveis:')
        console.log(breedsDog);
        dogList.innerHTML = ''

        for(const breed in breedsDog){
            const li = document.createElement('li')
            li.textContent = breed
            dogList.appendChild(li)
        }       
    })
    .catch(error =>{
        erroMessage.textContent = error.message
    })
}


getDogBreeds()
