N, D = list(map(int, input().split()))
INF = float("inf")
tab = []
listMin = [0 for _ in range(N)]
dist = 0
for k in range(D):
    tab.append(list(map(int, input().split())))

for k in range(N-1):
    col=N-k-2
    minimum=INF
    for j in range(min(k+1,D)):
        val=tab[j][col]+listMin[col+j+1]
        if val<minimum:
            minimum=val
    listMin[col]=minimum

print(listMin[0])


