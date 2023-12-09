def get_permutations(input_string):
    input_string = input_string.strip()
    time, distance = input_string.split('\n')
    time = time.split(':')[1]
    distance = distance.split(':')[1]
    time = time.split()
    distance = distance.split()
    t=''
    d=''
    for i in time:
        t+=i
    for j in distance:
        d+=j     
    t = int(t)
    d = int(d)
    ways = 0
    j = 0
    while t - j > 0:
        if j * (t-j) > d:
            ways += 1
        j+=1    
           
    return ways


with open('data/day6.txt', 'r') as hd:
    races = hd.read()
    print(get_permutations(races)) 