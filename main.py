import pickle
import os

class Student:
    def __init__(self, roll_number, name, age, course, gender, guardian_name, address):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.course = course
        self.gender = gender
        self.guardian_name = guardian_name
        self.address = address

    def __str__(self):
        return (
            f"\nRoll Number : {self.roll_number}\n"
            f"Name        : {self.name}\n"
            f"Age         : {self.age}\n"
            f"Course      : {self.course}\n"
            f"Gender      : {self.gender}\n"
            f"Guardian    : {self.guardian_name}\n"
            f"Address     : {self.address}\n"
        )

class StudentManager:
    FILE_NAME = "students.pkl"

    def __init__(self):
        self.student_list = self.load_data()

    def save_data(self):
        with open(self.FILE_NAME, "wb") as f:
            pickle.dump(self.student_list, f)

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "rb") as f:
                return pickle.load(f)
        return []

    def add_student(self):
        try:
            roll = int(input("Enter Roll Number: "))
            if any(s.roll_number == roll for s in self.student_list):
                print("❌ Roll number already exists!")
                return

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            gender = input("Enter Gender: ")
            guardian = input("Enter Guardian Name: ")
            address = input("Enter Address: ")

            student = Student(roll, name, age, course, gender, guardian, address)
            self.student_list.append(student)
            print("✅ Student added successfully.")
        except ValueError:
            print("❌ Invalid input. Please enter correct details.")

    def view_students(self):
        if not self.student_list:
            print("⚠️ No students found.")
            return
        print(f"Total Students: {len(self.student_list)}")
        for student in sorted(self.student_list, key=lambda s: s.roll_number):
            print(student)

    def search_student(self):
        print("Search by: 1. Roll Number  2. Name")
        try:
            opt = int(input("Enter choice: "))
            if opt == 1:
                roll = int(input("Enter Roll Number: "))
                for s in self.student_list:
                    if s.roll_number == roll:
                        print(s)
                        return
                print("❌ Student not found.")
            elif opt == 2:
                name = input("Enter Name: ").lower()
                found = False
                for s in self.student_list:
                    if name in s.name.lower():
                        print(s)
                        found = True
                if not found:
                    print("❌ Student not found.")
            else:
                print("❌ Invalid option.")
        except ValueError:
            print("❌ Invalid input.")

    def update_student(self):
        try:
            roll = int(input("Enter Roll Number to update: "))
            for s in self.student_list:
                if s.roll_number == roll:
                    s.name = input("Enter new name: ") or s.name
                    try:
                        age_input = input("Enter new age: ")
                        if age_input: s.age = int(age_input)
                    except ValueError:
                        print("⚠️ Age not updated. Invalid input.")

                    s.course = input("Enter new course: ") or s.course
                    s.gender = input("Enter new gender: ") or s.gender
                    s.guardian_name = input("Enter new guardian name: ") or s.guardian_name
                    s.address = input("Enter new address: ") or s.address
                    print("✅ Student updated successfully.")
                    return
            print("❌ Student not found.")
        except ValueError:
            print("❌ Invalid input.")

    def delete_student(self):
        try:
            roll = int(input("Enter Roll Number to delete: "))
            for i, s in enumerate(self.student_list):
                if s.roll_number == roll:
                    del self.student_list[i]
                    print("✅ Student deleted successfully.")
                    return
            print("❌ Student not found.")
        except ValueError:
            print("❌ Invalid input.")

    def run(self):
        while True:
            print("\n--- Student Management System ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '0':
                self.save_data()
                print("👋 Exiting and saving data...")
                break
            else:
                print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    StudentManager().run()
