from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)  # 'age' 키에 대한 값만 반환

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/gwangun', methods=['GET'])
def yoooo():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return str(random.randint(1,10))


if __name__ == '__main__':
    app.run(debug=True)