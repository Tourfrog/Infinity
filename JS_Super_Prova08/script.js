
const medidas = document.querySelector('#escolhas')

let valor = 0

medidas.addEventListener('click', (e)=>{

    if(e.target.value === 'Jarda') {
        valor = 1.09361
    } else if(e.target.value === 'Pé'){
        valor = 3.28084
    } else if(e.target.value === 'Polegada'){
        valor = 39.3701
    } else if(e.target.value === 'Milhas'){
        valor = 0.000621371
    } else if(e.target.value === '#'){
        valor = 0
    }

    console.log(e.target.value);
})


function converter(){
    const inputConverter = parseInt(document.querySelector('#inputConverter').value)

    const resultado = document.querySelector('#resultado')

    
    distancia = inputConverter * valor
    // console.log(distancia);

    if(distancia === 0){
        alert('Escolha uma das opções de medida a converter.')
        resultado.innerText = ''
    }
    if (valor === 1.09361){
        resultado.innerText = `A distancia convertida de ${inputConverter}m para jarda é: ${distancia}yd. `
    }
    if (valor === 3.28084){
        resultado.innerText = `A distancia convertida de ${inputConverter}m para pé é: ${distancia}ft. `
    }
    if (valor === 39.3701){
        resultado.innerText = `A distancia convertida de ${inputConverter}m para polegada é: ${distancia}in. `
    }
    if (valor === 0.000621371){
        resultado.innerText = `A distancia convertida de ${inputConverter}m para milhas é: ${distancia}mi. `
    }
    
        
        
}

const buttonConverter = document.querySelector('#buttonConverter')
buttonConverter.addEventListener('click',()=>{
    converter()
})

