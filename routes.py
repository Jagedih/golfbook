from app import app
from flask import render_template, request, redirect
import user,courses,clubs,score,stats

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if(user.login(username,password)):
            return render_template("index.html")
        else:
            return render_template("login.html", message="wrong username or password.")

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/scores", methods=["GET","POST"])
def scores():
    if request.method == "GET":
        course_names = courses.get_active_course_names()
        return render_template("/scores.html", active_courses=course_names)
    if request.method == "POST":
        course_name = request.form["course"]
        hole_details = courses.get_course_hole_details(course_name)
        user_id = user.get_user_session_id()
        friends = user.get_friends()
        return render_template("/post_scores.html", course_name=course_name, hole_details = hole_details,user_id=user_id, friends=friends)

@app.route("/post_scores", methods=["GET","POST"])
def post_scores():
    if request.method == "POST":
        handicap = request.form["handicap"]
        course_name = request.form["course"]
        course_id = courses.get_active_course_id(course_name)[0]
        holes = courses.get_course_hole_ids(course_id)
        player = request.form["player"]
        putts = request.form.getlist("putt")
        strokes = request.form.getlist("score")
        played = request.form["played"]
        round_id = score.add_round(player, course_id, played, handicap)[0]
        for i in range(1,19):
            score.add_score_to_round(round_id,holes[i-1][0],strokes[i-1][0],putts[i-1][0])
        return render_template("index.html")

@app.route("/handicap_scores", methods=["GET"])
def handicap_scores():
    score_data = score.get_user_round_scores('true')
    return render_template("/past_scores.html", all_hole_scores=score_data)

@app.route("/practice_scores", methods=["GET"])
def practice_scores():
    score_data = score.get_user_round_scores('false')
    return render_template("/past_scores.html", all_hole_scores=score_data)

@app.route("/practice_stats", methods=["GET"])
def practice_stats():
    title = 'Practice round stats'
    round_amount = stats.get_round_amount('false')[0]
    avg_putting = stats.get_average_putting_score('false')[0]
    avg_shots = stats.get_round_shot_avg('false')[0]
    min_shots = stats.get_round_shot_min('false')[0]
    max_shots = stats.get_round_shot_max('false')[0]
    return render_template("/stats.html", round_amount=round_amount, title=title,
    avg_putting=avg_putting, avg_shots=avg_shots, max_shots=max_shots, min_shots=min_shots)

@app.route("/handicap_stats", methods=["GET"])
def handicap_stats():
    title = 'Handicap round stats'
    round_amount = stats.get_round_amount('true')[0]
    avg_putting = stats.get_average_putting_score('true')[0]
    avg_shots = stats.get_round_shot_avg('true')[0]
    min_shots = stats.get_round_shot_min('true')[0]
    max_shots = stats.get_round_shot_max('true')[0]
    return render_template("/stats.html", round_amount=round_amount, title=title,
    avg_putting=avg_putting, avg_shots=avg_shots, max_shots=max_shots, min_shots=min_shots)

@app.route("/sign_up", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("sign_up.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.register(username,password):
            return render_template("index.html")
        else:
            return render_template("sign_up.html", message="Username already in use/empty or password was not given")

@app.route("/courses", methods=["GET","POST"])
def course_data():
    if request.method == "GET":
        all_course_data = courses.get_course_details()
        if(all_course_data == None):
            all_course_data = [""]
        return render_template("courses.html", all_course_data=all_course_data, club_names=clubs.get_club_names(), user=user)

    if request.method == "POST":
        course_name = request.form['courseName']
        club_name = request.form['club']
        pars = request.form.getlist('par')
        lengths = request.form.getlist('length')

        if(user.is_admin()):
            courses.add_course(club_name, course_name, pars, lengths)
        return redirect("/courses")

@app.route("/edit_profile", methods=["GET","POST"])
def edit_profile():
    if request.method == "GET":
        return render_template("edit_profile.html", club_names=clubs.get_club_names())
    if request.method == "POST":
        club_name = request.form['club']
        real_name = request.form['name']
        user.set_real_name(real_name)
        user.set_club(club_name)
        return redirect("/profile")

@app.route("/profile", methods=["GET","POST"])
def profile():
    if request.method == "GET":
        friendlist = user.get_friends()
        if(friendlist == None):
            friendlist = [""]
        return render_template("/profile.html", user_data=user.get_user_profile(), friendlist=friendlist)
    if request.method == "POST":
        friend_name = request.form['friend']
        if(friend_name != user.get_user_session_id()):
            user.add_friend(friend_name)
        return redirect("/profile")

@app.route("/logout", methods=["GET"])
def logout():
    user.logout()
    return redirect("/")
