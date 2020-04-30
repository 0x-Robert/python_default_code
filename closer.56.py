# ##클로저

# def outer(a,b):
     
#     def inner():
#         return a + b

#     return inner
# f = outer( 1,2 )    ## outer (1,2)를 선언한 시점에서 제일 위에 1,2가 들어감 iner함수에 1과 2에 들어감 inner를 실행한게 아니라 f를 실행할때 inner가 처음으로 실행이됨 실행이되면 a와 b가들어감
# print('#####')


# r = f()   ###r에는 f가들어감 
# print(r)



def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

cal1 = circle_area_func(3.14)  ##실행시 pi값에 들어감
cal2 = circle_area_func(3.141592) ##실행시 pi값에 들어감

print(cal1(10))   ##iner함수값 실행됨
print(cal2(10))   ##iner함수값 실행됨

##클로저는 제일처음쓴 인수를 써서 나중에 용도에따라서 다르게쓰고 싶을떄 클로저를 사용함 