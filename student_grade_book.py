import csv
class Student:
    def __init__(self, first_name, last_name, school_class):
        self.first_name = first_name
        self.last_name = last_name
        self.school_class = school_class
        self.grades = []

    def __str__(self):
        return self.first_name + " " + self.last_name

    def to_dict(self):
        data = {"first_name":self.first_name, "last_name":self.last_name, "class":self.school_class, "grades":";".join(str(grade) for grade in self.grades)}
        return data

    @classmethod
    def from_dict(cls, data):
        student = cls(data["first_name"], data["last_name"], data["class"])
        student.grades = [int(grade) for grade in data["grades"].split(";") if grade]
        return student


class GradeBook:
    def __init__(self):
        self.students = []


    def average_grade(self, first_name, last_name, school_class):
        student = self.find_student(first_name, last_name, school_class)
        if student is not None:
            try:
                median = sum(student.grades) / len(student.grades)
            except ZeroDivisionError:
                print("Student has no grades")
            else:
                print(f"Average grade is {median:.2f}")
        else:
            print("Student not found")

    def find_student(self, first_name, last_name, school_class):
        return next((student for student in self.students if student.first_name == first_name and student.last_name == last_name and student.school_class == school_class), None)

    def show_students(self):
        if self.students:
            for student in self.students:
                print(f"{student.first_name} {student.last_name} {student.school_class}")
        else:
            print("No students")

    def show_grades(self, first_name, last_name, school_class):
        student = self.find_student(first_name, last_name, school_class)
        if student is not None:
            print(", ".join(str(grade) for grade in student.grades))
        else:
            print("Student not found")


    def add_grade(self, first_name, last_name, school_class, grade):
        student = self.find_student(first_name, last_name, school_class)
        if student is not None:
            if 1 <= grade <= 6:
                student.grades.append(grade)
                print("Grade added")
            else:
                print("Invalid grade")
        else:
            print("Student not found")

    def add_student(self, *args):
        for student in args:
            if student:
                self.students.append(student)
                print("Student added")
            else:
                print("Student doesn't exist")

    def save(self):
        with open("students.csv", "w", newline="") as file:
            fieldnames = ["first_name", "last_name", "class", "grades"]
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for student in self.students:
                csv_writer.writerow(student.to_dict())

    def load(self):
        with open("students.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            self.students = [Student.from_dict(student) for student in csv_reader]


def main():
    grade_book = GradeBook()
    try:
        grade_book.load()
    except FileNotFoundError:
        print("No save file available")
    while True:
        print("1. Add student")
        print("2. Add grade")
        print("3. Show grades")
        print("4. Average grade")
        print("5. Show students")
        print("6. Save & Quit")
        choice = input("Enter choice (1-6): ")
        match choice:
            case "1":
                first_name = input("Enter first name: ").capitalize()
                last_name = input("Enter last name: ").capitalize()
                school_class = input("Enter school class: ")
                grade_book.students.append(Student(first_name, last_name, school_class))
            case "2":
                first_name = input("Enter first name: ").capitalize()
                last_name = input("Enter last name: ").capitalize()
                school_class = input("Enter school class: ")
                grade = input("Enter grade (1-6): ")
                try:
                    grade = int(grade)
                except ValueError:
                    print("Enter a whole number")
                    continue
                grade_book.add_grade(first_name, last_name, school_class, grade)
            case "3":
                first_name = input("Enter first name: ").capitalize()
                last_name = input("Enter last name: ").capitalize()
                school_class = input("Enter school class: ")
                grade_book.show_grades(first_name, last_name, school_class)
            case "4":
                first_name = input("Enter first name: ").capitalize()
                last_name = input("Enter last name: ").capitalize()
                school_class = input("Enter school class: ")
                grade_book.average_grade(first_name, last_name, school_class)
            case "5":
                grade_book.show_students()
            case "6":
                grade_book.save()
                break
            case _:
                print("Invalid option")
                continue


if __name__ == "__main__":
    main()
