def get_result(string):
    lis = string.split('\n')
    digits = []

    for i in lis:
        line = []
        for j in i:
            if j.isdigit():
                line.append(j)
        digits.append(line)        

    numbers = []

    for i in digits:
        numbers.append(int(i[0]+i[-1]))
    
    return sum(numbers)    
    
with open('data/day1.txt', 'r') as hd:
    lines = hd.read()
    
    print(get_result(lines))        