def moyenne(l, coefnote):
    sum = 0
    for k in range(len(l) - 1):
        sum += int(l[k + 1]) * int(coefnote[k])
    return sum


def bettermoyenne(l, coefdesnotes):
    moyennehaute = moyenne(l[0], coefdesnotes)
    eleve = l[0][0]
    for k in l:
        nouvemoyenne = moyenne(k, coefdesnotes)
        if moyennehaute < nouvemoyenne:
            moyennehaute = nouvemoyenne
            eleve = k[0]
        elif moyennehaute==nouvemoyenne:
            eleve="EX AEQUO"
    return eleve

list1=list(map(int,input().split()))
nombreDeleve = list1[0]
nombreDeMatière = list1[1]

coefdesnotes = list(map(int,input().split()))

i=0
l = []
while i < nombreDeleve:
    l.append([])
    l[i]=list(map(str,input().split()))
    i+=1

print(bettermoyenne(l, coefdesnotes))
