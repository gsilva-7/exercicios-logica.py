quantidadeComprada = int(input("Digite a quantidade comprada: "))
codigo = int(input("Digite o código do produto: "))

match codigo:
    case 1:
        print(f"Código do produto: {codigo}")
        print(f"Quantidade comprada: {quantidadeComprada}")
        print(f"Valor a pagar: {quantidadeComprada * 5.00}")
    case 2:
        print(f"Código do produto: {codigo}")
        print(f"Quantidade comprada: {quantidadeComprada}")
        print(f"Valor a pagar: {quantidadeComprada * 3.50}")
    case 3:
        print(f"Código do produto: {codigo}")
        print(f"Quantidade comprada: {quantidadeComprada}")
        print(f"Valor a pagar: {quantidadeComprada * 4.80}")
    case 4:
        print(f"Código do produto: {codigo}")
        print(f"Quantidade comprada: {quantidadeComprada}")
        print(f"Valor a pagar: {quantidadeComprada * 8.90}")
    case 5:
        print(f"Código do produto: {codigo}")
        print(f"Quantidade comprada: {quantidadeComprada}")
        print(f"Valor a pagar: {quantidadeComprada * 7.32}")

# precos = [5.00, 3.50, 4.80, 8.90, 7.32]

# codigo = int(input("Digite o codigo do produto: "))

# qtd = int(input("Digite a quantidade comprada: "))

# pagar = 0

# if 1 <= codigo <= 5:
#     pagar = qtd * precos[codigo - 1]
#     print(f"Valor a pagar: {pagar:.2f}")
# else:
#     print("Código inválido!")