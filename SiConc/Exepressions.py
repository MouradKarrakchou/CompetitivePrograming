from fractions import Fraction

exp1 = list(map(str, input().split()))
exp2 = list(map(str, input().split()))

expvalue=[]

def equat(var, param1, param2):
        if var=="+":
            return param2 + param1
        if var=="-":
            return param2 - param1
        if var=="*":
            return param2 * param1
        if var=="/":
            return Fraction(param2,param1)


def verify(exp):
    liste = []
    k=0;
    while (k<len(exp)):
        var = exp[k]
        if not var.isdigit():
            if len(liste) >= 2:
                var1 = int(liste.pop())
                var2 = int(liste.pop())
                if var=='/' and int(var1) == 0:
                    return False
                liste.append(equat(var, var1, var2))
            else:
                return False
        else:
            liste.append(var)
        k+=1
    if len(liste)==1:
        expvalue.append(liste[0])
    return (len(liste)==1)


is1true=verify(exp1)
is2true=verify(exp2)
print((not is1true and not is2true) or(len(expvalue)==2 and expvalue[0]==expvalue[1]))