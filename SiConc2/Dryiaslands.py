def iswater(lig, col, l):
    for k in range(3):
        if lig + k - 1 < Nligne and lig + k - 1 >= 0:
            for j in range(3):
                if col + j - 1 < Mcolonne and col + j - 1 >= 0:
                    a = lig + k - 1
                    b = j + col - 1
                    if (l[a][b] == '#'):
                        return False
    return True

l = []
Nligne, Mcolonne = list(map(int, input().split()))
for k in range(Nligne):
    l += [list(input())]

numberIsland=0

def isisland(string,lig,col):
    if lig-1>=0 and l[lig - 1][ col][0] == string:
        return l[lig - 1][ col][1]
    if lig+1<Nligne and l[lig + 1][col][0] == string:
        return l[lig + 1][col][1]
    if col-1>=0 and l[lig][ col - 1][0] == string:
        return l[lig][ col - 1][1]
    if col+1<Mcolonne and l[lig][ col + 1][0] == string:
        return l[lig][ col + 1][1]
    return -1


def numerousIsland(lig, col, l):
    numerodesiles=[l[lig][col]];
    numberOfIsland = 0
    if col-1>=0 and l[lig][ col-1][0] == 'i':
        if not l[lig][col-1] in numerodesiles:
            numerodesiles += [l[lig][col-1]]
            numberOfIsland += 1
    if lig+1<Nligne and l[lig + 1][col][0] == 'i':
        if  not l[lig + 1][col] in numerodesiles:
            numerodesiles+=[l[lig + 1][col]]
            numberOfIsland += 1
    if lig-1>=0 and l[lig-1][ col][0] == 'i':
        if not l[lig-1][ col] in numerodesiles:
            numerodesiles += [l[lig-1][ col]]
            numberOfIsland += 1
    if col+1<Mcolonne and l[lig][ col + 1][0] == 'i':
        if not l[lig][ col + 1] in numerodesiles:
            numerodesiles += [l[lig][ col + 1]]
            numberOfIsland += 1
    return numberOfIsland


nombredile = 0
for lig in range (Nligne):
    for col in range(Mcolonne):
        if (l[lig][col] == '.'):
            if iswater(lig,col,l):
                islandname=isisland('i',lig,col)
                if int(islandname)<0:
                    l[lig][col] = 'i'+str(numberIsland)
                    numberIsland+=1
                    nombredile += 1
                else:
                    l[lig][col] = 'i' + islandname
                    nombredile -= numerousIsland(lig, col, l)

print(nombredile)
