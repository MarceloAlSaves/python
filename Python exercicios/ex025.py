print("Custo da viagem")
distancia = float(input("Digite a distância da viagem (km): "))
if distancia <= 200:
    custo = distancia * 0.5
else:
    custo = distancia * 0.45
print(f"O custo da viagem é: R$ {custo:.2f}")