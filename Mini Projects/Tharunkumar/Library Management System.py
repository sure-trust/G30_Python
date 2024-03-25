import csv
import os

class Library:
    def __init__(self):
        self.books_file = r'C:\Users\tharu\Downloads\books.csv'
        self.students_file = r'C:\Users\tharu\Downloads\students.csv'
        self.books = []
        self.students = []
        self.load_data() 

    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.books = list(reader)
        if os.path.exists(self.students_file):
            with open(self.students_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.students = list(reader)

    def save_data(self):
        with open(self.books_file, mode='w', newline='') as file:
            fieldnames = ['id', 'title', 'copies']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.books)

        with open(self.students_file, mode='w', newline='') as file:
            fieldnames = ['id', 'name']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.students)

    def create_student_account(self, student_id, name):
        if not any(student['id'] == student_id for student in self.students):
            self.students.append({'id': student_id, 'name': name})
            self.save_data()
            print(f"Student account created successfully for {name}.")
        else:
            print("Student ID already exists.")

    def remove_student_account(self, student_id):
        self.students = [student for student in self.students if student['id'] != student_id]
        self.save_data()
        print("Student account removed successfully.")

    def create_library_account(self, book_id, book_title, copies):
        if not any(book['id'] == book_id for book in self.books):
            self.books.append({'id': book_id, 'title': book_title, 'copies': copies})
            self.save_data()
            print(f"Library account created successfully for {book_title}.")
        else:
            print("Book ID already exists.")

    def remove_library_account(self, book_id):
        self.books = [book for book in self.books if book['id'] != book_id]
        self.save_data()
        print("Library account removed successfully.")

    def show_available_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                print(f"Book ID: {book['id']}, Title: {book['title']}, Copies available: {book['copies']}")
        else:
            print("No books available in the library.")

    def show_available_students(self):
        if self.students:
            print("Available students:")
            for student in self.students:
                print(f"Student ID: {student['id']}, Name: {student['name']}")
        else:
            print("No students available.")

# Add more methods as needed...

# Main program
library = Library()

def print_centered(text, width=80):
    print(text.center(width))

while True:
    print()
    print_centered("Library Management System")
    print_centered("\nChoose menu:")
    print_centered("1. Create Student Account")
    print_centered("2. Remove Student Account")
    print_centered("3. Create Library Account")
    print_centered("4. Remove Library Account")
    print_centered("5. Show all available books in library")
    print_centered("6. Show all available students")
    print_centered("7. Issue Book")
    print_centered("8. Submit Book")
    print_centered("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        library.create_student_account(student_id, name)
    elif choice == '2':
        student_id = input("Enter Student ID to remove: ")
        library.remove_student_account(student_id)
    elif choice == '3':
        book_id = input("Enter Book ID: ")
        book_title = input("Enter Book Title: ")
        copies = int(input("Enter Number of Copies: "))
        library.create_library_account(book_id, book_title, copies)
    elif choice == '4':
        book_id = input("Enter Book ID to remove: ")
        library.remove_library_account(book_id)
    elif choice == '5':
        library.show_available_books()
    elif choice == '6':
        library.show_available_students()
    elif choice == '7':
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID to issue: ")
        library.issue_book(student_id, book_id)
    elif choice == '8':
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID to submit: ")
        library.submit_book(student_id, book_id)
    elif choice == '9':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please choose again.")
