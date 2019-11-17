# Write your code here!

class Member:
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi, my name is {self.full_name}!")
    

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason


class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, val):
        self.skills.append(val)
        print(f"{val} added as a skill to {self.full_name}")

class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
    
    def add_participant(self, val):
        if isinstance(val, Student):
            self.students.append(val)
            print(f"{val.full_name} added to Students")
        elif isinstance(val, Instructor):
            self.instructors.append(val)
            print(f"{val.full_name} added to Instructors")
        else:
            print("Not a valid participant")

    def print_details(self):
        print("=>")
        print(f"Workshop - {self.date} - {self.subject}")
        print("\n")
        print("Students")
        for student in self.students:
            print(f"{student.full_name} - {student.reason}")
        print("Instructors")
        for instructor in self.instructors:
            print(f"{instructor.full_name} - {instructor.skills}")
            print(f"{instructor.bio}")

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()