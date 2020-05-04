#built in 내장함수_파이썬
#print(globals())
import builtins

builtins.print()

ranking = {
    'A': 100,
    'B': 85,
    'C': 34
}
# ranking.get('A')

print(sorted(ranking, key=ranking.get))  #오름차순
print(sorted(ranking, key=ranking.get, reverse=True)) #내림차순

#내장함수 https://docs.python.org/ko/3.6/library/functions.html

def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True

test = all()
print(test)