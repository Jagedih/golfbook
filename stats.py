from db import db
import user

def get_round_amount(is_it_handicap):
    sql = "SELECT COUNT (id) FROM rounds WHERE player=:username AND handicap=:handicap"
    result = db.session.execute(sql, {"username":user.get_user_session_id(),"handicap":is_it_handicap})
    return result.fetchone()

def get_average_putting_score(is_it_handicap):
    sql = "SELECT ROUND(AVG (putts),1) FROM scores AS s LEFT JOIN rounds as r "\
    "ON r.id = s.round_id WHERE player=:username AND handicap=:handicap"
    result = db.session.execute(sql, {"username":user.get_user_session_id(),"handicap":is_it_handicap})
    return result.fetchone()

def get_round_shot_avg(is_it_handicap):
    sql = "SELECT round(avg(s),0) FROM (SELECT SUM(strokes) AS s FROM scores "\
    "LEFT JOIN rounds ON rounds.id = scores.round_id WHERE player=:username "\
    "AND handicap=:handicap GROUP BY scores.round_id)sumtable"

    result = db.session.execute(sql, {"username":user.get_user_session_id(),"handicap":is_it_handicap})
    return result.fetchone()

def get_round_shot_max(is_it_handicap):
    sql = "SELECT round(max(s),0) FROM (SELECT SUM(strokes) AS s from scores "\
    "LEFT JOIN rounds ON rounds.id = scores.round_id WHERE player=:username "\
    "AND handicap=:handicap GROUP BY scores.round_id)sumtable"

    result = db.session.execute(sql, {"username":user.get_user_session_id(),"handicap":is_it_handicap})
    return result.fetchone()

def get_round_shot_min(is_it_handicap):
    sql = "SELECT round(min(s),0) FROM (SELECT SUM(strokes) AS s from scores "\
    "LEFT JOIN rounds ON rounds.id = scores.round_id WHERE player=:username "\
    "AND handicap=:handicap GROUP BY scores.round_id)sumtable"

    result = db.session.execute(sql, {"username":user.get_user_session_id(),"handicap":is_it_handicap})
    return result.fetchone()
