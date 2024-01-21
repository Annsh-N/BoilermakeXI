import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# SQL Database
#Import required dependencies
from google.cloud.sql.connector import Connector
import sqlalchemy
from sqlalchemy import text


# Function to get CloudSQL instance password from Secret Manager
def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})
    # Print the secret payload.
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    return payload

# Function call to get DB password ino a local varaiable
db_password = access_secret_version('vernal-landing-411806', 'campus-crunch','1')


# initialize Connector object
connector = Connector()

# function to return the database connection
def getconn():
    conn= connector.connect(
        "vernal-landing-411806:us-east1:campus-crunch",
        "pymysql",
        user="root",
        password=db_password,
        db="userData"
    )
    return conn
# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
with pool.connect() as db_conn:
    # Create Table
    #db_conn.execute(text("CREATE TABLE IF NOT EXISTS userInfo(email text,dietaryRestrictions text,likedFoods text,dislikedFoods text,weight integer,dietGoals text)"))

    #print("Done")

    #db_conn.execute("INSERT INTO userInfo VALUES ('test', 'test', 'test', 'test', 50, 'test')")

    result = db_conn.execute("SELECT * FROM userInfo").fetchall()

    for row in result:
        print(row)
def addToLikedFoods(email, food):
    with pool.connect() as db_conn:
        db_conn.execute(text(f"UPDATE userInfo SET likedFoods = CONCAT(likedFoods, ',{food}') WHERE email = '{email}'"))
def addToDislikedFoods(email, food):
    with pool.connect() as db_conn:
        db_conn.execute(text(f"UPDATE userInfo SET dislikedFoods = CONCAT(dislikedFoods, ',{food}') WHERE email = '{email}'"))
def addDietaryRestrictions(email, restriction):
    with pool.connect() as db_conn:
        db_conn.execute(text(f"UPDATE userInfo SET dietaryRestrictions = CONCAT(dietaryRestrictions, ',{restriction}') WHERE email = '{email}'"))
def setDietGoals(email, goal):
    with pool.connect() as db_conn:
        db_conn.execute(text(f"UPDATE userInfo SET dietGoals = '{goal}' WHERE email = '{email}'"))
def setWeight(email, weight):
    with pool.connect() as db_conn:
        db_conn.execute(text(f"UPDATE userInfo SET weight = {weight} WHERE email = '{email}'"))
def getLikedFoods(email):
    with pool.connect() as db_conn:
        result = db_conn.execute(text(f"SELECT likedFoods FROM userInfo WHERE email = '{email}'")).fetchall()
        return result[0][0].split(',')
def getDislikedFoods(email):
    with pool.connect() as db_conn:
        result = db_conn.execute(text(f"SELECT dislikedFoods FROM userInfo WHERE email = '{email}'")).fetchall()
        return result[0][0].split(',')
def getDietaryRestrictions(email):
    with pool.connect() as db_conn:
        result = db_conn.execute(text(f"SELECT dietaryRestrictions FROM userInfo WHERE email = '{email}'")).fetchall()
        return result[0][0].split(',')
def getDietGoals(email):
    with pool.connect() as db_conn:
        result = db_conn.execute(text(f"SELECT dietGoals FROM userInfo WHERE email = '{email}'")).fetchall()
        return result[0][0].split(',')
def getWeight(email):
    with pool.connect() as db_conn:
        result = db_conn.execute(text(f"SELECT weight FROM userInfo WHERE email = '{email}'")).fetchall()
        return result[0][0]


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
    return render_template("diet-generator/index.html")


@app.route("/diet-generator/meal/")
def meal():
    return render_template("diet-generator/meal.html")


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
    return redirect("/new-user-info/")


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
