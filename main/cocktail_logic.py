def add_cocktail(db):
    """Requirement 3.3: Add data with validation (min 2 ingredients)."""
    print("\n--- CREATE NEW COCKTAIL ---")
    name = input("Enter Cocktail Name: ").strip()

    # Category selection
    cats = list(db.keys())
    for i, c in enumerate(cats): print(f"{i + 1}. {c}")
    try:
        cat_idx = int(input("Select Category Number: ")) - 1
        category = cats[cat_idx]
    except:
        return db

    # Ingredient collection
    ingredients = {}
    print("Add ingredients (type 'done' when finished):")
    while True:
        ing = input(" Ingredient Name: ").strip()
        if ing.lower() == 'done':
            if len(ingredients) < 2:
                print("Error: Minimum 2 ingredients required!")
                continue
            break
        try:
            amt = float(input(f" Amount of {ing} (ml): "))
            ingredients[ing] = amt
        except ValueError:
            print("Please enter a numeric value.")

    db[category].append({"name": name, "ingredients": ingredients, "custom": True})
    print(f"Successfully added {name}!")
    return db


def search_by_ing(db):
    """Search functionality using membership testing (Lesson 3)."""
    query = input("\nEnter ingredient to search for: ").lower()
    found = False
    for cat, drinks in db.items():
        for d in drinks:
            # Check if query exists in the keys of the ingredients dictionary
            if any(query in ing.lower() for ing in d['ingredients']):
                print(f"-> Found '{d['name']}' in {cat}")
                found = True
    if not found: print("No matches found.")