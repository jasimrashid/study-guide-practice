# web_app/routes/home_routes.py
from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from models.models import BoardGame, db, parse_records
# from web_app.models import User
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return 'Hello World!'
    # return render_template("prediction_form.html", screen_names=screen_names)

    # PRINT RECORDS FROM DATABASE

@home_routes.route("/add/<game_id>")
def fetch_and_add(game_id=None):

    # FETCH DATA FROM BGG API

    # STORE GAME DATA INTO DB
    # parse into objects > store into db
    db_game = BoardGame(game_id = game_id)
    db_game.name = 'game1'
    db_game.minplayers = 1
    db_game.maxplayers = 2
    db_game.playingtime = 10
    db_game.description = 'game1'

    breakpoint()
    
    db.session.add(db_game)
    db.session.commit()
    

@home_routes.route("/hello")
def hello():
    x = 2 + 2
    return f"About me {x}"