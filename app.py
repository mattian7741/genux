from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
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

