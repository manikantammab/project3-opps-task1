class parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return '{} sings {}'.format(self.name,song)
    def dance(self):
        return '{} is now dancing'.format(self.name)
p1=parrot('blu',10)

print(p1.sing('wol'))
print(p1.dance())