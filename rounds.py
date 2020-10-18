from db import db

def get_user_rounds(username):
    sql = "SELECT"
    result = db.session.execute(sql,{"userId":getUserSessionId()})
    return result.fetchall()
