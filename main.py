import os
import pandas as pd
import random
import csv


if not os.path.exists("data"):
    os.makedirs("data")


csv_file = "data/students.csv"
excel_file = "data/students.xlsx"


if not os.path.exists(csv_file):
    columns = ["Roll_No", "Name", "Branch", "Year", "Gender", "Age",
               "Attendance_%", "Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(csv_file, index=False)
    df.to_excel(excel_file, index=False)
    print("Empty CSV and Excel created successfully.")
else:
    df = pd.read_csv(csv_file)
    df.to_excel(excel_file, index=False)
    print("CSV already exists. Synced to Excel.")


def save_data(df):
    df.to_csv(csv_file, index=False)
    df.to_excel(excel_file, index=False)

def menu():
    print("\n--- Student Management System ---")
    print("1. Add New Student")
    print("2. Lookup Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Generate Report")
    print("6. Bulk Import CSV")
    print("7. Sort / Filter Students")
    print("8. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_student():
    df = pd.read_csv(csv_file)
    try:
        roll = int(input("Enter Roll No: "))
        if roll in df['Roll_No'].values:
            print("Roll No already exists!")
            return
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = int(input("Enter Year: "))
        gender = input("Enter Gender: ")
        age = int(input("Enter Age: "))
        attendance = int(input("Enter Attendance (0-100): "))
        mid1 = int(input("Enter Mid1 Marks (0-100): "))
        mid2 = int(input("Enter Mid2 Marks (0-100): "))
        quiz = int(input("Enter Quiz Marks (0-20): "))
        final = int(input("Enter Final Marks (0-100): "))
        
        new_student = {
            "Roll_No": roll, "Name": name, "Branch": branch, "Year": year,
            "Gender": gender, "Age": age, "Attendance_%": attendance,
            "Mid1_Marks": mid1, "Mid2_Marks": mid2, "Quiz_Marks": quiz, "Final_Marks": final
        }
        
        df = pd.concat([df, pd.DataFrame([new_student])])
        save_data(df)
        print("Student added successfully! (Saved to CSV & Excel)")
    except ValueError:
        print("Invalid input! Please enter correct data types.")

def lookup_student():
    df = pd.read_csv(csv_file)
    choice = input("Search by Roll_No (R) or Name (N)? ").upper()
    if choice == 'R':
        roll = int(input("Enter Roll No: "))
        result = df[df['Roll_No'] == roll]
    elif choice == 'N':
        name = input("Enter Name: ")
        result = df[df['Name'].str.contains(name, case=False)]
    else:
        print("Invalid choice!")
        return
    if not result.empty:
        print(result)
    else:
        print("No student found.")

def update_student():
    df = pd.read_csv(csv_file)
    roll = int(input("Enter Roll No to update: "))
    if roll not in df['Roll_No'].values:
        print("Roll No not found!")
        return
    idx = df[df['Roll_No'] == roll].index[0]
    print("Current data:\n", df.loc[idx])
    col = input("Enter column to update (Attendance_%/Mid1_Marks/...): ")
    if col not in df.columns:
        print("Invalid column!")
        return
    new_val = int(input(f"Enter new value for {col}: "))
    df.loc[idx, col] = new_val
    save_data(df)
    print("Record updated successfully! (Saved to CSV & Excel)")

def delete_student():
    df = pd.read_csv(csv_file)
    roll = int(input("Enter Roll No to delete: "))
    if roll not in df['Roll_No'].values:
        print("Roll No not found!")
        return
    confirm = input("Are you sure? (Y/N): ").upper()
    if confirm == 'Y':
        idx = df[df['Roll_No'] == roll].index[0]
        df_deleted = df.loc[[idx]]  # backup
        df.drop(idx, inplace=True)
        save_data(df)
        df_deleted.to_csv('data/students_deleted.csv', mode='a', index=False, header=False)
        df_deleted.to_excel('data/students_deleted.xlsx', mode='a', index=False, header=False, engine="openpyxl")
        print("Student deleted successfully! (Saved to CSV & Excel)")
    else:
        print("Deletion cancelled.")


while True:
    choice = menu()
    if choice == '1':
        add_student()
    elif choice == '2':
        lookup_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Report function not implemented yet.")
    elif choice == '6':
        print("Bulk import not implemented yet.")
    elif choice == '7':
        print("Sort/Filter not implemented yet.")
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")