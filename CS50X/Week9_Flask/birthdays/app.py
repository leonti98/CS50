import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        if not name:
            return redirect("/")
        birthday = request.form.get("birthday")
        if not birthday:
            return redirect("/")
        year, month, day = birthday.split("-")

        db.execute("INSERT INTO birthdays (name, month, day, year) VALUES(?, ?, ?, ?)", name, int(month), int(day), int(year))
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.form.get("id")
    new_name = request.form.get("editName")
    new_date = request.form.get("editBirthday")
    if new_name and new_name != db.execute("SELECT name FROM birthdays WHERE id = ?", id):
        db.execute("UPDATE birthdays SET name = ? WHERE id = ?", new_name, id)
    if new_date:
        try:
            year, month, day = new_date.split("-")
            year = int(year)
            if year > 2024:
                raise ValueError()
            month = int(month)
            day = int(day)
        except:
            pass
        db.execute("UPDATE birthdays SET day = ?, month = ?, year = ? WHERE id = ?", day, month, year, id)

    return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    id = request.form.get("id")
    db.execute("DELETE FROM birthdays WHERE id = ?", id)

    return redirect("/")
