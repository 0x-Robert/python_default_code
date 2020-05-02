def print_more(func):
    def wrapper(*args , **kwargs):
        print('func: ', func.__name__)
        print('args: ', args)
        print('kwargs:' , kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args , **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_more
@print_info
#@print_more

def add_num(a, b ):
    return a + b

# print('start')
# r = add_num(10,20)
# print('end')

# r = add_num(10,20)
# print(r)
f = print_info(print_more(add_num))   ##print_more을 print_info로 포괄을하는 식으로 인식하기
r = f(10,20)
print(r)
##데코레이터는 감싸준다 포괄한다는 의미로 보기 
##print_more과 print_info두개 다쓰고 실행을하면 출력순서가 바뀌어서 나옴





# @print_info
# def sub_num(a, b ):
#     return a - b