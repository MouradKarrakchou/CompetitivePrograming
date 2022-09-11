import queue
from inspect import stack

mod, a, b, c = list(map(int, input().split()))
nextElement = a, b, c
x, y, z = list(map(int, input().split()))
configurationObserve = set()
configurationObserve.add(nextElement)
p1 =[]
p2= []
tour = 0

while not (nextElement[0], nextElement[1], nextElement[2]) == (x, y, z):
    a, b, c = nextElement
    l1=[]
    trio1 = (a + b) % mod, (b + c) % mod, (c + a) % mod

    if trio1 not in configurationObserve:
        configurationObserve.add(trio1)
        p2.append(trio1)

    trio2 = (a + 1) % mod, (b - 1) % mod, c % mod
    if trio2 not in configurationObserve:
        configurationObserve.add(trio2)
        p2.append(trio2)

    trio3 = c, b, a
    if trio3 not in configurationObserve:
        configurationObserve.add(trio3)
        p2.append(trio3)

    if not(p1):
        tour += 1
        p1=p2
        p2=[]
    else:
        nextElement = p1.pop()


print(tour)
