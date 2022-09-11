def verify(lig,col,l):
    for k in range(3):
        if lig+k-1<Nligne and lig+k-1>=0:
            for j in range(3):
                if col+j-1<Mcolonne and col+j-1>=0:
                    a=lig+k-1
                    b=j+col-1
                    if (l[a][b]=='#'):
                        return(False)
    return(True)


l = []
Nligne, Mcolonne = list(map(int, input().split()))
for k in range(Nligne):
    l+=[list(input())]

caseseche=0
for lig in range(Nligne):
    for col in range (Mcolonne):
        if (l[lig][col]=='.'):
            if (verify(lig,col,l)):
                caseseche+=1

print(caseseche)