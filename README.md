# Expense Tracker Application

### Overview
This Expense Tracker is a command-line application designed to help users manage their expenses. It provides functionality to add, view, categorize, remove, and generate reports of expenses in either CSV or Excel formats.

## Features
### 1. View All Expenses
- Lists all the recorded expenses with details like:
  - Date
  - Category
  - Description
  - Amount

### 2. Add an Expense
- Allows the user to input details such as:
  - **Date of expense**
  - **Category** (e.g., Food, Transportation)
  - **Description** (optional)
  - **Amount** (mandatory)

### 3. View Total Expenses by Category
- Displays all expenses.
- Prompts the user to input a category and then:
  - Lists all expenses for that category.
  - Calculates and displays the total amount spent in the specified category.

### 4. Remove an Expense
- Lists all expenses.
- Allows the user to select an expense by its number and remove it from the database.

### 5. Generate Report
- Prompts the user to select a file format (`CSV` or `Excel`).
- Exports all expenses into the chosen format:
  - `report.csv`
  - `report.xlsx`

### 6. Exit
- Safely exits the application.

## Setup
1.  Clone the Repository using: git clone https://github.com/marouaneElka/ExpenseTracker
2.  Set up the Virtual Environment using: `python -m venv venv` and go inside the environment
3.  Activate the Virtual Environment using:
-   On windows in cmd: `.venv/Scripts/activate.bat`
-   On Windows in Powershell: `.venv/Scripts/activate.ps1`
-   On Mac OS or Linux: `source .venv/bin/activate`
3.  Install Dependencies using: `pip install -r requirements.txt`
4.  Run the Application using: `python main.py`


## Project Structure

```markdown
expense-tracker/
├── app/
│   ├── __init__.py          # Makes the app a package
│   ├── tracker.py           # Main application script
│   ├── db_manager.py        # Handles SQLite database operations
├── model/
│   ├── __init__.py          # Makes the model a package
│   ├── expense.py           # Contains the Expense class
├── database/
│   ├── __init__.py          # Makes the database folder a package
│   └── ExpenseTracker.db    # SQLite database (auto-created if missing)
├── config/
│   ├── __init__.py          # Makes the config folder a package
│   ├── config.py            # Environment configuration (reads .env file)
│   └── .env                 # Environment variables
├── __init__.py              # Root-level package initialization
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── main.py                  # Entry point for the application
```

## Environment Configuration
This project uses an `.env` file to configure the database path and other settings. An example `.env` file:
```bash
DB_PATH="database/ExpenseTracker.db"
PRODUCTION=False
```