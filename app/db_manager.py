import sqlite3
import csv
from model.expense import Expense

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("database/sample.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                amount REAL NOT NULL,
                FOREIGN KEY (category) REFERENCES categories (name)
            )
        """)

        self.connection.commit()

    def insert_category(self, category_name):
        self.cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (category_name,))
        self.connection.commit()

    def insert_expense(self, expense):
        self.insert_category(expense.category)
        self.cursor.execute(
            "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
            (expense.date, expense.category, expense.description, expense.amount)
        )
        self.connection.commit()

    def fetch_expenses(self):
        self.cursor.execute("SELECT id, date, category, description, amount FROM expenses")
        rows = self.cursor.fetchall()
        return [{"id": row[0], "expense": Expense(row[1], row[2], row[3], row[4])} for row in rows]

    def fetch_expenses_by_category(self, category):
        self.cursor.execute("SELECT id, date, category, description, amount FROM expenses WHERE LOWER(category) = LOWER(?)", (category.strip(),))
        rows = self.cursor.fetchall()
        total = sum(row[4] for row in rows)
        return [{"id": row[0], "expense": Expense(row[1], row[2], row[3], row[4])} for row in rows], total

    def remove_expense(self, expense_id):
        self.cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        self.connection.commit()

    def export_report(self, output_format="csv"):
        query = "SELECT * FROM expenses"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        if output_format == "csv":
            with open("report.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["ID", "Date", "Category", "Description", "Amount"])
                writer.writerows(data)
            print("Report saved as 'report.csv'.")
        elif output_format == "excel":
            df = pd.DataFrame(data, columns=["ID", "Date", "Category", "Description", "Amount"])
            df.to_excel("report.xlsx", index=False)
            print("Report saved as 'report.xlsx'.")