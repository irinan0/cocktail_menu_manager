import cocktail_viewer
import cocktail_manager
import analytics
import dummy_data

def main():
    """
    Main entry point for The Mixology Hub.
    Manages the primary navigation loop and initializes the data.
    """
    # Requirement: Initialize data structures at the top
    cocktails = []

    while True:
        print("\n" + "="*30)
        print("🍸 THE MIXOLOGY HUB 🍸")
        print("="*30)
        print("1. View/Filter Recipes")
        print("2. Add New Recipe")
        print("3. Update Existing Recipe")
        print("4. Mixology Analytics")
        print("5. Load Dummy Data (JSON/CSV)")
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ").strip()

        # Requirement: Modular Routing
        if choice == '1':
            cocktail_viewer.show_menu(cocktails)
        elif choice == '2':
            cocktails = cocktail_manager.add_menu(cocktails)
        elif choice == '3':
            cocktails = cocktail_manager.update_menu(cocktails)
        elif choice == '4':
            analytics.show_summary(cocktails)
        elif choice == '5':
            cocktails = dummy_data.load_menu(cocktails)
        elif choice == '6':
            print("Cheers! Program closed.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()