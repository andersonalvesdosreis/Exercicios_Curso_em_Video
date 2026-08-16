numero = int(input('Digite um numero'))
u = numero // 1 %10
d = numero // 10 %10
c = numero // 100 %10
m = numero // 1000 %10
print(f'Seu numero tem {u} casas de unidades')
print(f'Seu numero tem {d} casas de dezenas')
print(f'Seu numero tem {c} casas de centanas')
print(f'Seu numero tem {m} casas de milhares')