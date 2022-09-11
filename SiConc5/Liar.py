N = int(input())
l = []
liar = 0

for k in range(N):
    l.append(list(map(float, input().split())))
    l[k].append(k + 1)

l.sort()

k = 0
while k <= N - 1:
    if k!=N-1 and l[k][0] == l[k + 1][0]:
        if l[k][1]!=l[k+1][1]:
            if k != 0:
                if l[k + 1][1] >= l[k - 1][1]:
                    liar = l[k + 1][2]
            if k < N - 2:
                if l[k][1] <= l[k + 2][1]:
                    liar = l[k][2]
            break
    elif k < N - 3 and l[k][1] <= l[k + 1][1] and l[k][1] <= l[k + 2][1]:
        liar = l[k][2]
    elif k > 1 and l[k][1] >= l[k - 1][1] and l[k][1] >= l[k - 2][1]:
        if l[k][0] != l[k - 1][0] and l[k][0] != l[k - 2][0]:
            liar = l[k][2]
    k += 1;

print(liar)
