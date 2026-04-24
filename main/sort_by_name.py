def sort_by_name(db):
    all_cocktails = []

    for cocktails in db.values():
        all_cocktails.extend(cocktails)

    sorted_list = sorted(all_cocktails, key=lambda x: x["name"].lower())

    print("\nCocktails sorted by name:\n")
    for c in sorted_list:
        print(f"- {c['name']} ({c['category']})")