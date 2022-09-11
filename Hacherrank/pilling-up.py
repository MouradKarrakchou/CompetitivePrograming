T = int(input())


def verif(L, currentValue, start, end):
    while start != end:
        if max(L[start], L[end]) > currentValue:
            return False
        elif L[start] >= L[end]:
            currentValue = L[start]
            start += 1
        else:
            currentValue = L[end]
            end -= 1
    return currentValue >= L[start]


for _ in range(T):
    n = int(input())
    L1 = list(map(int, input().split()))
    bool = False
    if L1[0] > L1[-1]:
        bool = verif(L1, L1[0], 1, n-1)
    else:
        bool = verif(L1, L1[-1], 0, n - 2)
    if bool:
        print("Yes")
    else:
        print("No")
