class Expense:
    def __init__(self, user_id: str, amount: float, category: str, date: str):
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.date = date
