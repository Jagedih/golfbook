from flask import Flask
from db import db
def getPars(course):
    sql = "SELECT * FROM golf_courses WHERE name=:course"
    result = db.session.execute(sql, {"course":course})
    return result[3:22]

def getActiveCourses():
    sql = "SELECT * FROM golf_courses WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'});
    return result.fetchall()
