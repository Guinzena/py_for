print("Let's make a multiplication table!")
num = int(input('With which number do you want to do it? '))
for x in range(1, 11):
    # Para fazer a separação
    print('=' * 15)
    # Imprime os números e sua multiplicação de acordo com qual coluna
    print('{} x {:2} = {}'.format(num, x, num * x))
print('=' * 15)
