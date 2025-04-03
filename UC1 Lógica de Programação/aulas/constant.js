const readline = require('readline');   // O readline é um módulo do Node.js usado para capturar entrada do usuário pelo terminal.


const rl = readline.createInterface({ // Cria um interface de leitura (rl) que permite interagir com o usuário via terminal.

    input: process.stdin,
    output: process.stdout
});

function notas(nota1, nota2, nota3, nota4) { //
    let medianotas = (nota1 + nota2 + nota3 + nota4) / 4;

    if (medianotas >= 7) {
        return "Aprovado"; // se a média for maior que 7
    } else if (medianotas >= 5 && medianotas < 7) {
        return "Recuperação"; // se a média for menor que 7
    } else {
        return "Reprovado"; // se a média for menor que 5
    }
}

rl.question("Digite a primeira nota:", (nota1) => { // 
    rl.question("Digite a segunda nota:", (nota2) => //
        rl.question("Digite a terceira nota:", (nota3) => { //
            rl.question("Digite a quarta nota:", (nota4) => { // 
                nota1 = parseFloat(nota1); //  Depois de receber todas as notas, ele as converte de string para número (parseFloat):                
                nota2 = parseFloat(nota2);
                nota3 = parseFloat(nota3);
                nota4 = parseFloat(nota4);

                let resultado = notas(nota1, nota2, nota3, nota4); // 
                console.log("Classificação das notas: ", resultado); // 

                rl.close(); // o programa fecha a interface (rl.close()) para encerrar a interação com o terminal.
            });
        
                }   
