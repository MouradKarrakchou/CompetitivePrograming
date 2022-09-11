h, w = list(map(int, input().split()));
word = list(map(str, input().split()))[0];
wordlen = len(word);
list1 = []
for k in range(h):
    list1 += [list(map(str, input().split()))]


# sens est un int entre 0 et 3 qui dit la direction
# 0 : à droite
# 1 : à gauche
# 2 : en bas
# 3 : en haut
def research(x, y, index, sens):
    count = 0
    if (index == wordlen - 1):
        if (list1[y][x] == word[index]):
            return count + 1;
        else:
            return count;
    if (list1[y][x] != word[index]):
        return count;
    else:
        if sens == 0 and x + 1 < w:
            count += research(x + 1, y, index + 1, sens)
        if sens == 1 and x - 1 >= 0:
            count += research(x - 1, y, index + 1, sens)
        if sens == 2 and y + 1 < h:
            count += research(x, y + 1, index + 1, sens)
        if sens == 3 and y - 1 >= 0:
            count += research(x, y - 1, index + 1, sens)
    return count;


count = 0
for y in range(h):
    for x in range(w):
        i = list1[y]
        i2 = list1[y][x]
        if (i2 == word[0]):
            if x + wordlen <= h:
                count += research(x, y, 0, 0)
            if x - wordlen >= 0:
                count += research(x, y, 0, 1)
            if y + wordlen <= w:
                count += research(x, y, 0, 2)
            if y - wordlen >= 0:
                count += research(x, y, 0, 3)

print(count)
