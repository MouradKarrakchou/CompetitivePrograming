import collections

N, K = list(map(int, input().split()))
dictDeNom = collections.defaultdict(lambda: [0, 0])

for k in range(N):
    currentValue = input()
    dictDeNom[currentValue][0] += 1
    dictDeNom[currentValue][1] = k

od = sorted(dictDeNom.items(), key=lambda var: (var[1][0], var[1][1]), reverse=True)

for i in range(K):
    print(od[i][0])
