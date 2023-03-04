from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    engineers = get_shows()

    return render_template('index.html', shows = shows)

@app.route('/success', methods=['POST'])
def submit():
    show = request.form['show']
    add_show(show)

    return render_template('success.html')

def add_show(show):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO shows(shows) VALUES (?)", (show))
    conn.commit()
    conn.close()

def get_all_shows():
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM shows")
    engineers = []

    for row in result: 
        show = {
            'show': row[0],
        }
        shows.append(shows)

    conn.close()
    return shows

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')