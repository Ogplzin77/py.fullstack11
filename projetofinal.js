// Classe Disciplina (nome, código e  alunos Matriculados)
// Métodos: matricularAluno e gerarBoletim

class Disciplina {
    constructor(nome, codigo) {
        this.nome = nome;
        this.codigo = codigo;
        this.alunosMatriculados = {};
    }

    // Método para matricular um aluno à disciplina com nota inicial
    matricula(aluno, nota = 0) {
        this.alunosMatriculados[aluno] = nota;
        console.log(`Aluno ${aluno} matriculado na disciplina ${this.nome} com nota inicial ${nota}.`);
    }

    // Método para listar os alunos matriculados na disciplina
    listarAlunos() {
        const alunos = Object.keys(this.alunosMatriculados);
        if (alunos.length > 0) {
            console.log(`Alunos matriculados em ${this.nome}:`);
            alunos.forEach(aluno => console.log(`- ${aluno} (Nota: ${this.alunosMatriculados[aluno]})`));
        } else {
            console.log(`Nenhum aluno matriculado em ${this.nome}.`);
        }
    }

    // Método para gerar o boletim da disciplina
    gerarBoletim() {
        console.log(`Boletim da disciplina ${this.nome}:`);
        Object.entries(this.alunosMatriculados).forEach(([aluno, nota]) => {
            console.log(`${aluno}: Nota ${nota}`);
        });
    }
}