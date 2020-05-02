def test_func(x, l=None): #l을 빈리스트로 쓸떄 None설정함 초기화 하는 설정을 해야됨 중복방지를 위해 빈 리스트나 빈사전형은 디폴트인수로는 None으로 써줘야됨
    if l is None:
        l = []
    l.append(x)
    return l

# y = [1,2,3]
# r=test_func(100,y)
# print(r)


# y  = [1,2,3]
# r = test_func(200,y)
# print(r)

r = test_func(100)
print(r)



r = test_func(100)
print(r)


