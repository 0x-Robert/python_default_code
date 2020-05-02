w = ['mon', 'tue', 'wed']
f = ['coffee', ' milk', 'water']


d = {}
for x,y in zip(w,f):
    d[x]=y

print(d)
d = {x:y for x,y in zip(w,f)} #위에있는 for문 과같음 사전형도 사전안에 내포표기가 가능
print(d)

