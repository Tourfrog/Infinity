
const titulo = prompt('Digite o titulo do livro: ')
const autor = prompt('Digite o nome do autor: ')
const num_Pagina = prompt(`Quantas paginas o ${titulo} tem: `)

list = [{
    'titulo': titulo,
    'autor' : autor,
    'Paginas' : num_Pagina
}]


function obj_Json(){
    console.log(`O livro ${titulo}, foi escritor por ${autor} e tem ${num_Pagina} páginas.`)
}
obj_Json()