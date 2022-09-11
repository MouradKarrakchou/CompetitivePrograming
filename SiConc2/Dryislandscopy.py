def change(lig, col, l):
    for k in range(3):
        if lig + k - 1 < Nligne and lig + k - 1 >= 0:
            for j in range(3):
                if col + j - 1 < Mcolonne and col + j - 1 >= 0:
                    a = lig + k - 1
                    b = j + col - 1
                    if (l[a][b] != '#'):
                        l[a][b] = 'v'


def isl(a, b, l):
    if (l[a][b] == '.'):
        l[a][b] = 'i'
        island(a, b, l)


def island(lig, col, l):
    if lig + 1 < Nligne:
        isl(lig + 1, col, l)
    if lig - 1 >= 0:
        isl(lig - 1, col, l)
    if col + 1 < Mcolonne:
        isl(lig, col + 1, l)
    if col - 1 >= 0:
        isl(lig, col - 1, l)


l = []
Nligne, Mcolonne = list(map(int, input().split()))
for k in range(Nligne):
    l += [list(input())]

for lig in range(Nligne):
    for col in range(Mcolonne):
        if (l[lig][col] == '#'):
            change(lig, col, l)


def isisland(string):
    numberOfIsland = 0
    if lig-1>0 and l[lig - 1, col] == string:
        return False
    if lig+1<Nligne and l[lig + 1, col] == string:
        return False
    if col-1>0 and l[lig, col - 1] == string:
        return False
    if col+1<Mcolonne and l[lig, col + 1] == string:
        return False
    return True


def numerousIsland(lig, col, l):
    numberOfIsland = 0
    if lig-1>0 and l[lig - 1, col] == 'i':
        numberOfIsland += 1
    if lig+1<Nligne and l[lig + 1, col] == 'i':
        numberOfIsland += 1
    if col-1>0 and l[lig, col - 1] == 'i':
        numberOfIsland += 1
    if col+1<Mcolonne and l[lig, col + 1] == 'i':
        numberOfIsland += 1
    return numberOfIsland


nombredile = 0
for lig in range(Nligne):
    for col in range(Mcolonne):
        if (l[lig][col] == '.'):
            if not isisland('#'):
                if not isisland('i'):
                    l[lig][col] == 'i'
                    nombredile += 1
                else:
                    nombredile -= numerousIsland(lig, col, l)
                    l[lig][col] == 'i'

print(nombredile)
