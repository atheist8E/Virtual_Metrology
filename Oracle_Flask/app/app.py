import os
import click
import sqlite3
from flask import Flask, render_template, redirect, request, current_app, g
from flask.cli import with_appcontext


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

@app.route('/query', methods = ['GET', 'POST'])
def query():
    #my_db = db.get_db()
    #history = get_history()
    if request.method == "POST":
        print(request.form)
        line_id = request.form["LineID"]
        print(line_id)
        process_id = request.form["ProcessID"]
        print(process_id)
        photo_step = request.form["PhotoStep"]
        print(photo_step)
        photo_time = request.form["PhotoTime"]
        print(photo_time)
        overlay_step = request.form["OverlayStep"]
        print(overlay_step)
        overlay_time = request.form["OverlayTime"]
        print(overlay_time)
        photo_eqp = request.form["Photo EQP"]
        print(photo_eqp)
        lot_id = request.form["LotID"]
        print(lot_id)

        #cur = my_db.execute("SELECT * FROM ALIGNMENT_DRIVEN_DEFECT WHERE ~")
        #rows = cur.fetchone()
        # return render_template('query.html', 
        #                     accumulated_wafer_map = accumulated_wafer_map_file, 
        #                     alignment_wafer_map = alignment_wafer_map_file, 
        #                     overlay_wafer_map = overlay_wafer_map_file,
        #                     history = history)
    #return render_template('query.html', history = history)
    return render_template('query.html')



if __name__ == "__main__":
    app.run(debug= True)
