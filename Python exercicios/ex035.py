print("Analisando triângulos")
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triângulo.")
    if a == b == c:
        print("O triângulo é EQUILÁTERO.")
    elif a != b != c != a:
        print("O triângulo é ESCALENO.")
    else:
        print("O triângulo é ISÓSCELES.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")