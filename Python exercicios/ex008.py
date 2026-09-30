print("Pintando parede")
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
tinta = area / 2
print("A área da parede é de {} metros quadrados e será necessário {} litros de tinta para pintá-la".format(area, tinta))