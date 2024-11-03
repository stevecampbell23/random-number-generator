from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    min_num = None
    max_num = None
    error = None
    
    if request.method == 'POST':
        try:
            min_num = int(request.form['min_num'])
            max_num = int(request.form['max_num'])
            
            if min_num >= max_num:
                error = "Maximum number must be greater than minimum number"
            else:
                result = random.randint(min_num, max_num)
        except ValueError:
            error = "Please enter valid numbers"
    
    return render_template('index.html', result=result, error=error, 
                         min_num=min_num, max_num=max_num)

if __name__ == '__main__':
    app.run(debug=True)