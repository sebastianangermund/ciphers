common_words_eng = ['that', 'this', 'with', 'list', 'have', 'from', 'they', 'when',
                    'give', 'find', 'must', 'your', 'time', 'what', 'only', 'were',
                    'more', 'about', 'other', 'first', 'would', 'price',
                    'the', 'and', 'for', 'not', 'are']

with open('brute_force.txt') as f:
    lines = f.readlines()

keep = 'etaoinshrd'

for line in lines:
    count = 0
    for word in line.split(' '):
        if word in common_words_eng:
            count += 1
            print(word)
    print(count)
    print(line)