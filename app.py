from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'


@app.route('/event')
def event_page():
    return render_template("event.html")


@app.route('/')
def calendar_event():
    return render_template("calendar.html")


if __name__ == '__main__':
    app.run()
