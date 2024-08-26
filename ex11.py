from random import randint


def jogaDados():
    return randint(1, 6)


def jogar_craps():
    dado1 = jogaDados()
    dado2 = jogaDados()
    somadados = dado1 + dado2
    print(f"Você obteve {dado1} e {dado2}. Total: {somadados}")
    if somadados == 7 or somadados == 11:
        print(f'Voce obteve {somadados} e ganhou!')
        return
    elif somadados == 2 or somadados == 3 or somadados == 12:
        print(f'Você obteve {somadados} e isto é um craps! Você perdeu!')
        return
    ponto = somadados
    print(f'Seu ponto é {ponto} continue jogando até conseguir o mesmo valor')
    while True:
        dado1 = jogaDados()
        dado2 = jogaDados()
        somadados = dado1 + dado2
        print(f"Você obteve {dado1} e {dado2}. Total: {somadados}")
        if somadados == ponto:
            print(f"Você obteve {somadados} novamente e ganhou!")
            break
        elif somadados == 7:
            print("Você obteve 7 e perdeu!")
            break


jogar_craps()
