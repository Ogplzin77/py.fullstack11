/////////////////////////////////// AULA 9- 21/03////////////////////////////////////////

//Soma de Matrizes: Crie duas matrizes 3x3 e escreva uma função para somá-las. 
//A função deve retornar uma nova matriz com o resultado.
// Definindo as duas matrizes 3x3

//Criamos duas matrizes 3x3, matriz1 e matriz2, contendo números inteiros.

let matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
];

// Função para somar as matrizes
function somarMatrizes(m1, m2) { //A função recebe duas matrizes como argumentos (m1 e m2).
    // Inicializando a matriz de resultado
    let resultado = []; //Inicializamos uma nova matriz chamada resultado para armazenar a soma.


    // Percorrendo as linhas
    for (let i = 0; i < 3; i++) {
        // Inicializando uma nova linha para o resultado
        resultado[i] = [];
        
        // Percorrendo as colunas
        for (let j = 0; j < 3; j++) {
            // Somando os elementos correspondentes e armazenando na nova matriz
            resultado[i][j] = m1[i][j] + m2[i][j]; //A cada iteração, somamos os elementos correspondentes das duas matrizes (m1[i][j] + m2[i][j]) e armazenamos o resultado em resultado[i][j].

        }
    }
    return resultado;
}

// Chamando a função e exibindo o resultado
let matrizSoma = somarMatrizes(matriz1, matriz2);
console.log("Resultado da soma das matrizes:");
console.table(matrizSoma); //A função console.table() é utilizada para exibir a matriz de forma tabular, facilitando a visualização do resultado.


// Transposição de Matriz: Escreva uma função que receba uma matriz 3x3 e retorne sua transposta (troque linhas por colunas).

// Multiplicação de Matrizes: Crie duas matrizes 2x2 e escreva uma função para multiplicá-las







// Jogo da Velha: Implemente um jogo da velha usando uma matriz 3x3.
// O programa deve permitir que dois jogadores façam jogadas alternadas e verifique se há um vencedor.






// Busca em Matriz: Escreva uma função que receba uma matriz e um número, e retorne a posição (linha e coluna) desse número na matriz.
// Se o número não estiver na matriz, retorne null.
 







// Matriz Identidade: Crie uma função que gere uma matriz identidade de tamanho NxN (uma matriz onde os elementos da diagonal principal são 1 e os demais são 0).









// Rotação de Matriz: Escreva uma função que rotacione uma matriz 3x3 em 90 graus no sentido horário.









// Soma das Bordas: Escreva uma função que calcule a soma dos elementos das bordas de uma matriz NxN.


