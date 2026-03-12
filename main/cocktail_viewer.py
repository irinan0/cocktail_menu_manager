def show_menu(data):
    """Sub-menu for viewing, filtering, and sorting recipes."""
    if not data:
        print("\n[!] The list is empty. Load data first.")
        return

    while True:
        print("\n--- 📖 Recipe Gallery ---")
        print("1. View All")
        print("2. Filter by Category (Alcoholic/Non-Alcoholic)")
        print("3. Sort by Name (A-Z)")
        print("4. Back to Main Menu")
        
        choice = input("Select: ").strip()
        
        if choice == '1':
            display_list(data)
        elif choice == '2':
            filter_by_category(data)
        elif choice == '3':
            sort_by_name(data)
        elif choice == '4':
            break

def display_list(subset):
    """Iterates through data and prints using f-strings."""
    print(f"\n{'NAME':<20} | {'CATEGORY':<15} | {'INGREDIENTS'}")
    print("-" * 60)
    for drink in subset:
        # Requirement: Using .join() for list display
        ing_str = ", ".join(drink['ingredients'])
        print(f"{drink['name']:<20} | {drink['category']:<15} | {ing_str}")

def filter_by_category(data):
    """Filters list based on user input."""
    cat = input("Enter category (Alcoholic/Non-Alcoholic): ").strip().title()
    filtered = [d for d in data if d['category'] == cat]
    display_list(filtered) if filtered else print("No matches found.")

def sort_by_name(data):
    """Sorts the current list alphabetically by name."""
    # We sort a copy so we don't mess up the original order permanently if not desired
    sorted_data = sorted(data, key=lambda x: x['name'])
    display_list(sorted_data)