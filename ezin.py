# python 이진수 함수 이용하여 정수를 이진수로 변경 하는 함수만들가
# 파이썬은 정수를 이진수로 바꿔주는 개꿀함수가 있습니다

# 바로  bin함수인데요

#-------------파이썬 공식문서-------
#https://docs.python.org/ko/3/library/functions.html
# bin(x)
# 정수를 《0b》 가 앞에 붙은 이진 문자열로 변환합니다. 결과는 올바른 파이썬 표현식입니다. x 가 파이썬 int 객체가 아니라면, 정수를 돌려주는 __index__() 메서드를 정의해야 합니다.
#  몇 가지 예를 들면:

>>>
bin(3)
'0b11'
bin(-10)
'-0b1010'


파이참에서 한번 실행해보시거나 visualstudiocode에서 test.py를 만드시고
python test.py 를 실행하시면 됩니다.
visualstudio에서는 python .\test.py 형식으로 실행됩니다.

a1=bin(45)
a2=bin(25)
a3=bin(23)

print(a1)
print(a2)
print(a3)
결과는 파이썬 실행후에 3초후에 나옵니다.

# 그런데 이렇게 계속 변수를 넣어서 실행하는 것은 귀찮죠?
# 입력하는 숫자를 이진수로 바꿔주는 함수를 만들어볼까요?

def like_bin_func():  #def로 함수정의 
    b = int(input())  #b 라는 변수에 int()함수로 감싼 input함수를 넣어줍니다 int()는 ()안에 숫자로 바꾸는 함수구요 input()은 입력값을 받는 함수입니다. 공부를 위해서는 int()와 input()함수를 구글링!
    c = bin(b) #c라는 변수에 bin()함수를 대입하고 b라는 값을 넣습니다
    print(c) #c를 출력하는 print()함수실행

#결과는?
like_bin_func()  #입력하는 숫자를 이진수로 변환해주는 함수실행



# 대신 결과값이 <0b>가 붙은 이진문자열로 나옵니다. 이결 없애기 위해서는??

# 파이썬에 format 함수가 있었네요

---------------------------------------------------------------------------------------

def like_bin_func2():
    b = int(input())
    c = bin(b)
    print(c)                 ###여기까진 위의 함수와같습니다. ob가 표현되지만 그다음부터는?
    d = format(bin(b)[2:])   ###format이라는 함수안에 bin(b)를 넣고 [2:] 파이썬에 슬라이스라는 기능을 이용해보면??
    print(d)                   

like_bin_func2()

---------------------------------------------------------------------------------------
사용된 파이썬 내장함수
python 프롬프트창을열어보세요 윈도우 창을열고 python 검색후 커맨드창이 뜨면 밑에 명령이를 테스트 해보세요
---------------------------------------------------------------------------------------
int() 

>>> a='324'
>>> b=int(a)
>>> b
324
>>> type(b)
<class 'int'>

---------------------------------------------------------------------------------------

input()
>>> c=input()
234
>>> c
'234'
>>> type(c)
<class 'str'>
---------------------------------------------------------------------------------------

format()
>>> d=234234234
>>> e=format(d[2:])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> e = format(d[2:])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not subscriptable
>>> f=str(d)
>>> e = format(f[2:])
>>> e
'4234234'


---------------------------------------------------------------------------------------
파이썬의 개꿀함수 slice함수
list_like_bin이름은 임의로 생성한 리스트

list_like_bin = [1,3,4,5,6,7,8,]
list_like_bin[0:2]
list_like_bin[0]부터 list_like_bin[1] 까지 잘라 줍니다
list_like_bin[2:]
list_like_bin[0]부터 list_like_bin[1] 이후 숫자까지 출력해줍니다

