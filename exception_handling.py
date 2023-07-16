'''num2 = int(input("please input a number: " ))
result = 34/num2
print(result)
print("Done")'''
'''
trxt = "anisul islam"
print(trxt[-25])
print("done,boih")'''
'''try:
    list = [0,23,3,2,4,5,6]
    result = list[2] / list[9]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("dividing by zero is not possible")
except IndexError:
    print("index error")
'''
'''

def func():
    try:
        numbers = [0, 1, 2, 3, 4, 6]
        result = numbers[45]/ numbers[0]
        print(result)
    except IndexError:
        print("Index Error")
    except ZeroDivisionError:
        print("Do not try to divide something by Zero")
func()

try:
    numbers = [0,1,12,2,3,4,5,6,7,8,9]
    result = numbers[7] / numbers[0]
    print(result)
except ZeroDivisionError:
    print("nothing can be divided by Zero")
except IndexError:
    print("Index Error")
finally:
    print("Ok bois")

try:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    result = numbers[99] / numbers[9]
    print(result)
except IndexError:
    print("Please search in range of index")
except ZeroDivisionError:
    print("No bro, u cannot divide something by zero")
finally:
    print("Nice work guys")

try:
    num1 = int(input("please input the first number"))
    num2 = int(input("please input the 2nd number"))
    result = num1/num2
    print(result)
except (ValueError, ZeroDivisionError):
    print("enter a valid value")
finally:
    print("Thanks")'''

def voter(age):
    if age < 18:
        raise ValueError("Not eligible for voting")
    return "You are allowed to vote"

try:

    print(voter(2))
    print(voter(23))
except ValueError as e:
    print(e)

def voter(age):
    if age < 18:
        raise ValueError("You are not adult ")
    return "You are eligible. Come to the center and.."
try:
    print(voter(444))
    print(voter(12))
except ValueError as e:
    print(e)

#swapping
a = 20
b = 23
a,b = b,a
print("a  b =", a,b)

class Student:
    roll = ""
    gpa = ""
rahim = Student()
print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.65
print(f"Roll : {rahim.roll} , CGPA : {rahim.gpa}")
karim = Student()
print(isinstance(karim,Student))
karim.roll = 102
karim.gpa = 3.92
print(f"Roll : {karim.roll} , CGPA : {karim.gpa}")
anowar = Student()
anowar.roll = 103
anowar.gpa = 3.45
print(f"GPA: {anowar.gpa} , Roll: {anowar.roll}")
print()