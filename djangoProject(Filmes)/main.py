class Filme:
    def __init__(self, titulo, ano, diretor, genero, duracao):
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao

    def __repr__(self):
        return f"{self.titulo} ({self.ano}) - {self.diretor}, {self.genero}, {self.duracao} min"


class CatalogoFilmes:
    def __init__(self):
        self.filmes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def listar_filmes(self):
        return self.filmes

    def listar_filmes_por_ano(self):
        return sorted(self.filmes, key=lambda x: x.ano)

    def listar_filmes_por_genero(self):
        return sorted(self.filmes, key=lambda x: x.genero)

    def listar_filmes_por_diretor(self):
        return sorted(self.filmes, key=lambda x: x.diretor)


def cadastrar_filme():
    titulo = input("Digite o título do filme: ")
    ano = int(input("Digite o ano de lançamento: "))
    diretor = input("Digite o nome do diretor: ")
    genero = input("Digite o gênero do filme: ")
    duracao = int(input("Digite a duração do filme em minutos: "))

    return Filme(titulo, ano, diretor, genero, duracao)


def main():
    catalogo = CatalogoFilmes()

    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar filme")
        print("2. Listar filmes")
        print("3. Listar filmes por ano")
        print("4. Listar filmes por gênero")
        print("5. Listar filmes por diretor")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            filme = cadastrar_filme()
            catalogo.adicionar_filme(filme)
        elif escolha == '2':
            filmes = catalogo.listar_filmes()
            if not filmes:
                print("Nenhum filme cadastrado.")
            else:
                for filme in filmes:
                    print(filme)
        elif escolha == '3':
            filmes = catalogo.listar_filmes_por_ano()
            if not filmes:
                print("Nenhum filme cadastrado.")
            else:
                for filme in filmes:
                    print(filme)
        elif escolha == '4':
            filmes = catalogo.listar_filmes_por_genero()
            if not filmes:
                print("Nenhum filme cadastrado.")
            else:
                for filme in filmes:
                    print(filme)
        elif escolha == '5':
            filmes = catalogo.listar_filmes_por_diretor()
            if not filmes:
                print("Nenhum filme cadastrado.")
            else:
                for filme in filmes:
                    print(filme)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
