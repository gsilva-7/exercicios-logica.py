larguraTerreno = int(input("Digite a largura do terreno: "))
compTerreno = int(input("Digite o comprimento do terreno: "))
valorMetroQuadrado = int(input("Digite o valor do metro quadrado (R$): "))

areaTerreno = larguraTerreno * compTerreno
precoTerreno = valorMetroQuadrado * areaTerreno

print("--------------------------------------------------")

print(f"Largura do terreno: {larguraTerreno:.1f}")
print(f"Comprimento do terreno: {compTerreno:.1f}")
print(f"Valor m²: R${valorMetroQuadrado:.2f}")
print(f"Área do terreno: {areaTerreno:.2f}")
print(f"Preço do terreno: R${precoTerreno:.2f}")