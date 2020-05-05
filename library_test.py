s = "asdfasdfasdfasdf"

d = {}
for c in s:
    if c not in d:
        d.setdefault(c,0)
        d[c] = 0
    d[c] += 1
print(d)

from _collections import defaultdict
d = defaultdict(int)

for c in s:
    d[c] +=2
print(d)


#python library
