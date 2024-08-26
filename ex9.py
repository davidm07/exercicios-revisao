from random import randint

contadores = [0,0,0,0,0,0]

for x in range(100):
    sorteio = randint(1,6)
    contadores[sorteio - 1] += 1
    
for i in range(6):
    print(f'O valor de {i+1} for sorteado {contadores[i]}')