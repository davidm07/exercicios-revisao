from math import sqrt

a = int(input('Informe o valor de A: '))

if a == 0 :
    print('Valor de a é 0 então não é uma equação de segundo grau. FIM.')
else :
    b = int(input('Informe o valor de B: '))
    c = int(input('Informe o valor de C: '))
    delta = b*b - (4*a*c)
    if delta < 0:
        print('Delta negativo. Equação não possui raízes')
    elif delta == 0:
        raiz = -b/(2*a)
        print(f"A raíz é {raiz}")
    else:
        raiz1 = (-b + sqrt(delta))/(2*a)
        raiz2 = (-b - sqrt(delta))/(2*a)
        print(f"Os valores das raízes são {raiz1} e {raiz2}")