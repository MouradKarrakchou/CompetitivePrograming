myset=set()
Lcons=[]
Lvoy=[]


def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    n = len(string)
    total = n * (n + 1) / 2
    l=[n - i for i in range(n) if string[i] in vowels]
    k = sum([n - i for i in range(n) if string[i] in vowels])
    s = total - k

    if k == s:
        print("Draw")
    elif k > s:
        print(f"Kevin {int(k)}")
    else:
        print(f"Stuart {int(s)}")

if __name__ == '__main__':
    s = input()
    minion_game(s)


