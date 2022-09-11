from collections import Counter
from fractions import Fraction

puiss = 1
wordInLetter = input()
word = []
nombrepremier = 884819461
dictNumbers = {}
wordlen = 0
for k in wordInLetter:
    word.append(ord(k) - 65)
    wordlen += 1


def goThrough(x):
    counterSave = Counter()
    number = 0
    for i in range(x):
        number = (number + word[i]) * 26 % nombrepremier
    for k in range(0, wordlen - x):
        number -= puiss * word[k]
        number = (number + word[k + x]) * 26 % nombrepremier
        counterSave.update({number: 1})
        if counterSave.get(number) >= 3:
            return True
    return False


a = 0
b = wordlen
variable=0
# Pour éviter de recalculer à chaque fois de grandes puissances on les recalcule à partir de la puissance trouvé au
# rang n-1
while a < b:
    if (b - a) % 2 == 0:
        middle = int((b - a) / 2)
    else:
        middle = (b - a) // 2 + 1
    if variable==0:
        puiss = pow(26, middle, nombrepremier)
    else:
        if b - middle == a + middle:
            puiss = int(Fraction(puiss,pow(26,middle)))
        else:
            puiss = int(Fraction(puiss,pow(26,middle-1)))
    if goThrough(a + middle):
        a += middle
        variable=0
    else:
        if b-middle!=a+middle:
            puiss= int(Fraction(puiss,26))
        b -= middle
        variable=1
print(a)
