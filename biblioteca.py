# Lista de recomendações da Gemini
livros = [
    "1 - Neuromancer (William Gibson)", 
    "2 - Sapiens: Uma Breve História da Humanidade (Yuval Noah Harari)",
    "3 - Eu, Robô (Isaac Asimov)",
    "4 - O Guia do Mochileiro das Galáxias (Douglas Adams)",
    "5 - Código Limpo: Habilidades Práticas do Agile Software (Robert C. Martin)",
    "6 - Duna (Frank Herbert)",
    "7 - 1984 (George Orwell)",
    "8 - O Algoritmo de Mestre (Pedro Domingos)",
    "9 - Fundação (Isaac Asimov)",
    "10 - O Androide Sonha com Ovelhas Elétricas? (Philip K. Dick)"
]

while True:

    print("1 - Livros disponíveis.")
    print("2 - Emprestar livro.")
    print("3 - Devolver livro.")
    print("4 - Livros emprestados.")
    print("5 - Sair.")

    opcao = int(input("Selecione a opçao desejada (1-5): "))

    if opcao == 5:
        print("Saindo, até mais!!!")
        break

    if opcao == 1:
            for livro in livros:
                print("LIVROS DISPONÍVEIS")
                print(livro)
                print("-----------------")

    if opcao == 2:
            emprestar = int(input("Digite o código do livro que deseja emprestar: "))