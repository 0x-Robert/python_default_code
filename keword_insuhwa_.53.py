# def menu(**kwargs):  ##keoword args의 줄임말
#    # print(kwargs)
#     for k,v in kwargs.items():  #for문으로 keyword랑 value값을 넣어주면 값을 같이 출력
#         print(k,v)
# #menu(entree='beef', drink='coffee')    #

# d = {
#     'entree' : 'beef',
#     'drink' : 'ice coffee',
#     'dessert' : 'ice'

# }
# menu(**d)  ##  **두개를 붙이면 d 딕셔너리가 위에처럼 전개되어서 menu()로 넘어가고 넘어간 상태에서 **kwargs 사전형 딕셔너리형이 되어서 for문 실행시 출력됨


#위치인수랑 사전형이랑 튜플 같이쓰는것도가능

def menu(food, *args, **kwargs):  ##keoword args의 줄임말 
     print(food)                    ## * ** 두개에 대한 순서가 중요 *args, **kwargs 순서 바꾸면 신택스에러나옴
     print(args)
     print(kwargs)


menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

