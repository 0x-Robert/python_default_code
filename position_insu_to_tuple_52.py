def say_something(word, *args):  #*args를 넣으면 튜플에 넣어줌 
    print('word = ' ,word)       
    for arg in args:
        print(arg)

say_something('HI!', 'Mike', 'Nance')   #앞에들어간 hi만 word에 들어가고 나머지는 args에 들어감


# t = ('Mike', 'Nancy')
# say_something('HI', *t)



