N = int(input())
list1 = [0 for _ in range(N+1)]
compt = 0
for k in range(N-1):
    a, b = list(map(int, input().split()))
    list1[a] += 1
    if list1[a] == 2:
        compt += 1
    list1[b] += 1
    if list1[b] == 2:
        compt += 1
print(N-compt)
