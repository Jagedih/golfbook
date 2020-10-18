from db import db
import user

def get_user_round_scores(is_handicap):
    sql = "SELECT name, hole, par, strokes, putts, date_played FROM golf_courses AS g"\
     " LEFT JOIN holes AS h ON h.course_id = g.id"\
     " LEFT JOIN rounds AS r ON r.course = g.id"\
     " LEFT JOIN scores AS s ON s.round_id = r.id AND s.hole_id = h.id"\
     " WHERE r.player=:username AND r.handicap=:is_handicap ORDER BY date_played,hole"
    result = db.session.execute(sql, {"username":user.get_user_session_id(),"is_handicap":is_handicap})
    return result.fetchall()

def add_round(player_name, course_id, date, handicap):
    try:
        sql = "INSERT INTO rounds (player,course,date_played, handicap) "\
        "VALUES (:player_name,:course_id,:date, :handicap) RETURNING id"
        round_id = db.session.execute(sql, {"player_name":player_name,"course_id":course_id,"date":date,"handicap":handicap})
        db.session.commit()
        return round_id.fetchone()
    except:
        return False

def add_score_to_round(round_id,hole_id,strokes,putts):
    try:
        sql = "INSERT INTO scores (round_id,hole_id,strokes,putts) "\
        "VALUES (:round_id,:hole_id,:strokes,:putts)"
        db.session.execute(sql, {"round_id":round_id,"hole_id":hole_id,"strokes":strokes,"putts":putts})
        db.session.commit()
        return True
    except:
        return False
