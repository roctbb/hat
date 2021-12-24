from flask import Flask, render_template, request
import random

words = []

app = Flask(__name__)

def init():
    global words
    with open('words.txt') as file:
        words = file.read().split('\n')

@app.route('/')
def index():
    return render_template('hat.html')

@app.route('/remove', methods=['POST'])
def remove_word():
    word = request.json.get('word')
    if word and word in words:
        words.remove(word)

    return 'ok'


@app.route('/get')
def get_word():
    if words:
        return random.choice(words)
    return "слова закончились"

@app.route('/restart')
def restart():
    init()
    return 'ok'

init()
app.run(host='0.0.0.0', port=3456, debug=True)