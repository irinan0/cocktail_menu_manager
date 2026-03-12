import json

def load_menu(current):
    """Loads external files into the application."""
    print("\n1. JSON | 2. CSV")
    choice = input("Select: ")
    mode = input("1. Replace | 2. Append: ")
    
    loaded = []
    try:
        if choice == '1':
            with open('cocktails.json', 'r') as f: loaded = json.load(f)
        elif choice == '2':
            with open('cocktails.csv', 'r') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    r['ingredients'] = r['ingredients'].split(';')
                    loaded.append(r)
        return loaded if mode == '1' else current + loaded
    except FileNotFoundError:
        print("File not found."); return current