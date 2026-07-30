def group_by_category(db):
    print("\nCocktails by category:\n")

    for category, cocktails in db.items():
        print(f"\n=== {category.upper()} ===")

        for c in cocktails:
            print(f"- {c['name']}")