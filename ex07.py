# Gera o contador para evitar erros
count = 0
num = int(input('Choose a integer number: '))
# Laço que divide o número escolhido por todos os números até ele
for x in range(1, num + 1):
    # Descobre se foi possível dividir sem restos
    if num % x == 0:
        # Se aconteceu divisão, soma +1 ao contador e escreve o dividendo em verde
        count = count + 1
        print('\033[32m{}\033[m'.format(x), end=' ')
        # Se não escreve o dividendo em vermelho
    else:
        print('\033[31m{}\033[m'.format(x), end=' ')
# Se ultrapassar 2 divisões, então não é primo
print('''\nYour number {} has been divided {} times
{} a prime number!'''.format(num, count,
                             '''\033[32mSo it's''' if count == 2 else '\033[31mSo it is not'))
