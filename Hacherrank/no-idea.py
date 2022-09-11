n,m=list(map(int,input().split()))
L=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
compt=0
for x in L:
    if x in A:
        compt+=1
    elif x in B:
        compt-=1

print(compt)