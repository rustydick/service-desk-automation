"""
Flask application that streams html content from G4F API
"""

import os
import flask
from flask_bootstrap import Bootstrap5
from flask_font_awesome import FontAwesome

app = flask.Flask(__name__)
font_awesome = FontAwesome(app)
bootstrap = Bootstrap5(app)


@app.get("/")
def index():
    return "ok"


@app.get("/login")
def login():
    return flask.render_template("login.html")


@app.post("/login")
def login_post():
    return "ok"


@app.get("/req")
def req():
    return flask.render_template("req.html")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8130))
    app.run(host="0.0.0.0", port=port, debug=True)
