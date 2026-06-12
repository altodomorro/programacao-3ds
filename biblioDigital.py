class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de páginas: {self.paginas}"


# Programa principal
def main():
    print("Cadastro de Livro na Biblioteca Digital")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    paginas = input("Digite o número de páginas: ")

    livro = Livro(titulo, autor, paginas)

    print("\nDescrição do livro cadastrado:")
    print(livro)


if __name__ == "__main__":
    main()
