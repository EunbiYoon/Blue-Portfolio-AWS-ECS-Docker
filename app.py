from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/yml")
def text():
    return "CICD Working"

if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")