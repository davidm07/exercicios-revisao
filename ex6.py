while True:
    try: 
        paisA = int(input('Informe a população do país A: '))
        taxaA = float(input('Informe a taxa de crescimento do país A: '))
        paisB = int(input('Informe a população do país B: '))
        taxaB = float(input('Informe a taxa de crescimento do país B: '))
        count = 0
    except(TypeError, ValueError):
        print('Erro! Informe um valor válido.')
    else:
        while paisA <= paisB:
            paisA += paisA*(taxaA/100)
            paisB += paisB*(taxaB/100)
            count += 1
        print(f'Serão necessários {count} anos')
        while True:
            op = input("Deseja informar novos valores? S/N: ").upper()
            if op in 'SN':
                break
            else:
                print("Opção inválida! Por favor, escolha 'S' para sim ou 'N' para não.")
        if op == 'N':
            break
        


