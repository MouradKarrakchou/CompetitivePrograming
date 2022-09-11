def littleWord(l):
    smallestWord = l[0]
    minlen = len(l[0])
    i = 0
    for k in l:
        if len(k) < minlen:
            minlen = len(k)
            smallestWord = k
        elif len(k) == minlen:
            if k < smallestWord:
                smallestWord = k
        i += 1
    return smallestWord


nombreDeMot = int(input())
list=[]
j = 0
while j < nombreDeMot:
    j += 1
    list.append(input())

print(littleWord(list))
