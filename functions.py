''' def func():
    print("hello guys")
func()
def add(a,b,c):
    sum=a+b+c
    print("sum is", sum)
add(1,2,23)

def addition(a,b,c,d):

    sum = a+b+c+d
    return sum


result = addition( int(input("the value of a:")), int(input("the value of b:")), int(input("the value of c:")), int(input("the value of d:")))
print ("take your result ", result)
'''


'''
def large(a,b,c):
    if a>b and a>c:
        print(a, "is the largest number")
    elif b>a and b>c:
        print(b, "is the largest number")
    else:
        print(c, "is the largest number")
large(1,00,2)

'''
'''

'''
"""
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

haddu = largest
print (haddu(1,12,13))

def even_odd (a):
    if a%2 == 0:
        print (a, "is a even number")
    else: print(a, "is a odd number")
even_odd(23)
"""

'''
import math
def prime_number(a):

    if a<2:
        print (a, "this is not a prime number")
    for i in range(2, int(math.sqrt(a)), 1):
        if a%i==0:


            print(a, "is  not a prime number")
    
        print(a, "is a prime number")

prime_number(12)
'''
'''def student(id, name, gpa):
    print(id, name, gpa)
student(101, "hadu", 3.57)
'''
'''def student(*details):
    print(details[2])
student(101, "jadu", 3.45)
student(102, "jafor", 1913223606)
'''
'''
def add(*numbers):
     sum=0
     for num in numbers:
         sum=sum+num
     print(sum)
add(10,20)
add(10,12,1000,1122333333)

def add (*number):
    sum=0
    for num in number:
        sum = sum+num
    print(sum)

add(100,200,300,400,500)
add(10,20,30,40,50)

def student(id, name):
    print(id)
student(id = 101,name= "rakibul hasan")
def student(**details):

    print(details["id"])


student(id = 1001, name='hadisur rahman')
student(id = 1002, name='rakibul hasan')
student(id = 1003, name='mahzabin')
student(id = 1004, name='moudud ahmed')
''' '''
def add (*number):
    sum = 0
    for num in number:
        sum = sum +num
        return sum
print(add(100,200,300,400,500,600))

def calculate(a,b):
    return a**2 + 2*a*b + b**2
print(calculate(1,2))


a =(lambda a,b : a**2 + 2*a*b + b**2)(1,2)
print (a)
print((lambda a,b: (a+b)*(a+b) ) (1,2))

def cube(a):
    print(a**3)
cube(1222222222222222222222222222222)

x= (lambda a: a**3)(3)
print(x)'''

'''def square(x):
    return x**2
num = [1,2,3,4,5,6,7,345555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555]
result = list(map(square, num))
print(result)'''


'''def square(x):
    return x^3
num = [1,2,3,4,5,6,7,899]
result = list(map(square, num))
print (result)'''
'''nums = [1,2,3,4,56,7]
results = list(filter(lambda x: x%2==0, nums))
print(results)
'''

num = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x: x**2, num))
print(result)

num = [1,2,34,4,5,6,2,3]
result = list(filter(lambda x: x%2 ==0, num))
print(result)

num = [1,2,3,4,55,6,677,7]
result = list([x%2==0 for x in num])
print(result)

num = [1,2,23,4,45,6,45]
result = list(filter(lambda x: x%2==0, num))
print(result)

num = [1,23,3,4,5,6,73,3,4,3,2]
result = [x for x in num if x%2==0]
print(result)

roll = [101,102,103,104]
name = ["anis", "rakib", "zebin","moudud"]
print(list(zip(roll, name)))

roll = [1,2,3,4,5,6]
name = ["moudud", "jebin", "rakib", "hadis", "anis", "nice"]
cgpa =[3.90, 3.45, 3.56, 3.23, 3.34, 3.65]
x = list(zip(roll, name, cgpa,"123456"))
print(x)

def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

print(fact(4))