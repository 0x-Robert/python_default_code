# #built in 내장함수_파이썬
# #print(globals())
# import builtins
#
# builtins.print()
#
# ranking = {
#     'A': 100,
#     'B': 85,
#     'C': 34
# }
# # ranking.get('A')
#
# print(sorted(ranking, key=ranking.get))  #오름차순
# print(sorted(ranking, key=ranking.get, reverse=True)) #내림차순
#
# #내장함수 https://docs.python.org/ko/3.6/library/functions.html
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#         return True
#
# test = all()
# print(test)

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
    d[c] +=1
print(d)


import lesson_package.talk.animal

#파이썬에서 보통 하는 방법임? 어떤 스크립트라도 이런식으로 로컬에 있을때는 그냥 실행이 되기떄문에 아래와같이 조건문을 설정해고 진행함
#테스트목적에서는 if문 안써도 되지만 다른사람의 패키지를 쓰거나 연동할떄는 if문으로 조건둬야함

def main():
    lesson_package.talk.animal.sing()
    #print('lesson :' , __name__)

if __name__ == '__main__':
    main()

#python library
#