class employee:
    def __init__(self,id,salary,bonus):
        self.id=id
        self.salary=salary
        self.bonus=bonus
        self.f1=self.facility()

    def employee_details(self):
        print(self.id,self.salary,self.id)
    class facility:
        def __init__(self):
            self.pf=5000
            self.travel=20000
        def show(self):
            print(self.pf,self.travel)



e1=employee(1,30000,2000)
e2=employee(2,30000,2000)
print(e1.id)
e1.employee_details()
e1.f1.show()
print(e2.f1.travel)
