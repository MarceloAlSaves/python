print("Reajuste salarial de um funcionário")
salario = float(input("Digite o salário do funcionário: "))
if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.10)
print("O novo salário do funcionário é: R${:.2f}".format(novo_salario))
