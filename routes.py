from app import app
from flask import render_template, request, redirect
import user,users,courses,clubs,score

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
            return render_template("login.html", message="wrong username or password.")

@app.route("/scores", methods=["GET","POST"])
def scores():
    if request.method == "GET":
        courseNames = courses.getActiveCourseNames()
        return render_template("/scores.html", activeCourses = courseNames)
    if request.method == "POST":
        courseName = request.form["course"]
        holeDetails = courses.getCourseHoleDetails(courseName)
        userId = user.getUserSessionId()
        friends = user.getFriends()
        return render_template("/postScores.html", courseName = courseName, holeDetails = holeDetails,userId=userId, friends=friends )

@app.route("/postScores", methods=["GET","POST"])
def postScores():
    if request.method == "POST":
        courseName = request.form["course"]
        courseId = courses.getActiveCourseIdByName(courseName)[0]
        holeIds = courses.getCourseHoleIds(courseId)
        player = request.form["player"]
        putts = request.form.getlist("putt")
        strokes = request.form.getlist("score")
        played = request.form["played"]
        roundId = score.addRound(player, courseId, played)[0]
        for i in range(1,19):
            score.addHoleScoreToRound(roundId,holeIds[i-1][0],strokes[i-1][0],putts[i-1][0])
        return render_template("index.html")

@app.route("/signUp", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("signUp.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return render_template("index.html")
        else:
            return render_template("signUp.html", message="Username already in use/empty or password was not given")

@app.route("/courses", methods=["GET","POST"])
def renderCourses():
    if request.method == "GET":
        allCourseData = courses.getAllCourseDetails()
        if(allCourseData == None):
            allCourseData = [""]
        return render_template("courses.html", allCourseData = allCourseData, clubNames = clubs.getClubNames(), user = user)

    if request.method == "POST":
        courseName = request.form['courseName']
        clubName = request.form['club']
        pars = request.form.getlist('par')
        lengths = request.form.getlist('length')

        if(user.isAdmin()):
            courses.addCourse(clubName, courseName, pars, lengths)
        return redirect("/courses")

@app.route("/editProfile", methods=["GET","POST"])
def editProfile():
    if request.method == "GET":
        return render_template("editProfile.html", clubNames = clubs.getClubNames())
    if request.method == "POST":
        clubName = request.form['club']
        realName = request.form['name']
        user.setRealName(realName)
        user.setClub(clubName)
        return redirect("/profile")



@app.route("/profile", methods=["GET","POST"])
def profile():
    if request.method == "GET":
        friendlist = user.getFriends()
        if(friendlist == None):
            friendlist = [""]
        return render_template("/profile.html", userData = user.getUserProfile(), friendlist = friendlist)

    if request.method == "POST":
        friendName= request.form['friend']
        user.addFriend(friendName)
        return redirect("/profile")

@app.route("/asdf", methods=["GET","POST"])
def logout():
    user.logout()
    return "good bye"
