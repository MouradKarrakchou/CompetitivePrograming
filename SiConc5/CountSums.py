import math

S, N = list(map(int, input().split()))
l = []
liar = 0
marge = S
l = list(map(int, input().split()))
for k in range(N):
    marge -= l[k]
if marge == 0:
    print(1)
elif marge < 0:
    print(0)
elif N == 0:
    print(0)
else:
    N -= 1
    marge += N
    print(math.comb(marge, N))
