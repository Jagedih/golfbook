from flask import Flask
from flask import session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash

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
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user == None:
        return False
    else:
        password = password.encode('utf-8')
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False

def getUserDetails():
    sql = "SELECT username, real_name, name FROM users INNER JOIN golf_clubs ON users.club = golf_clubs.id WHERE users.id=:userid"
    result = db.session.execute(sql, {"userid":user_id()})
    return result.fetchall()

def user_id():
    return session.get("user_id",0)

def logout():
    del session["user_id"]
