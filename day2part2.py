def min_cubes(lines):
    lines = lines.split("\n")
    games = {}
    for i in lines:
        game = i.split(':')
        game_no = int(game[0].split(' ')[1])
        subsets = [i.split(',') for i in game[1].split(';')]     
        bag = []
        for i in subsets:
            subset = {}
            for j in i:
                roll = j.strip().split(' ')
                subset[roll[1]] = int(roll[0])
            bag.append(subset)   
        games[game_no] = bag  
    
    ans = [] 
    
    for i in range(1, len(games)+1):
        red = 0
        blue = 0
        green = 0
        for j in games[i]:
            if 'red' in j.keys():
                if red < j['red']:
                    red = j['red']
            if 'blue' in j.keys():
                if blue < j['blue']:
                    blue = j['blue']
            if 'green' in j.keys():
                if green < j['green']:
                    green = j['green']
        ans.append(red*blue*green)
    print(sum(ans))
    
with open('data/day2.txt', 'r') as hd:
    lines = hd.read()
    min_cubes(lines)                    
                       
        