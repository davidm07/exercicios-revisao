def calcularMulta(peso):
    if peso > 50:
        excesso = peso - 50
        multa  = excesso * 4
        print(f'O excesso de peso é {excesso} quilos e a multa será no valor de R${multa} reais')
    else:
        print(f'Não tem multa para o peso de {peso} quilos')

calcularMulta(65)
calcularMulta(50)
calcularMulta(35)

