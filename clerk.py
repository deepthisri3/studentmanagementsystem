import utils

def clerk_menu():
    while True:
        print("\n--- Clerk Menu ---")
        print("1. Add New Student (UC1)")
        print("2. Delete Student (UC4)")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            utils.add_student()
        elif choice == "2":
            utils.delete_student()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")