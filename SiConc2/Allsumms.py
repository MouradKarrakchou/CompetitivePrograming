l=[]
nombreDentier,nombreDerequete = list(map(int,input().split()))


l=list(map(int,input().split()))
for k in range(nombreDentier):
    if k!=0:
        l[k]+=l[k-1]

for k in range(nombreDerequete):
    a,b = list(map(int, input().split()))
    if a==0:
        print (l[b])
    else:
        print(l[b]-l[a-1])

