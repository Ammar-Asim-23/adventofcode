def get_points(cards):
    cards = cards.split('\n')
    points = []
    for card in cards:
        card = card.split(':')
        card = card[1].split('|')
        winning_number = card[0].split()
        winning_number = [int(x) for x in winning_number]
        card = card[1].split()
        card = [int(x) for x in card]
        point = 0
        for number in card:
            if number in winning_number:
                point+=1
        points.append(point)
    return sum([2**(point-1) if point > 0 else 0 for point in points])




with open('data/day4.txt', 'r') as hd:
    cards = hd.read()
    print(get_points(cards))