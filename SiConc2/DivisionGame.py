def raisin(n):
    if n == 0:
        return False
    if (not raisin((n - 1) // 2)) or (not raisin((n - 1) //  3)) or (not raisin((n - 1) //  7)):
        return True
    else:
        return False

if raisin(int(input())):
    print("First player")
else:
    print("Second player")
