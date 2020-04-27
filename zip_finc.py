days = ['Mon','Tue','Wed']
fruits = ['apple','banana','orange']
drinks = ['coffee', 'tea ', 'beer']


# for i in range(len(days)):
#     print(days[i],fruits[i],drinks[i])

# PS D:\flask> python .\zip_finc.py
# Mon apple coffee
# Tue banana tea
# Wed orange beer

#i가 여러군데쓰이면 헷갈림
#zip함수쓰면 깔끔하게 다 쓸수있음 

for day,fruit,drink in zip(days,fruits,drinks):
    print(day,fruit,drink)

#결과가 똑같음
#day,fruit,drink라는 변수를 이용하여 한방에 줄여줌
PS D:\flask> python .\zip_finc.py                                            \Local\Temp\pip-record-zdl_
Mon apple coffee                                                              --compile --install-header
Tue banana tea                                                               5n2kfra8p0\LocalCache\local
Wed orange bee

days 앞에있는것을 day변수에 넣고
fruits 앞에있는 것을  fruit변수에 넣고
drinks 앞에 있는 것을 drink변수에 넣고
for문 진행
한번에 진행됨