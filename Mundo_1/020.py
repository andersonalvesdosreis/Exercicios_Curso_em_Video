import random
aluno1 = str(input('Qual o nome do primeiro aluno?'))
aluno2 = str(input('Qual o nome do segundo aluno?'))
aluno3 = str(input('Qual o nome do terceiro aluno?'))
aluno4 = str(input('Qual o nome do quarto aluno?'))
alunos = [aluno1,aluno2,aluno3,aluno4]
escolha = random.choice(alunos)
alunos.remove(escolha)
escolha2 = random.choice(alunos)
alunos.remove(escolha2)
escolha3 = random.choice(alunos)
alunos.remove(escolha3)
escolha4 = random.choice(alunos)
print(f'O primeiro aluno à apresentar é {escolha} depois {escolha2} seguindo de {escolha3} e finalizando com {escolha4}')