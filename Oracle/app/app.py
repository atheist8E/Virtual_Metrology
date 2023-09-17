import os
import json
import flask
import click
import sqlite3

database_path = ".\\resource\\"

app = flask.Flask(__name__)
app.config["DATABASE"] = os.path.join(database_path, "database.db")

#################################################### DataBase ####################################################

def init_db():
    db = get_db()
    with flask.current_app.open_resource(os.path.join(database_path, "schema.sql")) as f:
        db.executescript(f.read().decode("utf-8"))

def get_db():
    if "db" not in flask.g:
        flask.g.db = sqlite3.connect(flask.current_app.config["DATABASE"], detect_types = sqlite3.PARSE_DECLTYPES)
        flask.g.db.row_factory = sqlite3.Row
    return flask.g.db

def close_db():
    db = flask.g.pop("db", None)
    if db is not None:
        db.close()

@app.cli.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the Database")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

#################################################### Utils ####################################################

def get_history():
    my_db = get_db()
    cur = my_db.execute("SELECT * FROM ANALYSIS_HISTORY")
    history = [json.dumps(dict((cur.description[i][0], value) for i, value in enumerate(row))) for row in cur.fetchall()]
    # print(history)
    print(history[0])
    print(history[1])
    return history

def insert_data(request):
    columns = [
        "line_id",
        "process_id",
        "current_step",
        "start_step",
        "duration_start",
        "duration_end",
        "cpo",
        "area",
        "distance",
        "mark_type",
    ]
    my_db = get_db()
    my_db.execute("INSERT INTO ANALYSIS_HISTORY ({}) VALUES ({})".format(','.join(columns), ','.join(['?' for _ in range(len(columns))])),
        (
            request.form["LineID"],
            request.form["ProcessID"],
            request.form["CurrentStep"],
            request.form["StartStep"],
            request.form["DurationStart"],
            request.form["DurationEnd"],
            request.form["CPO"],
            request.form["Area"],
            request.form["Distance"],
            request.form["MarkType"])
    )
    my_db.commit()

#################################################### Rendering ####################################################

@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def home():
    return flask.render_template('home.html')

@app.route('/analysis_multiple', methods = ['GET', 'POST'])
def analysis_multiple():
    if flask.request.method == "POST":
        insert_data(flask.request)
    history = get_history()
    return flask.render_template('analysis_multiple.html', history = history)



if __name__ == "__main__":

    app.run(debug = True)
