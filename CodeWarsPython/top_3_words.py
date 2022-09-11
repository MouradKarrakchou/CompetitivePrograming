def isaword(word):
    for k in word:
        if (k.isalpha()):
            return True
    return False

def top_3_words(text):
        text+=" "
        l=[];
        word=[];
        for k in text:
            if k.isalpha() or k=="'":
                word+=k.lower()
            else:
                if len(word)!=0 and isaword(word):
                    l.append(word);
                    word=[];
        l.sort()
        if len(l)==0:
            return([])
        k=0;
        lastletter=l[0];
        l2=[[1,l[0]]]
        while k<len(l):
            if lastletter!=l[k]:
                l2.append([1,l[k]])
                lastletter=l[k]
            else:
                l2[-1][0]+=1
            k+=1;
        l2.sort()
        l3=[]
        word=""
        l4=[]
        for i in range(len(l2)):
            k=l2[-i-1]
            word=""
            for j in range (len(k[1])):
                word+=k[1][j]
            l4.append(word)
        if len(l4)<3:
            return(l4)
        return([l4[0],l4[1],l4[2]])

