nome = str(input('Qual seu nome completo?')).strip()
print(f'Seu nome maiusculo é {nome.upper()}')
print(f'Seu nome minusculo é {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras')

primeironome = nome.split()
print(f'Seu primeiro nome é {primeironome[0]} e tem {len(primeironome[0])} letras')