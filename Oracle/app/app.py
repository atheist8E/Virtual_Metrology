import os
import click
import sqlite3
from flask.cli import with_appcontext
from flask import Flask, render_template, redirect, request, current_app, g


app = Flask(__name__)

def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"], detect_types = sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the Database")

def get_history():
    history = list()
    my_db = get_db()
    cur = my_db.execute("SELECT * FROM HISTORY")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/analysis_multiple', methods = ['GET', 'POST'])
def analysis_multiple():
    if request.method == "POST":
        line_id = request.form["LineID"]
        process_id = request.form["ProcessID"]

        current_step = request.form["CurrentStep"]
        start_step = request.form["StartStep"]

        duration_start = request.form["DurationStart"]
        duration_end = request.form["DurationEnd"]

        cpo = request.form["CPO"]
        area = request.form["Area"]

        distance = request.form["Distance"]
        mark_type = request.form["MarkType"]

        print(request.form)

    return render_template('analysis_multiple.html')



if __name__ == "__main__":
    app.run(debug = True)
