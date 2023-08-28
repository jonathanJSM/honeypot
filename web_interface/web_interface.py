# web_interface.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    attack_count = 50  # Replace with actual attack count
    return render_template('index.html', attack_count=attack_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
