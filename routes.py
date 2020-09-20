from app import app
from flask import render_template, request, redirect
import users,courses

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if(users.login(username,password)):
            return render_template("index.html")
        else:
            return render_template("message.html",message="wrong username or password.")

@app.route("/signUp", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("signUp.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return render_template("/index.html")
        else:
            return render_template("message.html",message="Username already in use")

@app.route("/courses", methods=["GET"])
def listCourses():
    return render_template("courses.html", activeCourses = courses.getActiveCourses())

@app.route("/profile", methods=["GET"])
def profile():
    return render_template("profile.html", userDetails = users.getUserDetails())
