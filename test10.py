class parrot:
    def fly(self):
        print('parrot can fly')
    def swim(self):
        print('parrot can not swim')
class penguin:
    def fly(self):
        print('penguin can not fly')
    def swim(self):
        print('penguin can swim')
def flying_test(bird):
    bird.fly()

p1=parrot()
p2=penguin()
p1.swim()
p2.fly()
flying_test(p1)
flying_test(p2)