import math
print("Catetos e Hipotenusa")
cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))
hipotenusa = math.hypot(cateto1, cateto2)
print("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))