import time
start_time = time.time()

word = input()
nombrepremier = 3524627047
dictNumbers = {}
dictChangeCharacter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
                       "L": 11,
                       "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21,
                       "W": 22, "X": 23, "Y": 24, "Z": 25}
wordlen = len(word)


def goThrough(x):
    puiss = 26 ** x
    number = 0
    for i in range(x):
        number = (number + dictChangeCharacter[word[i]]) * 26 % nombrepremier
    for k in range(0, wordlen - x):
        number -= puiss * dictChangeCharacter[word[k]]
        number = (number + dictChangeCharacter[word[k + x]]) * 26 % nombrepremier
        if number in dictNumbers:
            dictNumbers[number] += 1
            if dictNumbers[number] == 3:
                return True
        else:
            dictNumbers[number] = 1
    return False


a = 0
b = wordlen

while a < b:
    if (b - a) % 2 == 0:
        middle = int((b - a) / 2)
    else:
        middle = (b - a) // 2 + 1
    if goThrough(a + middle):
        a += middle
    else:
        b -= middle
    dictNumbers.clear()
print(a)
print("--- %s seconds ---" % (time.time() - start_time))