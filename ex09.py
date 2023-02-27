from datetime import date
# Variáveis criadas para contar o número de pessoas com e sem Maioridade
maycount = 0
mincount = 0
# Laço que perguntará seis vezes o ano de nascimento de seis pessoas
for age in range(1, 8):
    ageacc = int(input('What year was the {}° person born? '.format(age)))
    if date.today().year - ageacc >= 21:
        # Soma +1 aos com Maioridade
        maycount = maycount + 1
    else:
        # Soma +1 aos sem Maioridade
        mincount = mincount + 1
print('''In all we had {} people of age, 
And {} people who are under the age of majority.'''.format(maycount, mincount))
