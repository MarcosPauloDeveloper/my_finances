from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from wtforms.fields import SelectField


app = Flask(__name__)
app.config["FLASK_ADMIN_SWATCH"] = "lux"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:4132@localhost/my_finances"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "d3f4e7cb-cbfc-4883-b223-b6488cd9cf4a"


admin = Admin(app, name="Minhas Finanças", template_mode="bootstrap4")
db = SQLAlchemy(app)


from models import Expense, Income


class ExpenseView(ModelView):
    edit_modal = True
    create_modal = True
    column_editable_list = ('date', 'description', 'expense_value')
    column_filters = ['date', 'description']
    can_export = True
    export_types = ['csv']


class IncomeView(ModelView):
    edit_modal = True
    create_modal = True
    column_editable_list = ('date', 'income_type', 'income_value')
    column_filters = ['date', 'income_type']
    can_export = True
    export_types = ['csv']
    form_extra_fields = {
        'income_type': SelectField('Tipo', choices=['Salário', 'Outros'])
    }


admin.add_view(ExpenseView(Expense, db.session, name="Gastos"))
admin.add_view(IncomeView(Income, db.session, name="Ganhos"))


if __name__ == '__main__':
    app.run(debug=True)
