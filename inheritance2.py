'''class phone:
    def __init__(self):
        print("I am in 'Phone' class")
        print("I am in 'phone' class")
class samsung(phone):
    def __init__(self):
        super().__init__()
        print("Hello guys")
p = samsung()
print(issubclass(samsung, phone))



class phone:
    def __init__(self):
        print("I have phone, messge, game, etc")
class samsung(phone):
    def __init__(self):
        super().__init__()
        print("I can make video call")
        print("I can also make video upload")


s = samsung()
'''
'''
class shape:
    def __init__(self, dim1, dim2):

        self.dim1 = dim1
        self.dim2 = dim2
    def area(self):
        print("i AM area")
        
'''

class shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    def area(self):
        print("I am the area of the shape class")

class triangle(shape):
    def area(self):
        area = 0.5*self.dim2*self.dim1
        print("Area of triangle", area)

class rectangle(shape):
    def area(self):

        area = self.dim1 * self.dim2
        print("Area of triangle", area)
t1 = triangle(10, 12)
t1.area()


r1 = rectangle(10101, 10101)
r1.area()

class shape:
    def __init__(self, dim2, dim1):
        self.dim1 = dim1
        self.dim2 = dim2
        print("SHapes:")
class rectangle(shape):


    def area(self):
        print ("Area is ", self.dim2 * self.dim1)

class triangle(shape):
    def area(self):
        print("Area of triangle is ", .5 * self.dim1 * self.dim2)
        super().shape()
r1 = rectangle(10,12)
r1.area()
t1 = triangle(100,29)
t1.area()




