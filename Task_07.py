from flask import Flask, render_template
from calc import height, weight


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Home_page.html", title="")


@app.route("/avr_data")
def get_avr_data():
    return render_template("students.html", title="Students weight and height", weight=weight, height=height)


app.run(debug=True, port=50000)
