# Somente um print
print('{:-^30}'.format(' ARITHMETIC PROGRESSION(10) '))
term = int(input('Choose your term: '))
ratio = int(input('And now, choose your reason: '))
# Calcula até que número ir par ao termo máximo
maxt = term + (ratio * 10)
# Coloca o termo e a razão nos lugares certos
for x in range(term, maxt, ratio):
    print('-> {} '.format(x), end='')
