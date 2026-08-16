pergunta = int(input('Qnts km vai dar a viajem?'))
resposta = float(pergunta*0.50)
respostaalternativa = float(pergunta*0.45)
if pergunta > 200:
    print(f'\033[32m A viagem custara R${respostaalternativa}')
else:
    print(f'\033[36m A viagem custara R${resposta}')