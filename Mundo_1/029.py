from time import sleep
pergunta = int(input('Qual a velocidade do carro?'))
resposta = int(pergunta-80)
print('Verificando...')
sleep(3)
if pergunta < 80:
    print('Esta na velocidade ideal, boa viagem')
else:
    rg = int(resposta*7)
    print('\033[31mVocê está acima da velocidade!\033[m')
    print('Vou verificar o valor da multa')
    sleep(3)
    print(f'Deve-se pagar R${rg}')