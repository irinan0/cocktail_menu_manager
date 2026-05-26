import streamlit as st
import file_handler
import stats

# Configure the web page
st.set_page_config(page_title="Cocktail Bar Manager Pro", page_icon="🍸", layout="wide")

# Initialize the database into Streamlit's session state so it persists across button clicks
if 'db' not in st.session_state:
    st.session_state.db = file_handler.load_database()

db = st.session_state.db

st.title("🍸 Cocktail Bar Manager Pro")
st.markdown("---")

# Navigation Menu in Sidebar
menu_option = st.sidebar.radio(
    "Navigation Menu",
    [
        "📖 View Full Menu",
        "➕ Add Custom Cocktail",
        "❌ Delete a Cocktail",
        "🔍 Search by Ingredient",
        "📊 Bar Statistics"
    ]
)

# -----------------------------------------------------------------
# OPTION 1: VIEW FULL MENU
# -----------------------------------------------------------------
if menu_option == "📖 View Full Menu":
    st.header("📖 Current Cocktail Menu")

    for category, drinks in db.items():
        if drinks:
            st.subheader(f"⭐ {category.upper()} BASE")
            for drink in drinks:
                tag = "🟢 [CLASSIC]" if not drink.get('custom') else "🔵 [USER-CREATED]"

                # Expandable card for each cocktail
                with st.expander(f"{drink['name']} {tag}"):
                    if 'glass' in drink:
                        st.markdown(f"**Glassware:** {drink['glass']}")
                    if 'instructions' in drink:
                        st.markdown(f"**Instructions:** {drink['instructions']}")

                    st.markdown("**Ingredients:**")
                    for ing, amt in drink['ingredients'].items():
                        st.write(f"- {ing}: {amt}ml")

# -----------------------------------------------------------------
# OPTION 2: ADD CUSTOM COCKTAIL
# -----------------------------------------------------------------
elif menu_option == "➕ Add Custom Cocktail":
    st.header("➕ Create New Cocktail")

    with st.form("add_cocktail_form", clear_on_submit=True):
        name = st.text_input("Enter Cocktail Name:").strip()
        category = st.selectbox("Select Category:", list(db.keys()))
        glass = st.text_input("Glassware (e.g., Highball glass):").strip()
        instructions = st.text_area("Preparation Instructions:").strip()

        st.markdown("##### Ingredients (Minimum 2 required)")
        st.caption("Enter ingredient name and amount, separated by commas. Example: Light rum:50, Lime:20, Sugar:10")
        ingredients_raw = st.text_input("Ingredients list:")

        submitted = st.form_submit_button("Add Cocktail")

        if submitted:
            if not name:
                st.error("Please enter a cocktail name.")
            else:
                # Parse ingredients
                ingredients = {}
                try:
                    for item in ingredients_raw.split(","):
                        if ":" in item:
                            ing_name, amt = item.split(":")
                            ingredients[ing_name.strip()] = float(amt.strip())
                except ValueError:
                    st.error("Please ensure ingredient amounts are valid numbers.")

                if len(ingredients) < 2:
                    st.error("Error: Minimum 2 ingredients required!")
                else:
                    # Append new recipe
                    new_drink = {
                        "name": name,
                        "category": category,
                        "ingredients": ingredients,
                        "glass": glass,
                        "instructions": instructions,
                        "custom": True
                    }
                    db[category].append(new_drink)

                    # Force save back to file using file_handler context logic
                    file_handler.save_database(db)
                    st.success(f"Successfully added {name} to {category} database!")
                    st.rerun()

# -----------------------------------------------------------------
# OPTION 3: DELETE A COCKTAIL
# -----------------------------------------------------------------
elif menu_option == "❌ Delete a Cocktail":
    st.header("❌ Delete a Cocktail")

    category = st.selectbox("Select Category to view:", list(db.keys()))
    drinks = db[category]

    if not drinks:
        st.warning(f"No drinks found in {category}.")
    else:
        drink_names = [d['name'] for d in drinks]
        selected_drink_name = st.selectbox("Select Cocktail to Delete:", drink_names)

        if st.button("Delete Selected Cocktail", type="primary"):
            # Filter out the selected drink
            db[category] = [d for d in drinks if d['name'] != selected_drink_name]
            file_handler.save_database(db)
            st.success(f"Removed '{selected_drink_name}' from the database.")
            st.rerun()

# -----------------------------------------------------------------
# OPTION 4: SEARCH BY INGREDIENT
# -----------------------------------------------------------------
elif menu_option == "🔍 Search by Ingredient":
    st.header("🔍 Search Menu by Ingredient")
    query = st.text_input("Enter ingredient name (e.g., Rum, Juice, Mint):").strip().lower()

    if query:
        found = False
        for category, drinks in db.items():
            for drink in drinks:
                if any(query in ing.lower() for ing in drink['ingredients']):
                    st.info(f"🍹 **{drink['name']}** found in *{category} Base*")
                    found = True
        if not found:
            st.warning("No matching cocktail recipes found.")

# -----------------------------------------------------------------
# OPTION 5: BAR STATISTICS
# -----------------------------------------------------------------
elif menu_option == "📊 Bar Statistics":
    st.header("📊 Bar Summary & Metrics")

    # Render interactive grid metrics
    cols = st.columns(len(db.keys()) + 1)
    total_recipes = 0

    for idx, (cat, drinks) in enumerate(db.items()):
        cols[idx].metric(label=f"{cat} Recipes", value=len(drinks))
        total_recipes += len(drinks)

    cols[-1].metric(label="TOTAL RECIPES", value=total_recipes)

    # Optional bar chart visualization
    stats_data = {cat: len(drinks) for cat, drinks in db.items()}
    st.bar_chart(stats_data)