def g():
    for i in range(10):
        yield i

g = g()

# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


g = tuple(i for i in range(10) if i % 2 == 0)
# print(type(g))
# print(g)


for x in g:
    print(x)


    ##제너레이터도 한줄로 내포하는방법