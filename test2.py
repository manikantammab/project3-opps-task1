class employee:
    def __init__(self,id,salary,bonus):
        self.id=id
        self.salary=salary
        self.bonus=bonus
    def display_details(self):
        print(self.id,self.salary,self.bonus)

e1=employee(1,40000,1000)
e1.display_details()
e2=employee(2,70000,5000)
print(e2.salary)
e2.display_details()
