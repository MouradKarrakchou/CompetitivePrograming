import colorsys
from decimal import Decimal

list = list(map(str, input().split()));
newList = [];


def hsv(inp):
    R = int(inp[1] + inp[2], 16)
    G = int(inp[3] + inp[4], 16)
    B = int(inp[5] + inp[6], 16)
    return (colorsys.rgb_to_hsv(R, G, B)[0])

uneValTraité=False
for k in list:
    hsvVar = Decimal(hsv(k))
    if (hsvVar != 0):
        newList.append(hsvVar)
        if (not uneValTraité):
            newList.append(hsvVar + 1)
            uneValTraité=False

newList.sort()
max = 0
for k in range(len(newList) - 1):
    testValue = newList[k + 1] - newList[k]
    if testValue > max:
        max = testValue

print(f'{max:.5f}')
