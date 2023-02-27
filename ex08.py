print('{:-^30}'.format(' PALINDROME CHECKER '))
text = str(input('Type some sentence: '))
count = 0
# Transforma o texto digitado em uma lista por caractéres(MAIÚSCULAS) e conta quantas elas são
liststr = list(text.upper().replace(' ', ''))
sizelist = len(liststr)
# Cria uma lista vazia(mas com o mesmo tamanho da original), onde será inserido o valor inverso
invertlist = list(range(0, sizelist))
# Começa da última casa da lista, contando de trás pra frente até a primeira
for x in range(sizelist - 1, -1, -1):
    # Grava a mesma coisa na invertlist só que ao contrário
    invertlist[count] = liststr[x]
    count = count + 1
print(invertlist)
# Verifica se a frase ao contrário é igual ela normal(um palíndromo)
if liststr == invertlist:
    print('The sentence entered is a palindrome!')
else:
    print('The sentence entered is not a palindrome!')
