from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(os.getcwd(), "events.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False) # 15 ставил от балды, фронтдендеру или дизайнеру надо поменять
    #description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    #locations = db.Column(db.String(50), nullable=True)
    #tags = db.Column(db.String(100), nullable=True)
    #period = db.Column(db.String(50), nullable=True)
    #duration = db.Column(db.String(50), nullable=True)
    start_datetime = db.Column(db.String(50), nullable=False)
    end_datetime = db.Column(db.String(50), nullable=False)
    #created_at = db.Column(db.String(50), nullable=True)
    #updated_at = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Events %r>' % self.id

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
    if request.method == "POST":
        name = request.form['name']
        category = request.form['category']
        status = request.form['status']
        start = request.form['start_datetime']
        end = request.form['end_datetime']

        calendar = Events(name=name, category=category, status=status, start_datetime=start, end_datetime=end)

        try:
            db.session.add(calendar)
            db.session.commit()
            return redirect("/calendar")
        except Exception as e:
            return f"An error occurred: {e}"

    else:
        return render_template("add_event.html")


if __name__ == "__main__":
    app.run(debug=True)