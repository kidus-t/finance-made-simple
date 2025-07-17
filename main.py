from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/budgeting")
def budgeting():
  return render_template("budgeting.html")

@app.route("/investing")
def investing():
  return render_template("investing.html")


@app.route("/info-graphics")
def info_graphic():
  return render_template("info-graphics.html")

if __name__ == "__main__":
  app.run()