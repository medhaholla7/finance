 from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Store data
categories = []
transactions = []
monthly_income = 0
monthly_expenses = 0
income_goal = 0
expenses_goal = 0

@app.route('/')
def index():
    return render_template('index.html', 
                           transactions=transactions, 
                           categories=categories, 
                           income_goal=income_goal, 
                           expenses_goal=expenses_goal,
                           monthly_income=monthly_income, 
                           monthly_expenses=monthly_expenses)

@app.route('/add_income', methods=['POST'])
def add_income():
    global transactions, monthly_income
    source = request.form.get('source')
    amount = float(request.form.get('amount'))
    if source and amount:
        transactions.append({
            'date': datetime.now().strftime('%Y-%m-%d'),
            'type': 'Income',
            'category': None,
            'details': source,
            'amount': amount
        })
        monthly_income += amount
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    global transactions, monthly_expenses
    name = request.form.get('name')
    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    
    if name and amount and category:
        transactions.append({
            'date': datetime.now().strftime('%Y-%m-%d'),
            'type': 'Expense',
            'category': category,
            'details': name,
            'amount': amount
        })
        monthly_expenses += amount
    return redirect(url_for('index'))

@app.route('/set_goals', methods=['POST'])
def set_goals():
    global income_goal, expenses_goal
    income_goal = float(request.form.get('income_goal'))
    expenses_goal = float(request.form.get('expenses_goal'))
    return redirect(url_for('index'))

@app.route('/add_category', methods=['POST'])
def add_category():
    category = request.form.get('category_name')
    if category:
        categories.append(category)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
