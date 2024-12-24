from app.db_manager import DatabaseManager
from model.expense import Expense

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

    def view_total_by_category(self):
        category = input("\nEnter category to view total expenses: ")
        expenses, total = self.db_manager.fetch_expenses_by_category(category)
        if expenses:
            print(f"\nExpenses for category '{category}':")
            for i, entry in enumerate(expenses, 1):
                print(f"{i}. {entry['expense'].get_summary()}")
            print(f"\nTotal expenses for category '{category}': {total:.2f} EUR")
        else:
            print(f"No expenses found for category '{category}'.")

    def remove_expense(self):
        expenses = self.db_manager.fetch_expenses()
        if not expenses:
            print("No expenses to remove.")
            return

        print("\nExpenses:")
        for i, entry in enumerate(expenses, 1):
            print(f"{i}. {entry['expense'].get_summary()}")

        try:
            choice = int(input("Enter the number of the expense to remove: "))
            if 1 <= choice <= len(expenses):
                expense_id = expenses[choice - 1]["id"]
                self.db_manager.remove_expense(expense_id)
                print("Expense removed successfully.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def generate_report(self, output_format):
        self.db_manager.export_report(output_format)

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

            if choice == "1":
                self.view_expenses()
            elif choice == "2":
                date = input("Enter date (YYYY-MM-DD): ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                amount = float(input("Enter cost: "))
                self.add_expense(date, category, description, amount)
            elif choice == "3":
                self.view_expenses()
                self.view_total_by_category()
            elif choice == "4":
                self.remove_expense()
            elif choice == "5":
                output_format = input("Choose excel or csv: ").lower()
                self.generate_report(output_format)
            elif choice == "6":
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")