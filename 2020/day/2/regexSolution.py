import re
from collections import Counter

with open('a.input.txt', 'r') as f:
    valid = 0
    line = f.read().splitlines()
    print(line)
    for i in line:
        x = '1-3 a: aabbbcc'
        print(i)
        y = re.split('(\d+)-(\d+) ([a-z]): (.*)',i)
        s,e,c,p = list(filter(None, y))
        occurances = Counter(p)[c]
        if int(s) <= occurances and int(e) >= occurances:
            valid+=1
    print(valid)





