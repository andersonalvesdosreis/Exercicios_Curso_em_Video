pergunta = str(input("onde você nasceu?")).strip()
pergunta2 = pergunta.lower()
resposta2 = pergunta2.split()
resposta = resposta2[0]
if resposta == str('santo'):
    print(True)
else:
    print(False)
