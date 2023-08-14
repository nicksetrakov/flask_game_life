from flask import Flask, render_template
from game_of_life import *


app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(20, 20)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html',
                           life=game
                           )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
