from flask import Flask, jsonify
from games import games

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'greeting': 'Hello World!'
    })


@app.route('/games')
def all_games():
    return jsonify({
        'games': games,
    })


@app.route('/games/<game_id>')
def find_game_by_id(game_id):
    for game in games:
        if game["id"] == int(game_id):
            return jsonify({
                "game": game,
            })
