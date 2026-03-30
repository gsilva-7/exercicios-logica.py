mediaGlicose = float(input("Digite a média da glicose: "))

if mediaGlicose <= 0:
    print("Valor inválido")
elif mediaGlicose <= 100:
    print("Classificação: normal")
elif mediaGlicose <= 140:
    print("Classificação: elevado")
else:
    print("Classificação: diabetes")