/////////////////// ATIVIDADE AULA 19/04//////////////////////////////

// 1: Crie uma função que recebe um array de números e retorna a soma de todos os elementos.
function somaarray (arr) {
return arr.reduce((acc, num)=> acc + num, 0);

}
let num = [1,2,4,5,7,9];
let resultado =somaarray(num);
console.log ("resultado"); 








//// 2: Crie uma função que recebe um array de strings e retorna um novo array com as strings em ordem alfabética.







//// 3: Crie uma função que recebe um array e retorna um novo array sem elementos duplicados.