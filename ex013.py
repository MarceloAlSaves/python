print("Sorteando uma pessoa da lista")
import random
n1 = input("Digite o nome da primeira pessoa: ")
n2 = input("Digite o nome da segunda pessoa: ")
n3 = input("Digite o nome da terceira pessoa: ")
lista = [n1, n2, n3]
sorteado = random.choice(lista)
print("A pessoa sorteada foi: {}".format(sorteado))