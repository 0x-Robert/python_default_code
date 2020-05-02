#from lesson_package.tools import utils
from ..tools import utils
#..은 안쓰는것을 추천

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')

#파이썬  파이참에서 tools 메뉴에서 create setup.py로 만들시 배포할 패키지 만들수 있음
#파이참 메뉴 TOOLS/ run setup.py TASK 에서 실행시 tar파일 압축해서 배포가능
#이후 파이참없어도 python setup.py sdist 같은 명령어로 tar압축파일 배포가능