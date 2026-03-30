salario = float(input("Digite o salário do camarada: "))


if salario <= 1000:
    aumento = salario * 20 / 100
    print(f"Novo salário: {salario + aumento:.2f}")
    print(f"Aumento: {aumento:.2f}")
    print(f"Porcentagem: 20%")
elif salario <= 3000:
    aumento = salario * 15 / 100
    print(f"Novo salário: {salario + aumento:.2f}")
    print(f"Aumento: {aumento:.2f}")
    print(f"Porcentagem: 15%")
elif salario <= 8000:
    aumento = salario * 10 / 100
    print(f"Novo salário: {salario + aumento:.2f}")
    print(f"Aumento: {aumento:.2f}")
    print(f"Porcentagem: 10%")
else:
    aumento = salario * 5 / 100
    print(f"Novo salário: {salario + aumento:.2f}")
    print(f"Aumento: {aumento}")
    print(f"Porcentagem: 5%")