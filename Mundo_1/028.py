import random
pergunta = int(input('Tenta acertar um numero de 0 a 5:'))
numero = [0,1,2,3,4,5]
resposta = random.choice(numero)
if pergunta == resposta:
    print('Parabens Acertou!')
else:
    print(f'Errou! o numero era {resposta}')