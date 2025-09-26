import csv
import os

FILENAME = "students.csv"

# === UC1: Add Student ===
def add_student():
    roll = input("Enter Roll No: ")
    # Check duplicate
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("❌ Roll number already exists!")
                return

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    gender = input("Enter Gender: ")
    age = input("Enter Age: ")
    attendance = input("Enter Attendance %: ")
    mid1 = input("Enter Mid1 Marks: ")
    mid2 = input("Enter Mid2 Marks: ")
    quiz = input("Enter Quiz Marks: ")
    final = input("Enter Final Marks: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, branch, year, gender, age, attendance, mid1, mid2, quiz, final])

    print("✅ Student added successfully!")

def clerk_menu():
    while True:
        print("\n--- Clerk Menu ---")
        print("1. Add New Student (UC1)")
        print("2. Delete Student (UC4)")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")