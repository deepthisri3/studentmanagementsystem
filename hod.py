import utils

def hod_menu():
    while True:
        print("\n--- HOD / Admin Menu ---")
        print("1. Generate Reports (UC5)")
        print("2. Bulk Import Students (UC6)")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            utils.generate_report()
        elif choice == "2":
            utils.bulk_import()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
            