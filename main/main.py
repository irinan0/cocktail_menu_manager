import os
import file_handler
import stats
import cocktail_logic


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("\nPress ENTER to continue...")


def main():
    # Requirement 3.1: Data structure initialized before the loop
    db = file_handler.load_database()

    while True:
        clear()
        print("🍸 COCKTAIL BAR MANAGER PRO")
        print("=" * 30)
        print("1. 📖 View Full Menu")
        print("2. ➕ Add Custom Cocktail")
        print("3. 🔍 Search by Ingredient")
        print("4. 📊 Bar Statistics")
        print("5. 💾 Save/Export Database")
        print("0. 🚪 Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            clear()
            stats.display_all(db)
            pause()
        elif choice == "2":
            clear()
            db = cocktail_logic.add_cocktail(db)
            pause()
        elif choice == "3":
            clear()
            cocktail_logic.search_by_ing(db)
            pause()
        elif choice == "4":
            clear()
            stats.show_summary(db)
            pause()
        elif choice == "5":
            clear()
            file_handler.save_database(db)
            pause()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
            pause()


if __name__ == "__main__":
    main()