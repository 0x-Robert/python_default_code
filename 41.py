while True:
    word = input('Enter:')      #word 변수에 input 사용자입력값을 받는다
    num = int(word)             #num 변수에 word변수를 int정수형으로 변환한 값을 대입한다.
    if num == 100:              #num이 100일 경우 
                                #종료
        break                   #num이 100이아닐경우 next출력
    print('next')
