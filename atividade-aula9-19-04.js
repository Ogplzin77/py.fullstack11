/////////////////// ATIVIDADE AULA 19/04//////////////////////////////

// 1: Crie uma função que recebe um array de números e retorna a soma de todos os elementos.
function somaarray (arr) { // A função somaArray(numeros) recebe um array de números como parâmetro. A função somaArray(numeros) recebe um array de números como parâmetro.
    return arr.reduce((acc, num)=> acc + num, 0); // todo .reduce() percorre o array e acumula os valores em uma única variável. (acumulador): variável onde a soma será armazenada. (numero): cada elemento do array sendo processado.
     // A função de callback acumulador + numero soma cada número ao acumulador.  O segundo argumento 0 indica que o acumulador começa com o valor 0.

    }

    let num = [142,2788,56,534,71,29]; //  Criamos um array.

    let= resultado =somaarray(num); // Passamos esse array para a função somaArray(num).

    console.log ("resultado"); // O método .reduce() soma todos os números. 

    
    
    //// 2: Crie uma função que recebe um array de strings e retorna um novo array com as strings em ordem alfabética.

    function ordenarStrings(array) { // A função ordenarStrings(array) recebe um array de strings como entrada.

        return array.slice().sort(); // O método .slice() cria uma cópia do array original antes da ordenação. Isso evita modificar o array original e mantém a imutabilidade dos dados.
        // O método .sort() organiza os elementos do array em ordem alfabética. Por padrão, .sort() classifica strings corretamente em ordem crescente (A → Z).


    }
    
    // Exemplo de uso:
    const palavras = ["processador", "ram", "placa", "memoria"]; //  criação do array 
    const palavrasOrdenadas = ordenarStrings(palavras); // Chamamos a função ordenarStrings(), que retorna um novo array ordenado.
 
    
    console.log(palavrasOrdenadas); // resultado impresso
    
    
    //// 3: Crie uma função que recebe um array e retorna um novo array sem elementos duplicados.

    function removerDuplicatas(array) {
        return [...new Set(array)]; 
        //  O Set é uma estrutura de dados que não permite valores duplicados. Como Set não retorna um array, usamos [...new Set(array)] para converter o Set de volta para um array.
        // Criamos um Set com os elementos do array: new Set(array), que remove automaticamente os valores repetidos.

    }
    
    // Exemplo de uso:
    const numeros = [1, 2, 3, 4, 2, 3, 5, 6, 1]; //  O array  contém números repetidos.

    const resultado = removerDuplicatas(numeros); // A função removerDuplicatas(numeros) retorna sem elementos duplicados.

    console.log(resultado);  // resultado final 
    // Saída: [1, 2, 3, 4, 5, 6]    