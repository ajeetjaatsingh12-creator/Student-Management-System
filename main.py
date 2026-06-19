class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(
            f"id: {self.student_id}, name: {self.name}, age: {self.age}, marks: {self.marks}"
        )


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("enter student id:")

        for student in self.students:
            if student.student_id == student_id:
                print("student id already exists!")
                return

        name = input("enter student name:")
        age = int(input("enter age:"))
        marks = float(input("enter marks:"))

        new_student = Student(student_id, name, age, marks)
        self.students.append(new_student)
        print("student added successfully!")

    def view_student(self):
        if not self.students:
            print("no student records found.")
            return

        print("\nstudent records:")
        for student in self.students:
            student.display()

    def search_student(self):
        student_id = input("enter student id to search:")

        for student in self.students:
            if student.student_id == student_id:
                print("student found:")
                student.display()
                return

        print("student not found.")

    def update_marks(self):
        student_id = input("enter student id:")

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("enter new marks:"))
                student.marks = new_marks
                print("marks updated successfully!")
                return

        print("student not found.")

    def delete_student(self):
        student_id = input("enter student id to delete:")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("student deleted successfully!")
                return

        print("student not found.")

    def highest_marks_student(self):
        if not self.students:
            print("no student record available")
            return

        top_student = max(self.students, key=lambda student: student.marks)
        print("\nstudent with highest marks:")
        top_student.display()

    def menu(self):
        while True:
            print("\n===== student management system =====")
            print("1. add student")
            print("2. view all student")
            print("3. search student")
            print("4. update student marks")
            print("5. delete student")
            print("6. display highest marks student")
            print("7. exit")

            choice = input("enter your choice:")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_student()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_marks()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                self.highest_marks_student()
            elif choice == "7":
                print("exiting student management system...")
                break
            else:
                print("invalid choice! please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.menu()
              
      