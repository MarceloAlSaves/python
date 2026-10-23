print("Radar eletrônico")
velocidade = float(input("Digite a velocidade do carro (km/h): "))
if velocidade > 80:
    print("Você foi multado! A velocidade máxima permitida é de 80 km/h.")
    multa = (velocidade - 80) * 7
    print(f"O valor da multa é: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Tenha um bom dia!")