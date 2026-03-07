# Cocktail Menu Manager

A Python-based CLI application to manage cocktail recipes. This application allows users to browse drinks by base spirit, create custom recipes, and export data to CSV.

## Features
- **Browse by Base:** View cocktails based on Vodka, Gin, Tequila, Rum, or Wine.
- **Custom Creation:** Build your own cocktail from a list of available ingredients.
- **Menu Settings:** Update existing cocktail details or export the menu to a CSV file.
- **Data Persistence:** Uses JSON for the primary database and supports CSV for external exports.

## Technical Skills Applied
- **Nested Data Structures:** Dictionary of lists and dictionaries to store complex recipe data.
- **File I/O:** Reading and writing JSON and CSV files.
- **Modules:** Organized code into logic, data, and presentation layers.
- **Input Validation:** Ensuring user choices and dosages are handled correctly.

## How to Run
1. Ensure `menu.json` is in the same directory.
2. Run `python main.py`.
