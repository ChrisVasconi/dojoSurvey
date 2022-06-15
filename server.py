
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def form():
    return render_template("index.html")


@app.route("/results")
def results():
    return render_template("form.html")


@app.route("/process", methods=["post"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")


if __name__ == "__main__":
    app.run(debug=True)
