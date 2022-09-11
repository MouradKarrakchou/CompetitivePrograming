def beeramid(bonus,price):
    numberOfBeers=bonus//price;
    if numberOfBeers<0:
        return (0)
    k = 0;
    comptpaire = 0;
    comptimpaire =0;
    totalofcan=0;
    while totalofcan<=numberOfBeers:
        k += 1
        if k == 2:
            comptpaire = 4
            totalofcan += comptpaire
        elif k == 1:
            comptimpaire = 1
            totalofcan += comptimpaire
        elif k % 2 == 0:
            comptpaire += (k-1) * 4
            totalofcan += comptpaire
        elif k % 2 == 1:
            comptimpaire += (k-1) * 4
            totalofcan+=comptimpaire

    return k-1

print(beeramid(21, 1.5))