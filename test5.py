class car:
    def x1(self):
        print('this is the class-car')
class vehicle(car):
    def x2(self):
        print('this is the class-vehicle')
class audi(vehicle):
    def x3(self):
        print('this is the class-audi')

a=audi()
a.x1()
a.x2()
a.x3()