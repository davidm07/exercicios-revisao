from math import ceil

def calculaTinta(area):
    if area < 108:
        print(f'Sera necessária 1 lata de 18 litros no valor de 80 reais')
    else :
        qntdLatao = area / 108
        qntdLatao = ceil(qntdLatao)
        print(f'Serão necessárias {qntdLatao} latas de tinta no valor de {qntdLatao*80} reais')
    if area < 21.6 :
        print(f'Sera necessário 1 galão de 3,6 litros no valor de 25 reais')
    else :
        qntdGalao = area / 21.6
        qntdGalao = ceil(qntdGalao)
        print(f'Serão necessários {qntdGalao} galões de tinta no valor de {qntdGalao*25} reais')

def calculaEconomia(area):
    area_folga = area * 0.1
    litrosNecessarios = area_folga / 6
    #não consegui pensar no restante da lógica

calculaTinta(190)
calculaTinta(60)
calculaTinta(190)
