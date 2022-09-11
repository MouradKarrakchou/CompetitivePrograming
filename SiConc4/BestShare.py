N, Wj, Wh = list(map(int, input().split()))
l=[]
for k in range (N):
    l.append(list(map(int, input().split())))

dict={}
item=l.pop()

while True:
    for k in dict.keys():
        if k+item<Wj:
            l[k+item[1]].apend(l[k]+item[0])
