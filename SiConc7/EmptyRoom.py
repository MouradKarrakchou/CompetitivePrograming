import heapq

N = int(input())

tab = []
listeheap = []
heapValue = []
for k in range(N):
    a, b, c, d = list(map(int, input().split()))
    tab.append([[a, b], [c, d]])
    listeheap.append((a, b))
    listeheap.append((c, d))
listeheap.sort()
heapq.heapify(listeheap)

i = 0
while i < len(listeheap):
    current = listeheap.pop()
    j = 0
    while len(heapValue) > 0 and heapValue[1] > current[1]:
        del a[0]
        j += 1
    i += 1
