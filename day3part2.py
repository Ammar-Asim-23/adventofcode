def get_num(l, x):
    s = e = x
    while s >= 0 and l[s].isdigit():
        s -= 1
    while e < len(l) and l[e].isdigit():
        e += 1
    return int(l[s + 1 : e])

def get_gears(ls):
    sum = 0
    for y, l in enumerate(ls):
        for x, c in enumerate(l):
            if c == "*":
                s = list(
                    {
                        get_num(ls[i], j)
                        for i in range(max(0, y - 1), min(len(ls) + 1, y + 2))
                        for j in range(max(0, x - 1), min(len(l) + 1, x + 2))
                        if ls[i][j].isdigit()
                    }
                )
                if len(s) == 2:
                    sum += s[0] * s[1]
    return sum



with open('data/day3.txt', 'r') as hd:
    ls = hd.read().splitlines()
    print(get_gears(ls))