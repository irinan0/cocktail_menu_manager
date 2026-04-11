import os
import file_handler
import stats
import cocktail_logic


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("\nPress ENTER to continue...")

# Main menu initialization
def main():

    db = file_handler.load_database()

    while True:
        clear()
        print("🍸 COCKTAIL BAR MANAGER PRO")
        print("=" * 30)
        print("1. 📖 View Full Menu")
        print("2. ➕ Add Custom Cocktail")
        print("3. ❌ Delete a Cocktail")
        print("4. 🔍 Search by Ingredient")
        print("5. 📊 Bar Statistics")
        print("6. 💾 Save/Export Database")
        print("7. ❌ Delete ALL Menu")
        print("0. 🚪 Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            clear()
            stats.display_all_recipes(db)
            pause()
        elif choice == "2":
            clear()
            db = cocktail_logic.add_cocktail(db)
            pause()
        elif choice == "3":
            clear()
            db = cocktail_logic.delete_cocktail(db)
            pause()
        elif choice == "4":
            clear()
            cocktail_logic.search_by_ing(db)
            pause()
        elif choice == "5":
            clear()
            stats.show_summary(db)
            pause()
        elif choice == "6":
            clear()
            file_handler.save_database(db)
            pause()
        elif choice == "7":
            clear()
            cocktail_logic.delete_manu(db)
            pause()
            #cocktail_logic.delete_manu(db)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")
            pause()


if __name__ == "__main__":
    main()