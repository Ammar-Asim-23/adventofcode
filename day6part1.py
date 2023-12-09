def get_permutations(input_string):
    input_string = input_string.strip()
    time, distance = input_string.split('\n')
    time = time.split(':')[1]
    distance = distance.split(':')[1]
    time = [int(x) for x in time.split()]
    distance = [int(x) for x in distance.split()]
    lis = []
    for i in time:
        ways = 0
        j = 0
        while i - j > 0:
            if j * (i-j) > distance[time.index(i)]:
                ways += 1
            j+=1    
        lis.append(ways)
    
    ans = 1
    for i in lis:
        ans *= i 
        
    return ans

with open('data/day6.txt', 'r') as hd:
    races = hd.read()
    print(get_permutations(races))          