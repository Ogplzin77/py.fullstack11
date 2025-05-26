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

function transporMatriz(matriz) { // Inicializa uma matriz vazia matrizTransposta de tamanho 3x3
    let matrizTransposta = [];

    for (let i = 0; i < 3; i++) { 
        let linha = [];
        for (let j = 0; j < 3; j++) {
            linha.push(matriz[j][i]); // Inverte os índices (i, j) -> (j, i)
        }
        matrizTransposta.push(linha);
    }

    return matrizTransposta;
}

// Definição da matriz 3x3
let matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

// Chamando a função e imprimindo o resultado
let resultado1 = transporMatriz(matriz);
console.log("Matriz Transposta:", resultado);


// Multiplicação de Matrizes: Crie duas matrizes 2x2 e escreva uma função para multiplicá-las

function multiplicaMatrizes(matriz1, matriz2) {
    let matrizResultado = [[0, 0], [0, 0]]; // Inicializa a matriz 2x2 vazia

    for (let i = 0; i < 2; i++) { // Percorre as linhas de A
        for (let j = 0; j < 2; j++) { // Percorre as colunas de B
            matrizResultado[i][j] = 0; // Inicializa o valor da célula
            for (let k = 0; k < 2; k++) { // Multiplica os elementos e soma (Aqui, a variável 'K' serve para multiplicar os elementos corretos)


                matrizResultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
    }

    return matrizResultado;
}

// Definição das matrizes 2x2
let matrizA = [
    [1, 2],
    [3, 4]
];

let matrizB = [
    [5, 6],
    [7, 8]
];

// Chamando a função e imprimindo o resultado
let resultado = multiplicaMatrizes(matrizA, matrizB);
console.log("Matriz Resultado:", resultado);


// Jogo da Velha: Implemente um jogo da velha usando uma matriz 3x3.
// O programa deve permitir que dois jogadores façam jogadas alternadas e verifique se há um vencedor.

// Criando um tabuleiro 3x3 vazio
let tabuleiro = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
];

let jogadorAtual = "X"; // O jogador "X" começa

// Função para exibir o tabuleiro no console
function mostrarTabuleiro() {
    console.log("\n");
    tabuleiro.forEach(linha => console.log(linha.join(" | ")));
    console.log("\n");
}

// Função para verificar se há um vencedor
function verificarVencedor() {
    // Verifica linhas e colunas
    for (let i = 0; i < 3; i++) {
        if (tabuleiro[i][0] && tabuleiro[i][0] === tabuleiro[i][1] && tabuleiro[i][1] === tabuleiro[i][2]) {
            return tabuleiro[i][0]; // Vencedor por linha
        }
        if (tabuleiro[0][i] && tabuleiro[0][i] === tabuleiro[1][i] && tabuleiro[1][i] === tabuleiro[2][i]) {
            return tabuleiro[0][i]; // Vencedor por coluna
        }
    }

    // Verifica diagonais
    if (tabuleiro[0][0] && tabuleiro[0][0] === tabuleiro[1][1] && tabuleiro[1][1] === tabuleiro[2][2]) {
        return tabuleiro[0][0]; // Diagonal principal
    }
    if (tabuleiro[0][2] && tabuleiro[0][2] === tabuleiro[1][1] && tabuleiro[1][1] === tabuleiro[2][0]) {
        return tabuleiro[0][2]; // Diagonal secundária
    }

    return null; // Nenhum vencedor ainda
}

// Função para verificar empate
function verificarEmpate() {
    return tabuleiro.flat().every(celula => celula !== ""); // Verifica se todas as posições estão preenchidas
}

// Função para realizar uma jogada
function jogar(linha, coluna) {
    if (tabuleiro[linha][coluna] !== "") {
        console.log(" Posição já ocupada! Escolha outra.");
        return false;
    }

    // Marca a jogada no tabuleiro
    tabuleiro[linha][coluna] = jogadorAtual;
    mostrarTabuleiro();

    // Verifica se houve um vencedor
    let vencedor = verificarVencedor();
    if (vencedor) {
        console.log(`Jogador ${vencedor} venceu!`);
        return true;
    }

    // Verifica se houve empate
    if (verificarEmpate()) {
        console.log("O jogo terminou em empate!");
        return true;
    }

    // Alterna para o próximo jogador
    jogadorAtual = jogadorAtual === "X" ? "O" : "X";
    return false;
}


// Busca em Matriz: Escreva uma função que receba uma matriz e um número, e retorne a posição (linha e coluna) desse número na matriz.
// Se o número não estiver na matriz, retorne null.

function buscarNumero(matriz, numero) {
    for (let i = 0; i < matriz.length; i++) {
        for (let j = 0; j < matriz[i].length; j++) {
            if (matriz[i][j] === numero) {
                return [i, j]; // Retorna a posição do número encontrado
            }
        }
    }
    return null; // Retorna null se o número não estiver na matriz
}

// Exemplo de matriz 3x3
const matrizExemplo2 = [
    [1, 2, 12],
    [4, 7, 8],
    [9, 6, 4]
];

// Testando a busca
console.log(buscarNumero(matrizExemplo, 7));  // Saída: [1, 1] (Linha 1, Coluna 1)
console.log(buscarNumero(matrizExemplo, 4));  // Saída: [2, 2] (Linha 2, Coluna 2)
console.log(buscarNumero(matrizExemplo, 10)); // Saída: null (Não encontrado)


// Matriz Identidade: Crie uma função que gere uma matriz identidade de tamanho NxN (uma matriz onde os elementos da diagonal principal são 1 e os demais são 0).

function gerarMatrizIdentidade(n) {
    // Criamos uma matriz vazia de tamanho N x N
    let matriz = [];

    for (let i = 0; i < n; i++) {
        let linha = []; // Criamos uma nova linha

        for (let j = 0; j < n; j++) {
            // Se i == j, estamos na diagonal principal -> adicionamos 1
            if (i === j) {
                linha.push(1);
            } else {
                linha.push(0); // Caso contrário, adicionamos 0
            }
        }

        matriz.push(linha); // Adicionamos a linha na matriz
    }

    return matriz;
}

// Testando a função
console.log(gerarMatrizIdentidade(3));
console.log(gerarMatrizIdentidade(5));


// Rotação de Matriz: Escreva uma função que rotacione uma matriz 3x3 em 90 graus no sentido horário.

function rotacionarMatriz90(matriz) {
    let n = matriz.length;
    let matrizRotacionada = [];

    // Criar matriz vazia de mesmo tamanho
    for (let i = 0; i < n; i++) {
        matrizRotacionada.push([]);
    }

    // Preenchendo a nova matriz rotacionada
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            matrizRotacionada[j][n - 1 - i] = matriz[i][j];
        }
    }

    return matrizRotacionada;
}

// Exemplo de Matriz 3x3
let matrizExemploo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log(rotacionarMatriz90(matrizExemplo));


// Soma das Bordas: Escreva uma função que calcule a soma dos elementos das bordas de uma matriz NxN.

function somaDasBordas(matriz) {
    let n = matriz.length;
    let soma = 0;

    // Somando a primeira e última linha
    for (let j = 0; j < n; j++) {
        soma += matriz[0][j];    // Primeira linha
        if (n > 1) soma += matriz[n - 1][j]; // Última linha (evita duplicar se N = 1)
    }

    // Somando a primeira e última coluna (sem contar os cantos já somados)
    for (let i = 1; i < n - 1; i++) {
        soma += matriz[i][0];    // Primeira coluna
        soma += matriz[i][n - 1]; // Última coluna
    }

    return soma;
}

// Testando com uma matriz 3x3
const matrizExemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

console.log(somaDasBordas(matrizExemplo)); // Saída: 40

