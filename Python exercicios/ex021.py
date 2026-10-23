print("Analizando de textos")
print("Me diga seu nome completo:")
nome_completo = input("nome completo: ")
print(f"Seu nome completo é: {nome_completo}")
print(f"Seu nome em maiúsculas: {nome_completo.upper()}")
print(f"Seu nome em minúsculas: {nome_completo.lower()}")
print(f"Seu nome tem ao todo {len(nome_completo) - nome_completo.count
(' ')} letras")
print(f"Seu primeiro nome é {nome_completo.split()[0]} e ele tem {len(nome_completo.split()[0])} letras")