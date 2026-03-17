import json

def load_database(filename="bar_data.json"):
    """Dummy data loader from JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Default structure if file is missing or corrupted
        return {"Vodka": [], "Gin": [], "Rum": [], "Tequila": [], "Wine": [], "Non-Alcoholic": []}

def save_database(db):
    """Save to file with a filtering option."""
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