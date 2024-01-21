import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


@app.route("/")
def home():
    return render_template("index.html", session=session.get("user"))


@app.route("/diet-generator/")
def diet_generator():
    return render_template("diet-generator.html")


@app.route("/meal/")
def meal():
    return render_template("meal.html")


@app.route("/menus/")
def menu():
    return render_template("menu.html")


@app.route("/about-us/")
def about():
    return render_template("about-us.html")


@app.route("/contact-us/")
def contact():
    return render_template("contact-us.html")


@app.route("/privacy-policy/")
def privacy():
    return render_template("privacy-policy.html")


@app.route("/terms-of-service/")
def terms():
    return render_template("terms-of-service.html")


@app.route("/join/")
def join():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True), screen_hint="signup"
    )


@app.route("/login/")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for(
            "callback",
            _external=True,
        )
    )


@app.route("/callback/", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("http://127.0.0.1:3000")


@app.route("/logout/")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


@app.route("/new-user-info/")
def new_user_info():
    return render_template("new-user-info.html")


@app.route("/settings/")
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(env.get("PORT", 3000)))