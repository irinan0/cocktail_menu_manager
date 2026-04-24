import sort_by_name
import group_by_category

def sort_menu(db):
    while True:
        print("\nSort Options:")
        print("1. Sort by name.")
        print("2. Sort by category.")
        print("3. Back to main menu.")

        choice = input("Choose an option: ")

        if choice == "1":
            sort_by_name.sort_by_name(db)
        elif choice == "2":
            group_by_category.group_by_category(db)
        elif choice == "3":
            break
        else:
            print("Invalid choice")