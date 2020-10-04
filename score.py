from db import db

def getUserScores(username):
    sql = "SELECT strokes, putts, id from scores LEFT JOIN rounds ON rounds.id = scores.round_id WHERE player=:username"
    result = db.session.execute(sql, {"username":getUserSessionId()})
    return result.fetchall()

def addRound(playerName, courseId, date):
    try:
        sql = "INSERT INTO rounds (player,course,date_played) VALUES (:playerName,:courseId,:date) RETURNING id"
        roundId = db.session.execute(sql, {"playerName":playerName,"courseId":courseId,"date":date})
        db.session.commit()
        return roundId.fetchone()
    except:
        return False

def addHoleScoreToRound(roundId,holeId,strokes,putts):
    try:
        sql = "INSERT INTO scores (round_id,hole_id,strokes,putts) VALUES (:roundId,:holeId,:strokes,:putts)"
        db.session.execute(sql, {"roundId":roundId,"holeId":holeId,"strokes":strokes,"putts":putts})
        db.session.commit()
        return True
    except:
        return False
