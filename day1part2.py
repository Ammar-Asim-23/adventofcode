import re

def calculate_calibration_sum(lines):
    NUMBER_MAP = {
'zero': 0,
'one': 1,
'two': 2, 
'three': 3, 
'four': 4, 
'five': 5, 
'six': 6,
'seven': 7, 
'eight': 8, 
'nine': 9
}
    p = re.compile(r'(?=([0-9]|{0}'.format('|'.join(NUMBER_MAP)) + '))')
    
    first_int = p.findall(lines)[0]
    second_int = p.findall(lines)[-1]
    words = list()
    for word in first_int, second_int:
        if word in NUMBER_MAP.keys():
            words.append(str(NUMBER_MAP[word]))
            continue
        words.append(word)   
    return int(''.join(words))


with open('data/day1.txt', 'r') as hd:
    part_two_answer = sum([calculate_calibration_sum(line) for line in hd.readlines()])
    print(part_two_answer)