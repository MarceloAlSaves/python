print("aumentos multiplos")
salario = float(input("Digite o salário do funcionário: "))
if salario <= 1250:
    aumento = salario * 0.15
else:   
    aumento = salario * 0.10
novo_salario = salario + aumento
print(f"O salário atual é: R$ {salario:.2f}")
print(f"O aumento aplicado foi de: R$ {aumento:.2f}")
print(f"O novo salário é: R$ {novo_salario:.2f}")