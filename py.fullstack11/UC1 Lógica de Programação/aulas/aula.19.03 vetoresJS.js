///////    VETORES/ ARRAYS EM JAVASCRIPT- AULA 9 /////////

//arrays em javascript são estruturas de dados que permitem armazenar múltiplos
//exemplo lista;
let = frutas [ "Maçã , Banana", "Laranja"]; //O código cria um array chamado frutas que contém três elementos: "Maçã", "Banana" e "Laranja".
//O console.log(frutas) exibe esse array no console.
console.log (frutas);

//funções/ comandos de array:

//push: adiciona um ou mais elementos ao final do array:
frutas.push("Laranja"); // O método push() adiciona elementos no final de um array e modifica o array original.
//O console.log() exibe o array após a modificação, permitindo ver o novo conteúdo do array.
console.log(frutas);

// cont: em javascript, não temos uma função cont diretamente

console.log(frutas.length);

//copy: para copiar um array, podemos usar o método

let copiaFrutas = frutas.slice (); // O método slice() é utilizado para extrair uma cópia superficial de uma parte de um array. Quando chamado sem argumentos (como no caso frutas.slice()), ele cria uma cópia rasa de todo o array frutas.
console.log (copiaFrutas);

//random: para selecionar um elemento aleatório de yn array

let randomIndex = Math.floor(Math.random() * frutas.length); //randomIndex será um número inteiro aleatório entre 0 e frutas.length - 1, que são os índices válidos para acessar elementos no array frutas.
console.log (frutas [randomIndex]);

//range: JavaScript não tem uma função range nativa, 
//complexity
function range (start, end) {
    return array.from({length: end - start +1 },( ,i ) => i start + i); 
}
console.log(range(1,5)); 

//asort: javascript, podemos usar sort () para
let num = [3, 1, 4, 1, 5, 9];
num.sort((a,b) => a - b);
console.log (num);

//demonstração

let numeros = [5, 3, 8, 1, 9]

//ordenar o array

numeros.sort ((a,b) => a - b);
console.log ( numeros);

//adicionar um novo número
numeros.push (7);
console.log ("após o push:" , numeros);

//selecionar um número aleatório 
let randomNum = numeros[Math.floor(Math.random() * numeros.length)];
console.log("Número aleatório:", randomNum);

// Contar o número de elementos
console.log("Número de elementos:", numeros.length);


// Chamada da função
calcularJurosSimples();
