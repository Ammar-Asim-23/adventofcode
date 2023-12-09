def get_scratchcards(cards):
    card_dict = {}
    cards = cards.split('\n')
    points = []
    for i in range(len(cards)):
        card = cards[i].split(':')
        card = card[1].split('|')
        winning_number = card[0].split()
        winning_number = [int(x) for x in winning_number]
        card = card[1].split()
        card = [int(x) for x in card]
        card_dict[i] = [winning_number, card, 1]
        
        
    for i in range(len(card_dict)):
        matching_num=0
        for j in card_dict[i][1]:
            if j in card_dict[i][0]:
                matching_num+=1
        k = 1
        while k <= matching_num:
            card_dict[i+k][2]+=1*card_dict[i][2]
            k+=1
            
    sum = 0
    for i in range(len(card_dict)):
        sum += card_dict[i][2]
        
    return sum    
                    
                


with open('data/day4.txt', 'r') as hd:
    cards = hd.read()
    print(get_scratchcards(cards))