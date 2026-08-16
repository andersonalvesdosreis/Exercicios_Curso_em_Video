primeiro = int(input('Digite um valor:'))
segundo = int(input('Digite um valor:'))
terceiro = int(input('Digite um valor:'))
if primeiro > segundo and primeiro > terceiro:
    print(f'O {primeiro} é o maior numero')
if segundo > primeiro and segundo > terceiro:
    print(f'O {segundo} é o maior numero')
if terceiro > primeiro and terceiro> segundo:
    print(f'O {terceiro} é o maior numero')
if primeiro < segundo and primeiro < terceiro:
    print(f'O {primeiro} é o menor numero')
if segundo < primeiro and segundo < terceiro:
    print(f'O {segundo} é o menor numero')
if terceiro < primeiro and terceiro < segundo:
    print(f'O {terceiro} é o menor numero')
