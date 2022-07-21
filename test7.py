#class complex:
    #def __init__(self,real,imag):
        #self.real=real
        #self.imag=imag

    #def add(self,number):
        #real=self.real+number.real
        #imag=self.imag+number.imag
        #result=complex(real, imag)
        #return result

#n1=complex(2,5)
#n2=complex(-1,7)
#r=n1.add(n2)
#print(r.imag)
#print(r.real)


class triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def perimeter(self):
        p=self.c+self.b+self.a
        return p

t1=triangle(1,2,3)
t2=triangle(4,5,6)
print(t1.perimeter())



