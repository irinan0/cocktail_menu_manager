
#Logic Module
#Handles CRUD operations (Create, Read, Update) and Search features.


def add_cocktail(db):
    print("--- CREATE NEW COCKTAIL ---")
    name = input("Cocktail Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return db

    # Category selection using keys from the dictionary
    categories = list(db.keys())
    for i, cat in enumerate(categories):
        print(f"{i + 1}. {cat}")

    try:
        idx = int(input("Select base category number: ")) - 1
        selected_cat = categories[idx]
    except (ValueError, IndexError):
        print("Invalid category selection.")
        return db

        # Ingredient collection loop
    ingredients = {}
    print("Enter ingredients (type 'done' to finish):")
    while True:
        ing_name = input(" - Ingredient: ").strip()
        if ing_name.lower() == 'done':
            if len(ingredients) < 2:
                print("⚠️ Error: You must have at least 2 ingredients!")
                continue
            break

    try:
        amount = float(input(f"   Amount for {ing_name} (ml): "))
        ingredients[ing_name] = amount
    except ValueError:
        print("   ❌ Invalid amount. Use numbers only.")

    # Append the new cocktail dictionary to the list in that category
    new_drink = {"name": name, "ingredients": ingredients, "custom": True}
    db[selected_cat].append(new_drink)
    print(f"\n✅ {name} added to {selected_cat} successfully!")
    return db


def search_by_ingredient(db):
    #Searches cocktails
    print("--- SEARCH BY INGREDIENT ---")
    query = input("Enter ingredient to find: ").lower().strip()

    found = False
    # Nested loop: Category -> Cocktail List -> Ingredients Dictionary
    for cat, drinks in db.items():
        for drink in drinks:
            # Check if query is in any of the ingredient names
            if any(query in ing.lower() for ing in drink['ingredients']):
                print(f"👉 Found match: {drink['name']} (Base: {cat})")
                found = True

    if not found:
        print(f"No cocktails found containing '{query}'.")