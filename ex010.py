print("Aluguel de carro")
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))
preco_dia = 60
preco_km = 0.15
total = (dias * preco_dia) + (km * preco_km)
print("O total a pagar pelo aluguel do carro é: R${:.2f}".format(total))
