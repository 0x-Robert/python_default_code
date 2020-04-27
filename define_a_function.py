# #함수 정의하기
# def say_something(): #함수를 정의하다
#     s = 'hi'
#     return s

# # print(type(say_something))
# # python .\define_a_function.py
# # <class 'function'>


# result =say_something()
# print(result)



#함수 정의하기
def say_something(): #함수를 정의하다
    s = 'hi'# hi를 s에 담고 #s라는 변수를 넣어서 작동
    return s #s를 리턴해주고

# # print(type(say_something))
# # python .\define_a_function.py
# # <class 'function'>


result =say_something()
print(result)


#인수 작동방식

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
          return 'green pepper'
    else:
        return "i don't know"

result = what_is_this('green')
print(result)
result = what_is_this('red')
print(result)
