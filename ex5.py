paisA = 80000
paisB = 200000
count = 0

while True:
    paisA += paisA*0.03
    paisB += paisB*0.015
    count += 1
    if paisA >= paisB:
        break

print(f'Serão necessário {count} anos')
