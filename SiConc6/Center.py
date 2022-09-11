N = int(input())
feuille = set()
list1 = [set() for _ in range(N + 1)]
pile = [1]
listcompte = [0 for k in range(N + 1)]

for k in range(N - 1):
    a, b = list(map(int, input().split()))
    list1[a].add(b)
    listcompte[a] += 1
    list1[b].add(a)
    listcompte[b] += 1
    if listcompte[a] == 2:
        feuille.remove(a)
    elif listcompte[a] == 1:
        feuille.add(a)

    if listcompte[b] == 2:
        feuille.remove(b)
    elif listcompte[b] == 1:
        feuille.add(b)

etape = 0

while N > 2:
    nextfeuille = set()
    copylist = listcompte.copy()
    for k in feuille:
        if copylist[k] == 1:
            listcompte[k] -= 1
            N -= 1
            for j in list1[k]:
                if listcompte[j] != 1:
                    listcompte[j] -= 1
                if listcompte[j] == 1:
                    nextfeuille.add(j)

    feuille = nextfeuille
    etape += 1

if len(feuille) == 2:
    print(etape + 1)
    print(feuille.pop(), feuille.pop())
else:
    print(etape)
    print(feuille.pop())
