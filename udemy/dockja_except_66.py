#raise IndexError('test Error')

class UppercaseError(Exception):
    pass 


def check():
    words = [ 'APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)              #내가 만든 에러에 대해서 설정후 내가 출력하는 것을 통제 할 수있음 
            #raise ValueError(word)
try:
    check()

except UppercaseError as exc:                       
#except ValueError as exc:
    print('this is my fault . Go Next')