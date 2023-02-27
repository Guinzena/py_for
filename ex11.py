# Cria uma lista das idades, para fazer a soma no final(podia ser feito com um acumulador)
age = list(range(0, 4))
# Cria contadores para máxima idade masculina, nome do homem mais velho, e número de mulheres jovens
maxmaleage = 0
olderman = ''
countyfemale = 0
# Laço para perguntar para 4 participantes
for x in range(1, 5):
    print('---- {}° PERSON ----'.format(x))
    name = str(input('What is the name of the {}° person? '.format(x))).strip()
    age[x - 1] = int(input('How old is the {}° person? '.format(x)))
    gender = str(input('What is the gender of the {}° person?[M/F] '.format(x))).strip().upper()
    # Se o gênero for M verificará se é mais velho do que o último registrado em maxmaleage
    if gender == 'M' and age[x - 1] > maxmaleage:
        # Troca a idade mais velha e o homem mais velho
        maxmaleage = age[x - 1]
        olderman = name
    # Se o genêro for F verificará se é mais nova que 20 anos, e caso sim, somará +1 ao contador
    if gender == 'F' and age[x - 1] < 20:
        countyfemale = countyfemale + 1
# Faz a média das idades
average = sum(age) / 4
print('The average age of the group is {} years,'.format(average))
print('The oldest man is named {} and is {} years old,'.format(olderman, maxmaleage))
print('There are {} women under 20 years old.'.format(countyfemale))
