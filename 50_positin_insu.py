def menu(entree, drink, dessert):
    print('entreee = ', entree)
    print('drink =' , drink)
    print('dessert = ' , dessert)

#menu('beef', 'beer', 'ice')
menu(entree='beef', dessert='ice', drink='beer')
menu('beef', dessert='ice', drink='beer')
#함수의 위치에 원하는 위치에 안넣으면 순서에 안맞게 들어갈수있음
#위치인수와 키워드 인수를 섞을때는 순서를 중요하게 봐야됨