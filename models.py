from app import db


class Expense(db.Model):
    __tablename__ = 'expense'

    expense_id = db.Column(db.Integer, primary_key=True)
    expense_value = db.Column(db.Float)
    description = db.Column(db.String(1000))
    date = db.Column(db.Date)

    def __repr__(self):
        return self.expense_id
