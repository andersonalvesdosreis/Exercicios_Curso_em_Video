pergunta = float(input('Qual seu salario?'))
resposta1 = float(pergunta*0.10)
resposta2 = float(pergunta*0.15)
if pergunta >= 1250:
    print(f'\033[36 Parabens Ganhou um aumento para {pergunta+resposta1}')
else:
    print(f'\033[36 Parabens Ganhou um aumento para {pergunta+resposta2}')