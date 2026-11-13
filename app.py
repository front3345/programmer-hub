from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    db = sqlite3.connect("programmers_v2.db")
    db.cursor().execute("""
        CREATE TABLE IF NOT EXISTS programmers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birth_date TEXT,
        language TEXT,
        experience INTEGER,
        framework TEXT
        )
    """)
    db.commit()
    db.close()

@app.route("/")
def home():
    db = sqlite3.connect("programmers_v2.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("SELECT * FROM programmers")
    programmers = cursor.fetchall()
    db.close()
    return render_template("index.html", programmers=programmers)

@app.route("/add", methods=['POST'])
def add():
    name = request.form["name"]
    birth_date = request.form["birth_date"]
    language = request.form["language"]
    experience = request.form["experience"]
    framework = request.form["framework"]
    
    db = sqlite3.connect("programmers_v2.db")
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO programmers (name, birth_date, language, experience, framework) 
        VALUES (?, ?, ?, ?, ?)
    """, (name, birth_date, language, experience, framework))
    db.commit()
    db.close()
    
    return redirect(/)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
