from flask import Flask, render_template, request
from pymemcache.client import base
import os
  
import json

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
client = base.Client(('localhost', 11211))

@app.route('/')
def fib():
    result = request.args.get('number')
    if result:
        number = client.get(result)
        if number:
            return render_template('index.html', fib_number=number)
        fib1 = fib2 = 1
        n = int(result)
        if n == 0 or n == 1:
            return render_template('index.html', fib_number=n)
        while n > 0:
            fib1, fib2 = fib2, fib1 + fib2
            n -= 1
            client.set(result, str(fib2))
        return render_template('index.html', fib_number=fib2)
    return render_template('index.html', fib_number='Введите число')
#app.add_url_rule('/', 'fib', fib)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=port)                                                     