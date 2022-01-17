from flask import Flask, render_template, request
from batted_balls import Batted_Balls
from pagination import Pagination
import pandas as pd


app = Flask(__name__)

# routes
@app.route('/', defaults={'sort': 'GAME_DATE', 'is_asc': 'true', 'page': 0})
@app.route('/<sort>/<is_asc>/<int:page>')
def index(sort, is_asc, page):
    is_asc = convert_to_bool(is_asc) # is_asc is returned as string, convert to bool

    batted_balls = Batted_Balls().sort_by_column(sort, is_asc)

    page_data = {
    'batted_balls': batted_balls,
    'columns': Batted_Balls.usable_columns(),
    'pagination': Pagination(len(batted_balls.index), page),
    'sort': sort,
    'is_asc': is_asc
    }

    return render_template('index.html', data = page_data)

@app.route('/pitchers', defaults={'name': None, 'sort': 'GAME_DATE', 'is_asc': 'true'}, methods = ['GET', 'POST'])
@app.route('/pitchers/<name>/<sort>/<is_asc>')
def pitchers(name, sort, is_asc):
    is_asc = convert_to_bool(is_asc) # is_asc is returned as string, convert to bool

    batted_balls_by_pitcher = None

    if request.method == 'POST':
        name = request.form['pitcher']

    if name is not None:
        batted_balls = Batted_Balls().sort_by_column(sort, is_asc)
        batted_balls_by_pitcher = Batted_Balls().get_by_pitcher(name)


    page_data = {
    'batted_balls': batted_balls_by_pitcher,
    'columns': Batted_Balls.usable_columns(),
    'pitchers': Batted_Balls().get_pitchers(),
    'pitcher': name,
    'sort': sort
    }

    return render_template('pitchers.html', data = page_data)

@app.route('/batters', defaults={'name': None, 'sort': 'GAME_DATE', 'is_asc': 'true'}, methods = ['GET', 'POST'])
@app.route('/batters/<name>/<sort>/<is_asc>')
def batters(name, sort, is_asc):
    is_asc = convert_to_bool(is_asc) # is_asc is returned as string, convert to bool

    batted_balls_by_batter = None

    if request.method == 'POST':
        name = request.form['batter']

    if name is not None:
        batted_balls = Batted_Balls().sort_by_column(sort, is_asc)
        batted_balls_by_batter = Batted_Balls().get_by_batter(name)

    page_data = {
    'batted_balls': batted_balls_by_batter,
    'columns': Batted_Balls.usable_columns(),
    'batters': Batted_Balls().get_batters(),
    'batter': name,
    'sort': sort,
    }

    return render_template('batters.html', data = page_data)

@app.route('/matchups', defaults={'pitcher': None, 'batter': None, 'sort': 'GAME_DATE', 'is_asc': 'true'}, methods = ['GET', 'POST'])
@app.route('/matchups/<pitcher>/<batter>/<sort>/<is_asc>')
def matchups(pitcher, batter, sort, is_asc):
    is_asc = convert_to_bool(is_asc) # is_asc is returned as string, convert to bool

    batted_balls_by_matchup = None

    if request.method == 'POST':
        batter = request.form['batter']
        pitcher = request.form['pitcher']

    if batter is not None and pitcher is not None:
        batted_balls = Batted_Balls().sort_by_column(sort, is_asc)
        batted_balls_by_matchup = Batted_Balls().get_by_matchup(batter, pitcher)

    page_data = {
    'pitchers': Batted_Balls().get_pitchers(),
    'batters': Batted_Balls().get_batters(),
    'batted_balls': batted_balls_by_matchup,
    'columns': Batted_Balls.usable_columns(),
    'batter': batter,
    'pitcher': pitcher,
    'sort': sort
    }

    return render_template('matchups.html', data = page_data)

# helper functions

def convert_to_bool(string):
    if (string.lower() == 'true'):
        return True
    else:
        # TODO: throw error
        return False
