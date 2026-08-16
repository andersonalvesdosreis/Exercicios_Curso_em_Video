n1 = float(input('Digite o numero de um cateto: '))
n2 = float(input('Digite o numero de um cateto: '))
n3 = float(input('Digite um numero de uma hipotenusa: '))
if n3**2 == n2**2 + n3**2:
    print('Forma um triangulo')
else: 
    print('Não forma um triangulo')