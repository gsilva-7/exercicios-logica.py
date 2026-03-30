import math

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base**2 + altura**2)

print("------------")

print(f"Base do retângulo: {base:.1f}")
print(f"Altura do retângulo: {altura:.1f}")
print(f"Área do retângulo: {area:.4f}")
print(f"Perímetro do retângulo: {perimetro:.4f}")
print(f"Diagonal do retângulo: {diagonal:.4f}")