from db import db
import user
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
    sql = "SELECT password, username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    details = result.fetchone()

    if user == None:
        return False
    else:
        if check_password_hash(details[0],password):
            user.set_user_session_id(details[1])
            return True
        else:
            return False
