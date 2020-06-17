"""Controller for speaking with robot"""
from roboter.models import robot
##로보터 패키지/모델에서 robot.py 파일을 임포트하기

###

def talk_about_restaurant():
    """Function to speak with robot"""
    """로봇 함수 출력하는부분 순차 실행"""
    
    print('talk_about_restaurant() ')
    restaurant_robot = robot.RestaurantRobot()

    print('talk_about_restaurant 객체생성 ')
    print('robot.py에서 robot클래스를 상속받은 뒤 hello함수를 실행 후 hello데코레이터와 이어지나?')

    restaurant_robot.hello()
    print('생성된 객체에서 hello함수실행')

    restaurant_robot.recommend_restaurant()
    print('생성된 객체에서 recommend 레스토랑함수 실행')

    restaurant_robot.ask_user_favorite()
    print('생성된 객체에서 유저가 좋아하는 식당찾기 함수 실행')    

    restaurant_robot.thank_you()
    print('레스토랑 로봇 감사인사 ')

