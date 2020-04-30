def print_info(func):
    def wrapper(*args , **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


def add_num(a, b ):
    return a + b

print('start')
r = add_num(10,20)
print('end')


print(r)




