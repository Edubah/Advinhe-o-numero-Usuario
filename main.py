import random

def advinha (x):
    numero_aleatorio = random.randint(1, x)
    advinha = 0
    while advinha != numero_aleatorio:
        advinha = int(input(f'Advinhe um número entre 1 e {x}: '))
        if advinha < numero_aleatorio:
            print('Advinhe novamente, chute foi muito baixo!')
        elif advinha > numero_aleatorio:
            print('Advinhe novamente, chute muito alto!')
    print(f'BOA!! Você acertou o número {numero_aleatorio} corretamente!!!')

def advinha_computador(x):
    baixo = 1
    alto = x
    feedback = ''
    while feedback != 'c':
        if baixo != alto:
            advinha = random.randint(baixo, alto)
        else:
            advinha = baixo
        feedback = input(f'O número {advinha} está muito alto (A), baixo (B) ou correto (C)? ').lower()
        if feedback == 'a':
            alto = advinha - 1
        elif feedback == 'b':
            baixo = advinha + 1
    print(f'HAHAH, o computador advinhou seu número, {advinha}, corretamente!!!!')

advinha_computador(10)