from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main/")
def main():
    return render_template("main.html")

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
    return render_template("join.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/settings/")
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(debug=True)
