import os
import file_handler
import stats
import cocktail_logic

# Main ingredients list
def main():
    cocktails_db = {
        "Vodka": [],
        "Gin": [],
        "Rum": [],
        "Tequila": [],
        "Wine": [],
        "Non-Alcoholic": [],
   }
db = file_handler.load_database()

# Main menu initialization
while True:

        print("🍸 COCKTAIL BAR MANAGER PRO")
        print("=" * 35)
        print(" [1] 📖 View Full Menu")
        print(" [2] ➕ Add New Cocktail")
        print(" [3] 🔍 Search by Ingredient")
        print(" [4] 📊 Bar Statistics")
        print(" [5] 💾 Save/Export Data")
        print(" [0] 🚪 Exit")
        print("-" * 35)

        choice = input("\nSelect an option (0-4): ").strip()

        if choice == "1":
            print("\n[SYSTEM] -> Navigating to Display Module...")
        elif choice == "2":
            print("\n[SYSTEM] -> Navigating to Manage Module...")
        elif choice == "3":
            print("\n[SYSTEM] -> Navigating to Statistics Module...")
        elif choice == "4":
            print("\n[SYSTEM] -> Navigating to File Module...")
        elif choice == "0":
            print("\nExiting. Cheers!")
            break
        else:
            # Invalid input is caught and handled
            print("\n[ERROR] Invalid input. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()