# 3. Padrão de Acesso a Repositórios

# Crie uma classe UsuarioRepository com os seguintes métodos:
'''
- cadastrar(usuario): cadastra um usuário (dicionário com nome e email).
- listar_todos(): retorna uma lista com todos os usuários cadastrados.
- buscar_por_email(email): retorna o usuário correspondente ao email informado.
- remover(email): remove o usuário correspondente ao email informado. 
- atualizar(usuario): atualiza os dados do usuário correspondente ao email informado.
- listar_por_nome(nome): retorna uma lista com todos os usuários que possuem o nome informado.
- listar_por_email(email): retorna uma lista com todos os usuários que possuem o email informado.
- listar_por_nome_e_email(nome, email): retorna uma lista com todos os usuários que possuem o nome e email informados.
'''

class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        if self.buscar_email(usuario["email"]) is None:
            self.usuarios.append(usuario)
            # print("Usuário cadastrado com sucesso.")
        else:
            # print("Email já cadastrado.")
            pass

    def listar_todos(self):
        return self.usuarios

    def buscar_email(self, email):
        for usuario in self.usuarios:
            if usuario['email'] == email:
                return usuario
        return None

    def remover(self, email):
        usuario = self.buscar_email(email)
        if usuario:
            self.usuarios.remove(usuario)
            return True
        return False

    def atualizar(self, usuario_atualizado):
        for i, usuario in enumerate(self.usuarios):
            if usuario['email'] == usuario_atualizado['email']:
                self.usuarios[i] = usuario_atualizado
                return True
        return False

    def listar_por_nome(self, nome):
        return [usuario for usuario in self.usuarios if usuario['nome'] == nome]

    def listar_por_email(self, email):
        return [usuario for usuario in self.usuarios if usuario['email'] == email]

    def listar_por_nome_e_email(self, nome, email):
        return [usuario for usuario in self.usuarios if usuario['nome'] == nome and usuario['email'] == email]

if __name__ == "__main__":
    repo = UsuarioRepository()
    repo.cadastrar({"nome": "Pabllo", "email": "Pabllo@exemplo.com"})
    repo.cadastrar({"nome": "Sophia", "email": "Sophia@exemplo.com"})
    repo.cadastrar({"nome": "Pedro", "email": "pedro@exemplo.com"})
    repo.cadastrar({"nome": "Maria", "email": "Maria@exemplo.com"})
    

    print("\nTodos os usuários:", repo.listar_todos())
    print("Buscar Pabllo:", repo.buscar_email("Pabllo@exemplo.com"))
    print("Atualizar Pabllo → Ana:", repo.atualizar({"nome": "Ana", "email": "Pabllo@exemplo.com"}))
    print("Remover Pabllo:", repo.remover("Pabllo@exemplo.com")) 
    print("Listar por nome (Pabllo):", repo.listar_por_nome("Pabllo"))
    print("Listar por nome (Sophia):", repo.listar_por_nome("Sophia"))
    print("Listar por email (Pabllo@exemplo.com):", repo.listar_por_email("Pabllo@exemplo.com"))
    print("Listar por nome e email (Pabllo + Pabllo@exemplo.com):", repo.listar_por_nome_e_email("Pabllo", "Pabllo@exemplo.com"))
