temperaturas = list()

for x in range(12):
    temperaturas.append(float(input(f'Informe a média de temperatura do mês {x+1}: ')))
    
soma_temp = sum(temperaturas)
media_temp = soma_temp/len(temperaturas)

for i, temp in enumerate(temperaturas):
    if temp > media_temp:
        print(f'Temperatura acima da média no mês {i+1}, com a temperatura de: {temp} graus')



