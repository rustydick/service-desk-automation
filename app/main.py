"""
Flask application that streams html content from G4F API
"""

import os
import flask
from flask_bootstrap import Bootstrap5
from flask_font_awesome import FontAwesome
from flask_babel import Babel, gettext, _
from app.config import Config


app = flask.Flask(__name__)
app.config.from_object(Config)


def get_locale():
    return flask.request.accept_languages.best_match(app.config["LANGUAGES"])


font_awesome = FontAwesome(app)
bootstrap = Bootstrap5(app)
babel = Babel(app, locale_selector=get_locale)


@app.get("/")
def index():
    return flask.render_template(
        "index.html",
        tasks=[
            {
                "id": "1",
                "hash": "26fc16c36e89c8d35bf635b57e6829dce33ae9bb",
                "title": "Add new feature",
                "message": "Add new feature",
                "time": "2021-10-10 10:10:10",
            },
            {
                "id": "2",
                "hash": "ef6b14dbf478dbb1a5151981073fa2dae196cc15",
                "title": "Fix bug",
                "message": "Fix bug",
                "time": "2021-10-10 10:10:10",
            },
            {
                "id": "3",
                "hash": "",
                "title": "Add new feature",
                "message": "Add new feature",
                "time": "2021-10-10 10:10:10",
            },
        ],
    )


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
