N, M = list(map(int, input().split()))
tabPuiss = {}


def intToBase(x):
    return (int(x, 16))


tabPuiss[1] = list(map(intToBase, input().split()))
tab = []
for k in range(M):
    tab.append(list(map(int, input().split())))
puiss = 1
index = 1
rangee=N
while N-puiss > 0:
    rangee-=puiss
    tabPuiss[puiss*2]=[]
    for j in range(0, rangee):
        tabPuiss[puiss*2].append(tabPuiss[puiss][j] | tabPuiss[puiss][j + puiss])
    puiss *= 2

for k in range(M):
    a, b = tab[k]
    valeur = 0
    n=b-a+1
    while n:
        x = n & ~(n - 1)
        valeur |= tabPuiss[x][b - x + 1]
        b -= x
        n -= x
    print(f'{valeur:X}')
