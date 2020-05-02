# # #from lesson_package.utils import say_twice
# # from lesson_package.talk import human
# # from lesson_package.talk import animal
# # from lesson_package.talk import  *
# #
# #
# #
# # print(animal.sing())
# # print(animal.cry())
# #
# #
# #
# # # r = utils.say_twice('hello')
# #
# # #print(r)
# # ##모듈에서 불러오는 것이 충돌도 막고 분리해서 구분하기 좋음
# # ##풀패스를 쓰는것을 요청하는 회사도있음
# # # as u 도써도 되지만 추천하지
# # # 는 않음
# #
# # print(human.sing())
# # print(human.cry())
#
#
# try:
#     from lesson_package import  utils
# except ImportError:
#     from lesson_package.tools import utils
#
# utils.say_twice('word')



