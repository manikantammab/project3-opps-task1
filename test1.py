#Task 6
#for all the concepts that we have discussed is our class point you have to write altleast 10 examples
 #   you have to make sure that use ineuron students,class,class type,number of courses
#,attributtes,blog,internship,jobs as reference example
class company:
    def __init__(self,name,employes_no,branch,course_name):
        self.name=name
        self.employes_no=employes_no
        self.branch=branch
        self.course_name=course_name

c1=company('ineuron',300,'ML','data science')
c2=company('tcs',1000,'AL','web developer')

print(c1.branch)
print(c2.employes_no)
print(c2.course_name)
