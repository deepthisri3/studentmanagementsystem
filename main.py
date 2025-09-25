from clerk import clerk_menu
from teacher import teacher_menu
from hod import hod_menu

def main_menu():
    while True:
        print("\n=== Student Management System ===")
        print("1. Office Clerk")
        print("2. Teacher")
        print("3. HOD / Admin")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            clerk_menu()
        elif choice == "2":
            teacher_menu()
        elif choice == "3":
            hod_menu()
        elif choice == "0":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()