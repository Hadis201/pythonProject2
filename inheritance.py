#multilevel inheritance(goes from a to b and also from b to c)
''' class A:
    def display1(self):
        print("This is A class")
class B(A):
    def display2(self):
        print("This is B class")
class C(B):
    def display3(self):
        print("This is C class")
class D(C,A):#this is multiple class inheritance
    def display4(self):
        super().display2()
        super().display1()
        super().display3()
        print("This is D class")


d = C()
d.display3()
d.display2()
d.display1()
# this does not belong to the C class d.display4()

d = D()
d.display4()

'''
'''
# Multiple inheritance
class X:
    def display(self):
        print("This belongs to X")
class Y:
    def display(self):
        print("This belongs to Y")

class Z(X,Y):
    
    pass

ziiii = Z()
ziiii.display()

'''
'''
# abstraction
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        print("There is no area ")
class rectangle(shape):
    def __init__(self, width, height):
        self.width = witdth
        self.height = height

    def area(self):
        print( "the area is ", self.width* self.height)
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print( 3.14 * self.radius ** 2 )

circle1 = circle(10)
circle1.area()
'''


from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        print("shape does not really have area")
class rectangle(Shape):
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    def area(self):
        print("The area is ", self.d1* self.d2)
r1 = rectangle(10,12)
r1.area()

#class circle(Shape):

