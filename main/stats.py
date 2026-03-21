
def display_all_recipes(db):
    """ Displays data from JSON using nested loops."""
    print("--- 📖 CURRENT COCKTAIL MENU ---")

    found_any = False
    for category, drinks in db.items():
        if drinks:
            found_any = True
            print(f"\n⭐ {category.upper()} BASE:")

            for drink in drinks:
                # Distinguish between original and user-added drinks
                tag = "[CLASSIC]" if not drink.get('custom') else "[USER-CREATED]"
                print(f"  • {drink['name']} {tag}")

                # Nested loop for ingredients (Dictionary inside List)
                for ing, amt in drink['ingredients'].items():
                    print(f"    - {ing}: {amt}ml")

    if not found_any:
        print("\nThe bar is currently empty! Use Option 2 to add drinks.")


def show_summary(db):
    """ Shows a formatted status table."""
    print(f"{'CATEGORY':<20} | {'COUNT':<5}")
    print("-" * 28)
    total = 0
    for cat, drinks in db.items():
        print(f"{cat:<20} | {len(drinks):<5}")
        total += len(drinks)
    print("-" * 28)
    print(f"{'TOTAL RECIPES':<20} | {total:<5}")