#사전을 for문으로 처리하기 방식
#사전정의
#  d= { 'x': 100, 'y': 200}
# for v in d:
#     print(v)
    #이건키만 나옴

#키와 밸류 모두 나오게끔할려면 사전형에는 items()라는 메소드가 있음
#k라는 변수에 키값이 들어가고 v라는 변수에 값이 들어감
# d = { 'x': 100, 'y': 200}
# for k , v in d.items():
#     print(k, ':', v)

#띄어쓰기 오류 IndentationError: unexpected indent
#결과값 나옴
# PS D:\flask> python .\dic_to_for.py
# x : 100
# y : 200



#사전형의 loop는 많이사용

d = { 'x': 100, 'y': 200}
print(d.items())

#실행하면 dict_items에 튜플형으로 들어가있음 리스트가 되어있고
#d.itmes가 아래와 같은 값을 갖고온다
#dict_items([('x', 100), ('y', 200)])


