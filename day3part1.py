def sum_parts(ls):
    sum = 0
    for y, l in enumerate(ls):
        x = 0
        while x < len(l):
            numlen = 0
            if ls[y][x].isdigit():
                while x < len(l) and ls[y][x].isdigit():
                    numlen += 1
                    x += 1
                num = int(l[x - numlen : x])
                if any(
                    c not in "1234567890."
                    for i in range(max(0, y - 1), min(len(ls), y + 2))
                    for c in ls[i][max(0, x - numlen - 1) : min(len(l), x + 1)]
                ):
                    sum += num
            else:
                x += 1
                
    return sum    

with open('data/day3.txt', 'r') as hd:
    ls = hd.read().splitlines()
    print(sum_parts(ls))