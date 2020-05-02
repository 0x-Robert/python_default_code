l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words,func):
    for word in words:
        print(func(word))




def sample_func(word):
    return word.capitalize()



def sample_func2(word):
    return word.lower()

#sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize()) #람다를쓸때는?  sample_func1 과2처럼 계속해서 펑션을 늘려야 하기때문에 코드량을 줄이기위해서 씀
change_words(l, lambda word: word.lower()) 

##sample_Func를 인수로 해서 change_words에서 돌려준다

