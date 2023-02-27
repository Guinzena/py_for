# Realiza a contagem de números pares de 2 á 50
for x in range(2, 51, 2):
    # Coloca todos os números na mesma linha, separados por espaço
    print(x, end=' ')
print('End')
# Somente para separar os dois códigos
print('=' * 75)
# Ou(Opção 2):
for x in range(1, 51):
    if x % 2 == 0:
        print(x, end=' ')
print('End')
