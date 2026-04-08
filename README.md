# Cocktail Bar Manager Pro

A modular Python CLI application designed to manage a digital database of drink recipes. This tool allows for menu management, including ingredient tracking in milliliters (ml), glassware selection, and detailed preparation instructions.

---

## Author
Irina Norinsky

---

## Features

* Tabular Menu View: Displays a table including Cocktail Name, Glassware, Category, Instructions, and precise Ingredient amounts.
* Custom Recipe Creation: Add new cocktails with built-in validation (minimum 2 ingredients required).
* Case-Insensitive Search: Find recipes by searching for specific ingredients regardless of capitalization.
* Dynamic Updating: Modify the names or ingredient lists of existing cocktails in the database.
* Secure Deletion: Remove unwanted cocktails from the menu database.
* Advanced Exporting: Save your database to custom filenames or specific folder paths, with options to filter by category.

---

## Project Structure

The application is built with a modular architecture:

| File | Function |
| :--- | :--- |
| main.py | The central entry point managing the user interface and menu loop. |
| cocktail_logic.py | Core logic for adding, searching, deleting, and updating data. |
| file_handler.py | Manages JSON data persistence and directory-aware saving/loading. |
| stats.py | Handles data visualization and table generation. |
| bar_data.json | The primary data store containing the recipe collection. |

---

## How to Run

This project requires no installation of external libraries.

1. Prerequisites: Ensure you have Python 3.x installed on your system.
2. Setup: Place all .py files and the bar_data.json file in the same directory.
3. Execution: Open a terminal or command prompt in that directory and run:
   python main.py

---

## Data Format

The system utilizes a structured JSON format where each cocktail entry includes:
* Name: The identifier for the drink.
* Category: Grouped by Alcoholic or Non-Alcoholic.
* Ingredients: Mapped as a dictionary of names and numeric values in ml.
* Glass: Specific glassware requirements.
* Instructions: Step-by-step preparation guide.

---

## Requirements
* Python 3.6+
* Standard Libraries: os, json

## Open for contribution
