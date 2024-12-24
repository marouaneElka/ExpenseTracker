from app.db_manager import DatabaseManager
from model.expense import Expense
from model.category import Category

class ExpenseTracker:
    def __init__(self):
        self.db_manager = DatabaseManager()

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