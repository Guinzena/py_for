# Coloca valor para a variável add(para evitar erro)
add = 0
count = 0
# Faz o laço de repetição apenas em números ímpares
for x in range(1, 501, 2):
    # Verifica se o número é múltiplo de três
    if x % 3 == 0:
        # Adiciona ao contador
        count = count + 1
        # Adiciona a soma
        add = add + x
print('The sum of the {} numbers requested, is equal to: {}'.format(count, add))
