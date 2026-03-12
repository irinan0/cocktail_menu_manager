def show_summary(db):
    """Provides a formatted table of the bar's status."""
    print("\n" + "="*35)
    print(f"{'CATEGORY':<20} | {'COUNT':<10}")
    print("-" * 35)
    total = 0
    for cat, drinks in db.items():
        print(f"{cat:<20} | {len(drinks):<10}")
        total += len(drinks)
    print("-" * 35)
    print(f"{'TOTAL RECIPES':<20} | {total:<10}")
    print("="*35)

def display_all(db):
    """Displays full details of every cocktail."""
    print("\n--- FULL COCKTAIL MENU ---")
    for cat, drinks in db.items():
        if drinks:
            print(f"\n[{cat.upper()}]")
            for d in drinks:
                status = "(Custom)" if d.get('custom') else "(Classic)"
                print(f" • {d['name']} {status}")
                for ing, amt in d['ingredients'].items():
                    print(f"   - {ing}: {amt}ml")