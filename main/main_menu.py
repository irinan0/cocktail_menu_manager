import cocktail_logic
import file_handler
import stats


def main():
    # Initialize Data
    db = file_handler.load_data() # Load initial/famous cocktails

    while True:
        print("\n=== COCKTAIL APP MENU ===")
        print("1. Famous Cocktails (View All)")
        print("2. Create Author's Cocktail")
        print("3. Edit Existing Cocktail")
        print("4. Search by Ingredient")
        print("5. Load/Upload List (JSON)")
        print("6. Save/Download List (JSON)")
        print("7. Bar Statistics (Summary)")
        print("0. Exit")

    #menu selection
        choice = input("\nSelect option: ")

        if choice == "1":
            stats.show_all_recipes(db)
        elif choice == "2":
            db = cocktail_logic.add_cocktail(db)
        elif choice == "3":
            db = cocktail_logic.edit_cocktail(db)
        elif choice == "4":
            cocktail_logic.search_ingredient(db)
        elif choice == "5":
            db = file_handler.load_data(input("Enter filename: "))
        elif choice == "6":
            file_handler.save_data(db)
        elif choice == "7":
            stats.display_stats(db)
        elif choice == "0":
            print("Cheers! Goodbye.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()