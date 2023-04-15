from flask import Flask, render_template, redirect, request
import sqlite3


# Configure application
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/benefit')
def benefit():
    return render_template('benefit.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/day')
def day():
    return render_template('day.html')


@app.route('/why')
def why():
    return render_template('why.html')


@app.route('/form', methods=["GET"])
def show_form():
    return render_template("form.html")


@app.route('/submit', methods=["POST"])
def form():
    # Połącz się z bazą danych SQLite
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()

    # pobranie danych z formularza
    name = request.form['name']
    gender = request.form['q1']
    danced_before = request.form['q2']
    how_often = request.form['q3']
    encouraged = request.form['q4']
    planning = request.form['q5']

    # wprowadzenie danych do bazy danych
    c.execute("INSERT INTO survey (name, gender, danced_before, how_often, encouraged, planning) VALUES (?, ?, ?, ?, ?, ?)", (name, gender, danced_before, how_often, encouraged, planning))
    conn.commit()
    # przekierowanie do strony z potwierdzeniem wysłania formularza
    conn.close()

    return redirect("/thanks")
    ## return redirect(url_for("thanks"))


@app.route("/results")
def results():
    return render_template("results.html")

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')



if __name__ == '__main__':
    app.run(debug=True)