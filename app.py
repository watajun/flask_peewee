from flask import Flask
from flask import render_template
from database import Post
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create():
    name = request.form["postName"]
    title = request.form["postTitle"]
    body = request.form["postBody"]
    Post.create(name="Keisuke", title="Title", body="Body")
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
