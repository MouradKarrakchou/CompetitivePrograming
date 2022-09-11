def copy(a,b,str):
    str2=""
    for k in range (len(str)):
        if k==a:
            str2+=str[b]
        elif k==b:
            str2+=str[a]
        else:
            str2+=str[k]
        return(str2)
def next_smaller(n):
    nomb=str(n)
    lenn=len(nomb)
    for j in range(lenn):
        for k in range (lenn):
            if lenn<k+j:
                break
            if nomb[-k-1]<nomb[-k-j-1]and nomb[-k-1]!=0:
                copy(lenn-k-1,lenn-k-j-1,nomb)
                return(nomb)
    return(nomb)

print(next_smaller(907))