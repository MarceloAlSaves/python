
import random
print("Jogo de adivinhação v1")
print("Me diga um número entre 0 e 10:")
numero = int(input("número: "))
numero_aleatorio = random.randint(0, 10)
if numero == numero_aleatorio:
    print("Parabéns! Você acertou o número aleatório que era: {}".format(numero_aleatorio))
else:
    print("Você errou! O número aleatório era: {}".format(numero_aleatorio))
    print("tente novamente!")
