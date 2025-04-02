class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def print_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student roll number: {self.roll_number}")
        print(f"Student grade : {self.grade}")

student1 = Student("Kags", 22, "A+")
student2 = Student("Rishita", 20, "A2")

students = [student1, student2]

for student in students:
    student.print_details()