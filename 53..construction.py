# Question: class: triange --> variables: height, base -->function: calculate_area
'''
class triange:
    base = ""
    height = ""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        print("area = ", .5 * self.height *self.base)


t1 = triange(10, 20)
t1.area()
t2 = triange(20, 30)
t2.area()



'''

class square:
    side = ""
    def __init__(self,side):
        self.side = side
    def calculate_area(self):
        print("Area is:", self.side**2)
s1= square(10)
s1.calculate_area()
s2 = square(200)
s2.calculate_area()
s3 = square(23)
s3.calculate_area()

class mobile :
    def call(self):
        print("You can call me")
    def photo(self):
        print("you can take a photo")
    def message(self):
        print("You can message ")
class samsung:
    def call (self):
        print("You can call")
    def message(self):
        print("You can message ")
p = samsung(phone)
p.message()
p.photo()


import students from object_oriented:
halim.display()