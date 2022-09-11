hg = ["┌"]
hd = ["┐"]
bg = ["└"]
bd = ["┘"]
l = [hg, hd, bg, bd]

def update(hg, hd, bg, bd):
    newHg = fusionate(hg, hd) + fusionate(bg, hg)
    newHd = fusionate(hg, hd) + fusionate(hd, bd)
    newBg = fusionate(hg, bg) + fusionate(bg, bd)
    newBd = fusionate(bd, hd) + fusionate(bg, bd)
    return newHg, newHd, newBg, newBd

def fusionate(a,b):
    l3=[]
    for k in range(len(a)):
        l3+=[""]
        l3[k]= a[k]+b[k]
    return l3

i = int(input())
for k in range(i-1):
    l = update(hg, hd, bg, bd)
    hg, hd, bg, bd = l
m="\n".join(fusionate(hg,hd)+fusionate(bg,bd))
print(m)
