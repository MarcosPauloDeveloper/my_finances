from app import db


class Expense(db.Model):
    __tablename__ = 'expense'
    expense_id = db.Column(db.Integer, primary_key=True)
    expense_value = db.Column(db.Float)
    description = db.Column(db.String(1000))
    date = db.Column(db.Date)

    def __repr__(self):
        return self.expense_id


class Income(db.Model):
    __tablename__ = 'income'
    income_id = db.Column(db.Integer, primary_key=True)
    income_value = db.Column(db.Float)
    income_type = db.Column(db.String(500))
    date = db.Column(db.Date)

    def __repr__(self):
        return self.income_id
