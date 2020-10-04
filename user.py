from flask import Flask
from flask import session
from db import db

def setRealName(realName):
    try:
        sql = "UPDATE users SET real_name=:realName WHERE username=:username"
        db.session.execute(sql, {"realName":realName, "username":getUserSessionId()})
        db.session.commit()
        return True
    except:
        return False

def setClub(clubName):
    try:
        sql = "UPDATE users SET club=:clubName  WHERE username=:username"
        db.session.execute(sql, {"clubName":clubName, "username":getUserSessionId()})
        db.session.commit()
        return True
    except:
        return False

def getUserProfile():
    sql = "SELECT username, real_name, club FROM users WHERE username=:userId"
    result = db.session.execute(sql, {"userId":getUserSessionId()})
    return result.fetchall()

def getFriends():
    sql = "SELECT DISTINCT user_id, friend_id from friendships INTERSECT SELECT friend_id, user_id from friendships WHERE user_id=:userId"
    result = db.session.execute(sql, {"userId":getUserSessionId()})
    return result.fetchall()

def addFriend(friendId):
    try:
        sql = "INSERT INTO friendships (user_id, friend_id) VALUES (:user_id,:friend_id)"
        db.session.execute(sql, {"user_id":getUserSessionId(),"friend_id":friendId})
        db.session.commit()
        return True
    except:
        return False

def isAdmin():
    sql = "SELECT admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":getUserSessionId()})
    status = result.fetchone()
    return status[0]

def getUserSessionId():
    return session.get("user_id",0)

def setUserSessionId(userid):
    session["user_id"] = userid
    
def logout():
    del session["user_id"]
