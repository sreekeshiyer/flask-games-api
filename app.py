from re import DEBUG
from flask import Flask, jsonify, request, Response
from store import games, add_game_to_DB


app = Flask(__name__)
app.config['DEBUG'] = True


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


@app.route('/games/add', methods=['POST'])
def add_game():
    data = request.get_json()
    try:
        title = data['title']
        hours = data['hours']
        if title and hours:
            data = add_game_to_DB(title, int(hours))
            return jsonify(data), 201
    except:
        return Response('''{"message": "Bad Request"}''', status=400, mimetype='application/json')
