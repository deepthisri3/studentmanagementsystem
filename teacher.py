import utils

def teacher_menu():
    while True:
        print("\n--- Teacher Menu ---")
        print("1. Search Student (UC2)")
        print("2. Update Records (UC3)")
        print("3. Sort / Filter Students (UC7)")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            utils.search_student()
        elif choice == "2":
            utils.update_student()
        elif choice == "3":
            utils.sort_filter_students()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")