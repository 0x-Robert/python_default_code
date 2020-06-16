# ##Stack

# stk =[]
# stk.append(1)
# stk.append(2)
# print(stk)
# print(stk.pop())
# print(stk.pop())



"""stack은 쌓는다는 의미처럼
먼저들어간 항목이 나중에 나오고 나중에 들어간 항목이 먼저나오는 의미"""


class stack:
    """stack을 클래스로 구현후 객체생성을 통해 stack의 원리를 파악하는 클래스"""
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return not self.items

stk = stack() #stack 객체를 생성 stack클래스에서 객체를 생성하는 뜻
print(stk)    #stack object 생성 확인
print(stk.isEmpty())  #아무것도 없을떄는 True 있을때는 False
stk.push(1)   #stk에 1을 넣음
stk.push(2)   #stk에 2을 넣음
print(stk.pop())   #stk에 2를 뺌 
print(stk.pop())   #stk에 1을 뺌
print(stk.isEmpty()) ##객체에는 아무것도 없음 True출력