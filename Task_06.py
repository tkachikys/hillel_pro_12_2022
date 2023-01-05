from flask import Flask, render_template
from utils import read_req
app = Flask(__name__)


@app.route("/")
def write_req():
    return read_req()


app.run(debug=True, port=12345)

