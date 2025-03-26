/////////////////////////////////////// PROJETO FINAL////////////////////////////////////////
///////////////////////////////////// Classe Professor (nome, departamento, disciplinas) Métodos: ////////////////////////////////////// 

// Declarar as classes 
class Professor {
    constructor(nome, departamento) { // O construtor da classe recebe dois parâmetros: 'nome' e 'departamento'.
        this.nome = nome; //atribui o nome do professor 
        this.departamento = departamento; // atribui o departamento do professor 
        this.disciplinas = []; // inicia um array vazio para a diciplina    
        this.turmas = []; // inicia um array vazio para as turmas
    }

    // Atribuir uma disciplina
    atribuirDisciplina(disciplina) { // verifica se a diciplina está atribuiada ao professor 
        if (!this.disciplinas.includes(disciplina)) { 
            this.disciplinas.push(disciplina);  //adicione a diciplina ao array 
            console.log(`Disciplina ${disciplina} atribuída ao professor ${this.nome}.`); // Caso a disciplina já tenha sido atribuída, exibe uma mensagem de aviso

        } else {
            console.log(`Professor ${this.nome} já ministra a disciplina ${disciplina}.`); //caso a diciplina não tenha sido atribuida, exiba uma mensagem  
        }
    }

    // Listar as disciplinas atribuídas
    listarDisciplina() { //verifica se o professor tem alguma diciplina atribuida 
        if (this.disciplinas.length > 0) {
            console.log(`O professor ${this.nome} ministra as seguintes disciplinas:`); //para cada diciplina atribuida, insira seu nome 
            this.disciplinas.forEach(disciplina => console.log(`- ${disciplina}`));
        } else {
            console.log(`Professor ${this.nome} ainda não tem disciplinas atribuídas.`); // se não tiver diciplina atribuida, exiba uma mensagem
        }
    }

    // Listar as turmas atribuídas
    listarTurmas() { // verifica se a turma foi atribuida ao professor 
        if (this.turmas.length === 0) {
            console.log(`${this.nome} ainda não tem turmas atribuídas.`);  // se não haver turmas, exiba uma mensagem de aviso
        } else {
            console.log(`Turmas atribuídas ao professor ${this.nome}:`); // caso tenha turmas, exiba uma mensagem de aviso  
            this.turmas.forEach((turma, index) => {
                console.log(`${index + 1}. ${turma}`); 
            });
        }
    }

    // Método para atribuir turma 
    atribuirTurma(turma) {  // verifica se a turma foi atribuida ao professor 
        if (!this.turmas.includes(turma)) {
            this.turmas.push(turma);
            console.log(`Turma ${turma} atribuída ao professor ${this.nome}.`);  // adicionar um array de turmas
        } else {
            console.log(`Professor ${this.nome} já tem a turma ${turma} atribuída.`); // caso tenha sido atribuida, exiba uma mensagem de texto 
        }
    }
}
        
const professor1 = new Professor("Carlos Silva", "Matemática");
const professor2 = new Professor("joão","fisica");

// Atribuindo disciplinas
professor1.atribuirDisciplina("Ciências"); // atribuia a diciplina ''ciencias''
professor1.atribuirDisciplina("Matemática"); // atribua a diciplina ''matematica''
professor2.atribuirDisciplina("ed fisica"); // atribua a diciplina ''ed fisica''
professor2.atribuirDisciplina("fisica"); // atribua a diciplina '' fisica''

// Atribuindo turmas
professor1.atribuirTurma("Turma A - 2009"); // atribua a ''turma A - 2009''
professor1.atribuirTurma("Turma B - 2010"); // atribua a ''turma B - 2010''
professor2.atribuirTurma("turma c - 2011"); // atribua a ''turma c - 2011''
professor2.atribuirTurma("turma d - 2012"); // atribua a ''turma d - 2012''
// Listando disciplinas e turmas
professor1.listarDisciplina();  //exiba a lista de diciplina ao professor 1 
professor1.listarTurmas(); //exiba as turmas do professor 1
professor2.listarDisciplina(); // exiba a lista de diciplina ao professor 2
professor2.listarTurmas(); //exiba as turmas do professor 2
