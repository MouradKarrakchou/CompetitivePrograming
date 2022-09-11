import re
from collections import Counter
def mix(s1, s2):
    l1=re.findall("[a-z]",s1)
    l1.sort()
    l2=re.findall("[a-z]",s2)
    l2.sort()
    c1=Counter(l1)
    c2=Counter(l2)
    mot=""
    letprec=""
    phrase=[]
    for i in range(len(l1)):
        k=l1[i]
        if k!=letprec:
            mot=""
            letprec=k
            e1=c1.get(k)
            e2=c2.get(k)
            if e2==None:
                e2=0
            if e2==e1:
                mot+="=:"
            elif e2>e1:
                mot+="2:"
            else:
                mot += "1:"
            for i in range(max(e1,e2)):
                mot+=k
            mot+="/"
            if max(e1,e2)>1:
                if e1==e2:
                    phrase.append([max(e1, e2)+0.1, mot])
                elif e2>e1:
                    phrase.append([max(e1,e2)+0.2,mot])
                else:
                    phrase.append([max(e1, e2) + 0.3, mot])
    for i in range(len(l2)):
        k=l2[i]
        if k!=letprec:
            mot=""
            letprec=k
            e1=c1.get(k)
            e2=c2.get(k)
            if e1==None :
                e1=0
                if e2==e1:
                    mot+="=:"
                elif e2>e1:
                    mot+="2:"
                else:
                    mot += "1:"
                for i in range(max(e1,e2)):
                    mot+=k
                mot+="/"
                if max(e1,e2)>1:
                    if e1==e2:
                        phrase.append([max(e1, e2)+0.1, mot])
                    elif e2>e1:
                        phrase.append([max(e1,e2)+0.2,mot])
                    else:
                        phrase.append([max(e1, e2) + 0.3, mot])

    phrase.sort()
    mot=""
    l=[]
    for k in range(len(phrase)):
        if k>0 and k<len(phrase)-1:
            if phrase[-k-1][0]!=phrase[-k][0] and len(l)>0:
                for u in range (len(l)):
                    for j in range (len(l[u])):
                        mot+=l[-u-1][-j-1]
                l=[]
            if phrase[-k-1][0]==phrase[-k-2][0]:
                l.append([phrase[-k-1][1]])
            else:
                mot += phrase[-k - 1][1]
        elif(k==0):
            if phrase[-k-1][0]==phrase[-k-2][0]:
                l.append([phrase[-k-1][1]])
            else:
                mot+=phrase[-k-1][1]
        else:
            if phrase[0][0]==phrase[1][0]:
                    mot += phrase[-k - 1][1]
            if len(l)>0:
                for u in range(len(l)):
                    for j in range(len(l[u])):
                        mot += l[-u - 1][-j - 1]
            if phrase[0][0]!=phrase[1][0]:
                mot += phrase[-k - 1][1]
    return(mot[:-1])

