from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def transactions():
    return render_template('transactions.html')

@app.route('/merchants')
def merchants():
    return render_template('merchants.html')

@app.route('/transaction_data')
def transaction_data():
    response = {
        'columns': [
            {'data': 'id', 'title': 'ID'},
            {'data': 'date', 'title': 'Date'},
            {'data': 'value', 'title': 'Value'},
            {'data': 'category', 'title': 'Category'}
        ],
        'data': [
            {'id': 1, 'date': '2023-01-01', 'value': 100.5, 'category': 'A'},
            {'id': 2, 'date': '2023-01-01', 'value': 102.3, 'category': 'B'},
            {'id': 3, 'date': '2023-01-03', 'value': 98.7, 'category': 'A'},
            {'id': 4, 'date': '2023-01-05', 'value': 105.2, 'category': 'C'},
            {'id': 5, 'date': '2023-01-05', 'value': 99.4, 'category': 'A'},
            {'id': 6, 'date': '2023-01-08', 'value': 104.8, 'category': 'B'},
            {'id': 7, 'date': '2023-01-10', 'value': 96.4, 'category': 'C'},
            {'id': 8, 'date': '2023-01-11', 'value': 100.9, 'category': 'A'},
            {'id': 9, 'date': '2023-01-11', 'value': 103.1, 'category': 'B'},
            {'id': 10, 'date': '2023-01-15', 'value': 108.5, 'category': 'A'},
            {'id': 11, 'date': '2023-01-18', 'value': 101.0, 'category': 'C'},
            {'id': 12, 'date': '2023-01-20', 'value': 107.2, 'category': 'B'},
            {'id': 13, 'date': '2023-01-20', 'value': 104.5, 'category': 'A'},
            {'id': 14, 'date': '2023-01-22', 'value': 102.8, 'category': 'C'},
            {'id': 15, 'date': '2023-01-25', 'value': 100.1, 'category': 'B'}
        ]
    }
    return jsonify(response)

@app.route('/merchant_data')
def merchant_data():
    response = {
        'columns': [
            {'data': 'id', 'title': 'ID'},
            {'data': 'name', 'title': 'Name'},
            {'data': 'age', 'title': 'Age'},
            {'data': 'sign', 'title': 'Sign'}
        ],
        'data': [
            {'id': 1, 'name': 'Alice', 'age': 28, 'sign': 'Aries'},
            {'id': 2, 'name': 'Bob', 'age': 25, 'sign': 'Sagitarius'},
            {'id': 3, 'name': 'Charlie', 'age': 35, 'sign': 'Cancer'},
            {'id': 4, 'name': 'Bob', 'age': 28, 'sign': 'Scorpio'}
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8001, debug=True)

