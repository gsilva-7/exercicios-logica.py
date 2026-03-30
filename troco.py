unidadeProduto = float(input("Digite o valor unitário do produto (R$): "))
qtdComprada = int(input("Digite a quantidade comprada: "))
dinheiroRecebido = float(input("Digite o valor pago pelo cliente (R$): "))

totalCompra = unidadeProduto * qtdComprada
troco = dinheiroRecebido - totalCompra

if dinheiroRecebido < totalCompra:
    print("Valor recebido insuficiente.")
else:
    print("--------")
    print(f"Valor unitário: R${unidadeProduto:.2f}")
    print(f"Quantidade comprada: {qtdComprada}")
    print(f"Total da compra: R${totalCompra:.2f}")
    print(f"Dinheiro recebido: R${dinheiroRecebido:.2f}")
    print(f"Troco: R${troco:.2f}")
