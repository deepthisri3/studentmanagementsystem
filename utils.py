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

# === UC2: Search Student ===
def search_student():
    choice = input("Search by (1) Roll_No or (2) Name? ")
    found = False
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        if choice == "1":
            roll = input("Enter Roll No: ")
            for row in reader:
                if row and row[0] == roll:
                    print("Student Found:", row)
                    found = True
        elif choice == "2":
            name = input("Enter Name (partial match): ").lower()
            for row in reader:
                if row and name in row[1].lower():
                    print("Match:", row)
                    found = True
    if not found:
        print("❌ No student found.")

# === UC3: Update Records ===
def update_student():
    roll = input("Enter Roll No to update: ")
    rows, updated = [], False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows.append(headers)
        for row in reader:
            if row and row[0] == roll:
                print("Old Record:", row)
                row[6] = input("Enter new Attendance %: ") or row[6]
                row[7] = input("Enter new Mid1 Marks: ") or row[7]
                row[8] = input("Enter new Mid2 Marks: ") or row[8]
                row[9] = input("Enter new Quiz Marks: ") or row[9]
                row[10] = input("Enter new Final Marks: ") or row[10]
                updated = True
            rows.append(row)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("✅ Updated." if updated else "❌ Student not found.")

# === UC4: Delete Student ===
def delete_student():
    roll = input("Enter Roll No to delete: ")
    rows, deleted = [], False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows.append(headers)
        for row in reader:
            if row and row[0] == roll:
                confirm = input(f"Delete {row}? (Y/N): ")
                if confirm.lower() == "y":
                    deleted = True
                    continue
            rows.append(row)

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("✅ Deleted." if deleted else "❌ Not deleted.")

# === UC5: Reports ===
def generate_report():
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    students, total_marks = [], []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            if row and row[2] == branch and row[3] == year:
                students.append(row)
                try:
                    total = float(row[7]) + float(row[8]) + float(row[9]) + float(row[10])
                    total_marks.append(total)
                except:
                    pass

    if not students:
        print("❌ No students found for report.")
        return

    avg = sum(total_marks) / len(total_marks)
    high, low = max(total_marks), min(total_marks)

    print("\n📊 Report")
    print("Total Students:", len(students))
    print("Class Average:", avg)
    print("Highest Score:", high)
    print("Lowest Score:", low)

    filename = f"report_{branch}_{year}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(students)
    print(f"✅ Report saved to {filename}")

# === UC6: Bulk Import ===
def bulk_import():
    file_in = input("Enter CSV filename to import: ")
    if not os.path.exists(file_in):
        print("❌ File not found.")
        return

    with open(file_in, "r") as fin, open(FILENAME, "a", newline="") as fout:
        reader = csv.reader(fin)
        writer = csv.writer(fout)
        next(reader)  # skip header
        for row in reader:
            if row:
                writer.writerow(row)

    print("✅ Bulk import completed.")

# === UC7: Sort / Filter ===
def sort_filter_students():
    choice = input("1. Sort by Marks  2. Filter by Attendance < 75: ")
    students = []
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            if row:
                students.append(row)

    if choice == "1":
        students.sort(key=lambda x: float(x[10]) if x[10] else 0, reverse=True)
    elif choice == "2":
        students = [row for row in students if float(row[6]) < 75]

    print("\nResult:")
    for row in students:
        print(row)