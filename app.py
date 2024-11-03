from flask import Flask, render_template, request, jsonify
import random
import statistics
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'No JSON data received', 'success': False}), 400
            
        min_val = int(data.get('min', 1))
        max_val = int(data.get('max', 100))
        count = int(data.get('count', 1))
        
        if count == 1:
            result = random.randint(min_val, max_val)
            return jsonify({
                'number': result,
                'success': True
            })
        else:
            numbers = [random.randint(min_val, max_val) for _ in range(count)]
            stats = {
                'mean': statistics.mean(numbers),
                'median': statistics.median(numbers),
                'mode': statistics.mode(numbers) if len(set(numbers)) < len(numbers) else numbers[0],
                'range': max(numbers) - min(numbers)
            }
            return jsonify({
                'numbers': numbers,
                'statistics': stats,
                'success': True
            })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
Last edited 1 hour ago


