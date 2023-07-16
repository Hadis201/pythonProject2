'''class students:

    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa  = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")



rahim = students()
rahim.set_value("101", '3.99')
rahim.display()


karim = students()
karim.set_value("102", "4.00")
karim.display()

halim = students()
halim.set_value("103", '4.22')
halim.display()

dalim = students()
dalim.set_value('104', '6.22')
dalim.display()

ovi = students()
ovi.set_value('105', '7.22')
ovi.display()
'''
class students:
    roll = ""
    name = ""
    cgpa = ""
    passing_year = ""
    baper_nam = ""
    def __init__(self, roll, name,  cgpa, passing_year, baper_nam):
        self.roll = roll
        self.name =name
        self.cgpa = cgpa
        self.passing_year = passing_year
        self.baper_nam = baper_nam
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll} , CGPA: {self.cgpa}, Passing Year: {self.passing_year}, Baper nam:{self.baper_nam}")

rahim = students(191,"rahim", 2,2222, "Abdul Aziz")
rahim.display()
karim = students(191, "Abdul Karim", 2.45,2011, "Abdul Aziz")
karim.display()
halim = students(192, "Abdul Halim", 4.00, 1999, "Tasen Molla")
halim.display()

