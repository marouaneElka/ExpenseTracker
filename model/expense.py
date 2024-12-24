class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def get_summary(self):
        return f"Expense on {self.date}: {self.category} - {self.description} for {self.amount:.2f} EUR"