from flask import Flask
import random

app = Flask(__name__)

phrases = [
    "Фраза 1",
    "Фраза 2",
    "Фраза 3",
    "Фраза 4",
    "Фраза 5"
]

@app.route('/phrase')
def get_phrase():
    return random.choice(phrases)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)
