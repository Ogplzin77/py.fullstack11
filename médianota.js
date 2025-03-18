//Cálculo de Média de Notas: Peça ao usuário que insira 4 notas (de 0 a 10). 
//Calcule a média das notas e exiba o resultado. 
//Se a média for maior ou igual a 7, exiba "Aprovado". Caso contrário, exiba "Reprovado".

const readline = require ('readline')
const r1 = readline.createInterface ({
    input: process.stdin, 
    output: process.stdout
});

function calcularmedia(n1,n2,n3,n4) {
    let medianotas = n1 + n1 + n3 + n4 / 4;
    if (medianotas <=7){
        return "aprovado"
    } else if (medianotas<= 5 && medianotas <7) {
        return "recuperação" 
    } else {