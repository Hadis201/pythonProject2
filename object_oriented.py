class students:
    name =""
    roll =""
    gpa = ""
    def display(self):
        print(f"Roll: {self.roll} \nName: {self.name}")

hadis = students()
students.name = "Hadisur Rahman Molla"
students.roll = 5
students.gpa = 3.65
students.display(hadis)

rakib = students
rakib.name = "Rakibul Hasan Molla"
rakib.roll = 3
rakib.gpa = 3.75
students.display(rakib)