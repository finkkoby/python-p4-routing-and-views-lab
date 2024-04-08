#!/usr/bin/env python3

from flask import Flask
import re
pattern = re.compile(r'[\+\-\*\%]|div')

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:word>')
def print_string(word):
    print(word)
    return word

@app.route('/count/<int:number>')
def count(number):
    answer = ''
    for num in range(number):
        answer += f'{num}\n'
    return answer

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '%':
        return str(num1 % num2)
    elif operation == 'div':
        return str(num1 / num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
