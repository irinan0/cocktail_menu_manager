from flask import Flask, render_template, request, redirect, url_for
import file_handler

app = Flask(__name__)


@app.route('/')
def index():
    # Load database using your existing backend
    db = file_handler.load_database()

    # Calculate statistics
    stats = {cat: len(drinks) for cat, drinks in db.items()}

    # Render the HTML template, passing the data to it
    return render_template('index.html', db=db, stats=stats)


@app.route('/add', methods=['POST'])
def add_cocktail():
    db = file_handler.load_database()

    # Capture form data from HTML
    name = request.form.get('name')
    category = request.form.get('category')
    glass = request.form.get('glass')
    ingredients_raw = request.form.get('ingredients')

    # Parse ingredients string into a dictionary
    ingredients = {}
    for item in ingredients_raw.split(","):
        if ":" in item:
            ing_name, amt = item.split(":")
            ingredients[ing_name.strip()] = float(amt.strip())

    # Append to database and save
    new_drink = {
        "name": name,
        "category": category,
        "ingredients": ingredients,
        "glass": glass,
        "custom": True
    }
    db[category].append(new_drink)
    file_handler.save_database(db)

    # Reload the page
    return redirect(url_for('index'))


@app.route('/delete/<category>/<drink_name>', methods=['POST'])
def delete_cocktail(category, drink_name):
    db = file_handler.load_database()

    # Filter out the deleted drink and save
    db[category] = [d for d in db[category] if d['name'] != drink_name]
    file_handler.save_database(db)

    return redirect(url_for('index'))


if __name__ == '__main__':
    # Binds to 0.0.0.0 to allow AWS external traffic on port 8501
    app.run(host='0.0.0.0', port=8501)