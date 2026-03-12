def add_menu(data):
    """Handles the logic for adding a new cocktail to the list."""
    while True:
        print("\n--- ➕ Add New Recipe ---")
        name = input("Enter cocktail name (or 'back'): ").strip().title()
        if name.lower() == 'back': break
        if not name: continue

        category = input("Category (Alcoholic/Non-Alcoholic): ").strip().title()
        
        # Requirement: Nested List for Ingredients
        ing_input = input("Enter ingredients (separated by commas): ")
        ingredients = [i.strip() for i in ing_input.split(",") if i.strip()]
        
        glass = input("Glass type: ").strip()
        instructions = input("Instructions: ").strip()

        # Requirement: Nested Structure (Dict containing List and Dict)
        new_drink = {
            "name": name,
            "category": category,
            "ingredients": ingredients,
            "info": {"glass": glass, "instructions": instructions}
        }
        
        data.append(new_drink)
        print(f"Added {name} successfully!")
        break
    return data

def update_menu(data):
    """Finds a cocktail by name and updates its ingredients."""
    name_to_find = input("\nEnter the name of the cocktail to update: ").strip().title()
    for drink in data:
        if drink['name'] == name_to_find:
            print(f"Current ingredients: {drink['ingredients']}")
            new_ings = input("Enter new ingredients (comma separated): ")
            drink['ingredients'] = [i.strip() for i in new_ings.split(",") if i.strip()]
            print("Update complete!")
            return data
    print("Cocktail not found.")
    return data