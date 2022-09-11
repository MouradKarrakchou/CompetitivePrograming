h, w = list(map(int, input().split()));
word = list(map(str, input().split()))[0];
wordlen = len(word);
list1 = []
count=0
for k in range(h):
    list1 += list(map(str, input().split()))

newlist1=[[list1[i][j]for j in range(h)]for i in range(w)]
newlist2=[[list1[h-j-1][i]for j in range(h)]for i in range(w)]
newlist3=[[list1[j][w-i-1]for j in range(h)]for i in range(w)]

counttot=0

def find(lis):
    compte=0
    for k in lis:
        index=k.index(word)
        while (index>0):
            compte+=1
            index = k.index(word,index+1)
    return compte

count+=find(list1)
count+=find(newlist1)
count+=find(newlist2)
count+=find(newlist3)
print(count)