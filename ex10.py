# Cria os contadores de maior e menor peso
maxweight = 0
minweight = 0
# Vai perguntar o peso de 5 pessoas
for x in range(1, 6):
    weight = float(input('What is the weight of the {}° person(Kg)? '.format(x)))
    # Automaticamente se for a 1° vez no laço, coloca o 1° peso inserido como maior e menor
    if x == 1:
        maxweight = weight
        minweight = weight
    else:
        # Seleciona qual é mior e qual é menor
        if weight > maxweight:
            maxweight = weight
        elif weight < minweight:
            minweight = weight
print('''The highest weight entered was {}Kg,
And the smallest weight entered was {}Kg.'''.format(maxweight, minweight))
