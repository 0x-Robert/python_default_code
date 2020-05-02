l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)


print("################")


def counter(num=10):
    for _ in range(num):
        yield 'run'



def greeting():
    yield 'Good morning'
    # for i in range(100000):
    #     print(i)
    yield 'Good afternoon'
    # for i in range(100000):
    #     print(i)
    yield 'Good night'


## yield 실행전에 for문을 많이 돌려야 한다던지 하는 상황에서 제너레이터를 쓰는것이 편리함
##반복문을 다돌리고 실행하는 것이아니라 조금씩 분할해서 사용할떄 제너레이터를 사용함
# for g in greeting():
#     print(g)


g = greeting() # g: generator object greeting at 0x105d8d410
c = counter()
print(next(g)) #첫번째값 출력


print(next(c)) #두번째값 출력
print(next(c))
print(next(c))
print(next(c))
print(next(c))


print(next(g))

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(g))  ## yiled문이 3개밖에 없기떄문에 이이상 출력할 값이 없을때는 stopIteration
