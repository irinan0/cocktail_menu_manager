import json


def load_database(filename="bar_data.json"):
    try:
        with open(filename, 'r') as f:
            raw_data = json.load(f)

        # If the data is a list, restructure it into a dictionary by category
        if isinstance(raw_data, list):
            structured_db = {}
            for drink in raw_data:
                cat = drink.get('category', 'Uncategorized')
                if cat not in structured_db:
                    structured_db[cat] = []

                # Convert ingredients list to dict to match your stats.py logic
                if isinstance(drink['ingredients'], list):
                    # Defaulting to 0ml since the JSON doesn't have amounts
                    drink['ingredients'] = {ing: 0 for ing in drink['ingredients']}

                structured_db[cat].append(drink)
            return structured_db

        return raw_data

    except (FileNotFoundError, json.JSONDecodeError):
        return {"Alcoholic": [], "Non-Alcoholic": []}

def save_database(db):
    """ Save to file with a filtering option."""
    print("\n--- SAVE DATABASE ---")
    filename = input("Enter filename (e.g., backup.json): ").strip()
    if not filename.endswith('.json'): filename += '.json'

    print("1. Save All Categories")
    print("2. Filter (Save only one category)")
    mode = input("Select mode: ")

    data_to_save = db
    if mode == "2":
        cats = list(db.keys())
        for i, cat in enumerate(cats): print(f"{i+1}. {cat}")
        try:
            idx = int(input("Select category index: ")) - 1
            data_to_save = {cats[idx]: db[cats[idx]]}
        except:
            print("Invalid choice, saving all.")

    with open(filename, 'w') as f:
        json.dump(data_to_save, f, indent=4)
    print(f"Successfully saved to {filename}")