from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '🧮 Flask Calculator API is running! Use POST /calculate'

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    if num1 is None or num2 is None or operation is None:
        return jsonify({'error': 'Missing num1, num2, or operation'}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero is not allowed'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
