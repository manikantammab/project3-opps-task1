class human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def description(self):
        print('my name is {} , i am a {}'.format(self.name,self.gender))
    def dance(self):
        print('i can dance')
class girl(human):
    def dance(self):
        print('i can do classic dance')
    def activity(self):
        super().dance()#super class
g=girl('lily',20,'girl')
g.description()
g.activity()