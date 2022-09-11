from collections import Counter

wordInLetter = input()
word = []
nombrepremier = 669827881051493
dictNumbers = {}
wordlen = 0
for k in wordInLetter:
    word.append(ord(k) - 65)
    wordlen += 1  


def goThrough(x):
    puiss = pow(26, x-1, nombrepremier)
    counterSave = Counter()
    number=0
    for i in range(0,x-1):
        number = (number + word[i]) * 26 % nombrepremier
    number+= word[x-1] % nombrepremier
    for k in range(0, wordlen - x):
        number -= puiss * word[k]
        number = (number*26 + word[k + x]) % nombrepremier
        counterSave.update({number: 1})
        if counterSave.get(number) >= 3:
            return True
    return False


a = 0
b = wordlen
variable=0
while a < b:
    if (b - a) % 2 == 0:
        middle = int((b - a) / 2)
    else:
        middle = (b - a) // 2 + 1
    if goThrough(a + middle):
        a += middle
    else:
        b -= middle
print(a)
