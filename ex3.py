valor = float(input("Informe o valor da hora: "))
horas = float(input("Informe as horas trabalhadas: "))
salario = valor * horas

print(f"Salario bruto: {valor} * {horas}: R$ {valor*horas}")

if salario <= 900:
    ir = 0
    print(f'IR isento')
elif salario <= 1500 and salario > 900:
    ir = salario*0.05
    print(f'IR 5%: R$ {ir}')
elif salario <= 2500 and salario > 1500:
    ir = salario*0.10
    print(f'IR 10%: R$ {ir}')
else :
    ir = salario*0.20
    print(f'IR 20%: R$ {ir}')

inss = salario*0.1
print(f'INSS 10%: R$ {inss}')

fgts = salario*0.11
print(f'FGTS 11%: R$ {fgts}')

print(f'Total de descontos: R${inss+ir}')

salario_liquido = salario - (inss + ir)
print(f'Total de descontos: R$ {salario_liquido}')
