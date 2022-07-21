class car:
    def x1(self):
        print('this is the base class-car')

class vehicle:
    def x2(self):
        print('this is the base class-vehicle')

class audi(car,vehicle):
    def x3(self):
        print('this is a derived class-audi')

a1=audi()
a1.x3()
a1.x2()
a1.x1()