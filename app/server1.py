from flask import Flask
import random
import llama2

app = Flask(__name__)

# Initialize llama2
llama = llama2.Llama()

@app.route('/phrase')
def get_phrase():
    # Generate a phrase using llama2
    phrase = llama.generate_phrase()
    return phrase

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5051)
