def game_possibility(lines):
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
        
        indices = []
        red = 12
        green = 13
        blue = 14
        
        for i in range(1, len(games)+1):
                game = games[i]
                valid = True
                for j in game:
                    if 'blue' in j.keys():    
                        if int(j['blue'] or 0) > blue:
                            valid = False
                    if 'red' in j.keys():     
                        if int(j['red'] or 0) > red:
                            valid = False
                    if 'green' in j.keys(): 
                        if int(j['green'] or 0) > green:
                            valid = False
                if valid:
                    indices.append(i)
    print(sum(indices))       
                             

with open('data/day2.txt', 'r') as hd:
    lines = hd.read()
    game_possibility(lines)
       