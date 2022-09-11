list = list(map(str, input().split()));


def lumcoul(inp):
    R = int(inp[1] + inp[2], 16)
    G = int(inp[3] + inp[4], 16)
    B = int(inp[5] + inp[6], 16)
    return (0.2126 * R + 0.7152 * G + 0.0722 * B)


list.sort(key=lambda k: lumcoul(k))

print(list[int(len(list)/2)])