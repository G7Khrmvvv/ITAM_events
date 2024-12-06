from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False) # 15 ставил от балды, фронтдендеру или дизайнеру надо поменять
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    locations = db.Column(db.String(50), nullable=True)
    tags = db.Column(db.String(100), nullable=True)
    period = db.Column(db.String(50), nullable=True)
    duration = db.Column(db.String(50), nullable=True)
    start_datetime = db.Column(db.String(50), nullable=False)
    end_datetime = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(50), nullable=True)
    updated_at = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Calendar %r>' % self.id

@app.route('/event')
def event_page():
    return render_template("event.html")


@app.route('/calendar')
def calendar_event():
    return render_template("calendar.html")


@app.route('/')
@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/add_event', methods=['POST', 'GET'])
def event_creation():
    if (request.method == "POST"):
        title = request.form['title'] # EDIT HEREEEEEEE
    else:
        return render_template("add_event.html")

if __name__ == '__main__':
    app.run()
