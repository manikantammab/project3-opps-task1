class shape:
    def no_of_sides(self):
        pass
    def two_dimensional(self):
        print( 'i am a 2d object.i am from shape class')
class square(shape):
    def no_of_sides(self):#method overiding
        print('i have 4 sides.i am from square class')
class triangle(shape):
    def  no_of_sides(self):#method overiding
        print('i have 3 sides.i am from triangle class')

sq=square()
sq.no_of_sides()
t=triangle()
t.no_of_sides()