t = (1,2,3,4,5)
t2 = (5,6,7,8,9,10)

r = [ ]
for i in t:
    if i % 2 ==0:
         r.append(i)


r = [i for i in t if 1 % 2 ==0] #이런식으로 쓰는 이유는 메모리를 안쓰는 것도 있꼬 일부러 append를 안해도되서 처리가 빠르다는 장점이 있음 짧은 for문은 리스트안에서 쓰는 방법이 있음

print(r)


#리스트 내포표기 




r = []
for i in t:
    for j in t2:
        r.append(i*j)

print(r)

r = [ i * j for i in t for j in t2] #위의 for문과 동일한 효과 리스트안에 for문을 쓰는 방법 
print(r)