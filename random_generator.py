from flask import Flask, render_template, request, jsonify
import random
import statistics
from datetime import datetime

app = Flask(__name__)

class RandomNumberGenerator:
    def __init__(self):
        self.history = []  # Store generated numbers
        
    def generate_single(self, min_val, max_val):
        number = random.randint(min_val, max_val)
        self.history.append({
            'number': number,
            'timestamp': datetime.now(),
            'range': (min_val, max_val)
        })
        return number
    
    def generate_multiple(self, min_val, max_val, count):
        numbers = [random.randint(min_val, max_val) for _ in range(count)]
        self.history.append({
            'numbers': numbers,
            'timestamp': datetime.now(),
            'range': (min_val, max_val)
        })
        return numbers
    
    def get_statistics(self, numbers):
        if not numbers:
            return None
        return {
            'mean': statistics.mean(numbers),
            'median': statistics.median(numbers),
            'mode': statistics.mode(numbers),
            'range': max(numbers) - min(numbers)
        }

generator = RandomNumberGenerator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    min_val = int(data.get('min', 1))
    max_val = int(data.get('max', 100))
    count = int(data.get('count', 1))
    
    try:
        if count == 1:
            result = generator.generate_single(min_val, max_val)
            return jsonify({
                'number': result,
                'success': True
            })
        else:
            numbers = generator.generate_multiple(min_val, max_val, count)
            stats = generator.get_statistics(numbers)
            return jsonify({
                'numbers': numbers,
                'statistics': stats,
                'success': True
            })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        })

@app.route('/history')
def get_history():
    return jsonify(generator.history[-10:])  # Return last 10 generations

if __name__ == '__main__':
    app.run(debug=True)
Last edited 37 minutes ago


