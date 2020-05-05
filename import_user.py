import collections
import os
import sys
# import 사용시 라이브러리,라이브러리 이런식으로 하는 것보다  import 한줄당 하나씩 해야 가독성이 좋음
# 위에는 표준라이브러리 import임을 나타내고 서드파티는 한줄띄어서 나타내는게 가독성이 좋음


import termcolor  #  서드파티 구분 한줄 띄어서

import lesson_package  ## 다른 회사에서 만들었거나 다른 패키지 임포트시에도 띄어서 구분

import config #내가만든 패키지도 한줄 띄어서 구분


#import 문 순서
#표준라이브러리

#서드파티 라이브러리 알파벳 순서로 묶어서 쓰기

#자기들이 만들거나 회사에서 만든 라이브러리

#로컬 라이브러리

#테스트코드

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)    ##syspath 읽어오는 부분
#__file__을 이용하여 어느경로에 위치해있는지 출력



