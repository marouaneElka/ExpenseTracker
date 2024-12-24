from app.db_manager import DatabaseManager
from model.expense import Expense
from model.category import Category

class ExpenseTracker:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def add_expense(self, date, category, description, amount):
        expense = Expense(date, category, description, amount)
        self.db_manager.insert_expense(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        expenses = self.db_manager.fetch_expenses()
        if expenses:
            print("\nExpenses:")
            for i, entry in enumerate(expenses, 1):
                print(f"{i}. {entry['expense'].get_summary()}")
        else:
            print("No expenses found.")
            
    def run_menu(self):
        while True:
            print("\nPersonal Expense Tracker")
            print("1. View All Expenses")
            print("2. Add an Expense")
            print("3. View Total Expenses by Category")
            print("4. Remove an Expense")
            print("5. Generate Report")
            print("6. Exit")
            choice = input("Enter your choice: ")