from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Calculator App</title>
        </head>
        <body>
            <h1>Welcome to the Calculator App</h1>
            <p>Perform calculations using the following routes:</p>
            <ul>
                <li>/add</li>
                <li>/subtract</li>
                <li>/multiply</li>
                <li>/divide</li>
            </ul>
        </body>
    </html>
    '''

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        data = request.form
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        return render_template('result.html', operation='Addition', result=result)
    else:
        return render_template('form.html', operation='Addition')

@app.route('/subtract', methods=['POST', 'GET'])
def subtract():
    if request.method == 'POST':
        data = request.form
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 - num2
        return render_template('result.html', operation='Subtraction', result=result)
    else:
        return render_template('form.html', operation='Subtraction')

@app.route('/multiply', methods=['POST', 'GET'])
def multiply():
    if request.method == 'POST':
        data = request.form
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 * num2
        return render_template('result.html', operation='Multiplication', result=result)
    else:
        return render_template('form.html', operation='Multiplication')

@app.route('/divide', methods=['POST', 'GET'])
def divide():
    if request.method == 'POST':
        data = request.form
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        if num2 != 0:
            result = num1 / num2
            return render_template('result.html', operation='Division', result=result)
        else:
            return "Error: Division by zero is not allowed."
    else:
        return render_template('form.html', operation='Division')

if __name__ == '__main__':
    app.run(debug=True, port=8000)


