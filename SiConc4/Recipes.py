mod, a, b, c = list(map(int, input().split()))
nextElement = a, b, c
x, y, z = list(map(int, input().split()))
configurationObserve = set()
configurationObserve.add(nextElement)
p1 = []
p2 = []
tour = 0

if (x, y, z) not in configurationObserve:
    while True:
        a, b, c = nextElement
        l1 = [((a + b) % mod, (b + c) % mod, (c + a) % mod), ((a + 1) % mod, (b - 1) % mod, c % mod), (c, b, a)]
        for k in l1:
            if k not in configurationObserve:
                configurationObserve.add(k)
                p2.append(k)

        if not p1:
            tour += 1
            p1 = p2
            p2 = []
            if (x, y, z) in configurationObserve:
                break
        else:
            nextElement = p1.pop()

print(tour)
