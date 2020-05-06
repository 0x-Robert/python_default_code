def Person(object):
    def __init__(self,name):
        self.name = name

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):   #자기자신에게 엑세스할수있음
        print('run' * num)

person = Person('Mike')
person.say_something()

#del person
#print('######')