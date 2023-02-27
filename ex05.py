# Cria as variáveis acumuladoras
count = 0
add = 0
# Laço de repetição que pede os 6 números
for x in range(0, 6):
    num = int(input('Choose the {}° integer number: '.format(x+1)))
    # Verifica se é par, e caso sim adiciona o número ao add e +1 ao contador
    if num % 2 == 0:
        count = count + 1
        add = add + num
# Imprime com o plural certo
print('''Among their numbers, there are {} {}
And their sum(of pairs) is equal to: {}'''.format(count, 'pairs' if count != 1 else 'pair', add))
