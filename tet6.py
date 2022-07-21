class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def check_pass_fail(self):
        if self.marks>=40:
            return True
        else:
            return False
s1=student('henry',70)
print(s1.check_pass_fail())
s2=student('bunny',30)
print(s2.check_pass_fail())
print(s1.name)
print(s1.marks)
print(s2.name)
print(s2.marks)