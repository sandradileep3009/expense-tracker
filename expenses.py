class Expense:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.price:.2f}>"
