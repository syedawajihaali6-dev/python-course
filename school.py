class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"

class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.next_student_id = 1

    def add_student(self, name, grade):
        student = Student(self.next_student_id, name, grade)
        self.students[self.next_student_id] = student
        self.next_student_id += 1
        print(f"Student '{name}' added with ID: {student.student_id}")

    def view_students(self):
        if not self.students:
            print("No students in the system.")
            return
        print("\n--- Student List ---")
        for student_id, student in self.students.items():
            print(student)
        print("--------------------")

    def update_student(self, student_id, new_name=None, new_grade=None):
        if student_id in self.students:
            student = self.students[student_id]
            if new_name:
                old_name = student.name
                student.name = new_name
                print(f"Student ID {student_id} name updated from '{old_name}' to '{new_name}'.")
            if new_grade:
                old_grade = student.grade
                student.grade = new_grade
                print(f"Student ID {student_id} grade updated from '{old_grade}' to '{new_grade}'.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student '{removed_student.name}' with ID {student_id} deleted.")
        else:
            print(f"Student with ID {student_id} not found.")

    def display_menu(self):
        print("\n--- School Management System Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("-------------------------------------")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student name: ")
                grade = input("Enter student grade: ")
                self.add_student(name, grade)
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                try:
                    student_id = int(input("Enter student ID to update: "))
                    if student_id in self.students:
                        print("What do you want to update?")
                        print("a. Name")
                        print("b. Grade")
                        update_choice = input("Enter your choice (a/b): ").lower()

                        if update_choice == 'a':
                            new_name = input("Enter new name: ")
                            self.update_student(student_id, new_name=new_name)
                        elif update_choice == 'b':
                            new_grade = input("Enter new grade: ")
                            self.update_student(student_id, new_grade=new_grade)
                        else:
                            print("Invalid update choice.")
                    else:
                        print(f"Student with ID {student_id} not found.")
                except ValueError:
                    print("Invalid input. Please enter a number for student ID.")
            elif choice == '4':
                try:
                    student_id = int(input("Enter student ID to delete: "))
                    self.delete_student(student_id)
                except ValueError:
                    print("Invalid input. Please enter a number for student ID.")
            elif choice == '5':
                print("Exiting School Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.run()
