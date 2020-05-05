#환경설정에서 python file/settings/project interpreter 에서 플러스버튼누르고 python 서드파티 라이브러리 검색가능
#여기서는 termcolor검색후 설치 연동하는 실습이 있었음
#위에는 파이참 방법n pip install termcolor로도 실행가능

from termcolor import colored

print('test')
print(colored('test','red'))#colored 이용하여 사용 가능
#import termcolor
#pypi 이용해서 서드파티 라이브러리 이용 검색
print(help(colored)) #help로 사용방법 알 수 있음