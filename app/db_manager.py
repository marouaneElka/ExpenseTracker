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