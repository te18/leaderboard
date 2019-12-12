# te18/leaderboard
# https://github.com/te18/leaderboard

from flask import Flask, render_template

app = Flask(__name__)

# error handlers
@app.errorhandler(400)
def error_400(e):
    return render_template("errors/400.html"), 400

@app.errorhandler(404)
def error_404(e):
    return render_template("errors/404.html"), 400

@app.errorhandler(500)
def error_500(e):
    return render_template("errors/500.html"), 500


# main routes
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")