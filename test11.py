class human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def description(self):
        print('my name is {} i am a {}'.format(self.name,self.gender))
class girl(human):
    def schoolName(self,schoolname):
        print('i study in schoolname {}'.format(schoolname))

h=girl('lily',30,'girl')
h.description()
h.schoolName('abc')
