def show_summary(data):
    """Displays summary statistics about the cocktail database."""
    if not data:
        print("No data to analyze.")
        return

    total = len(data)
    alc_count = len([d for d in data if d['category'] == 'Alcoholic'])
    non_alc = total - alc_count
    
    # Calculate average number of ingredients
    avg_ing = sum(len(d['ingredients']) for d in data) / total

    print("\n--- 📊 Mixology Analytics ---")
    print(f"Total Recipes:      {total}")
    print(f"Alcoholic:          {alc_count}")
    print(f"Non-Alcoholic:      {non_alc}")
    print(f"Avg. Ingredients:   {avg_ing:.1f}")