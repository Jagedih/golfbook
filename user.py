from flask import Flask
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def set_real_name(real_name):
    try:
        sql = "UPDATE users SET real_name=:real_name WHERE username=:username"
        db.session.execute(sql, {"real_name":real_name, "username":get_user_session_id()})
        db.session.commit()
        return True
    except:
        return False

def set_club(club_name):
    try:
        sql = "UPDATE users SET club=:club_name  WHERE username=:username"
        db.session.execute(sql, {"club_name":club_name, "username":get_user_session_id()})
        db.session.commit()
        return True
    except:
        return False

def get_user_profile():
    sql = "SELECT username, real_name, club FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":get_user_session_id()})
    return result.fetchall()

def get_friends():
    sql = "SELECT DISTINCT user_id, friend_id from friendships INTERSECT SELECT friend_id, user_id from friendships WHERE user_id=:userId"
    result = db.session.execute(sql, {"userId":get_user_session_id()})
    return result.fetchall()

def add_friend(friend_id):
    try:
        sql = "INSERT INTO friendships (user_id, friend_id) VALUES (:user_id,:friend_id)"
        db.session.execute(sql, {"user_id":get_user_session_id(),"friend_id":friend_id})
        db.session.commit()
        return True
    except:
        return False

def is_admin():
    sql = "SELECT admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":get_user_session_id()})
    status = result.fetchone()
    return status[0]

def get_user_session_id():
    return session.get("user_id",0)

def register(username,password):
    hashedpw = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
        db.session.execute(sql, {"username":username,"password":hashedpw})
        db.session.commit()
    except:
        return False
    return login(username,password)

def login(username,password):
    sql = "SELECT password, username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            set_user_session_id(user[1])
            return True
        else:
            return False

def set_user_session_id(userid):
    session["user_id"] = userid

def logout():
    del session["user_id"]
