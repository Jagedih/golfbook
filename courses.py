from db import db

def getCourseHoleDetails(courseName):
    sql = "SELECT hole,par,length,name FROM holes LEFT JOIN golf_courses ON golf_courses.id = holes.course_id WHERE golf_courses.name=:courseName AND expired=:status"
    result = db.session.execute(sql, {"courseName":courseName, "status":'false'})
    return result.fetchall()

def getAllCourseDetails():
    sql = "SELECT name,club_name,address FROM golf_courses LEFT JOIN golf_clubs ON golf_clubs.club_name = golf_courses.club WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'})
    return result.fetchall()

def getCourseName(courseId):
    sql = "SELECT name from golf_courses WHERE id=:courseId"
    result = db.session.execute(sql, {"courseId":courseId})
    return result.fetchone()

def getCourseClub(courseId):
    sql = "SELECT club from golf_courses WHERE id=:courseId"
    result = db.session.execute(sql, {"courseId":courseId})
    return result.fetchone()

def getActiveCourseIdByName(name):
    sql = "SELECT id FROM golf_courses WHERE name=:name AND expired=:status"
    result = db.session.execute(sql, {"name":name, "status":'false'})
    return result.fetchone()

def getActiveCourseNames():
    sql = "SELECT name FROM golf_courses WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'})
    return result.fetchall()

def getActiveCourseIds():
    sql = "SELECT id FROM golf_courses WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'})
    return result.fetchall()

def getCourseHoleIds(courseId):
    sql = "SELECT id FROM holes WHERE course_id=:courseId"
    result = db.session.execute(sql, {"courseId":courseId})
    return result.fetchall()

def getCourseLength(courseId):
    sql = "SELECT SUM (length) FROM holes LEFT JOIN golf_courses on golf_courses.id = holes.course_id WHERE course_id =:courseId"
    result = db.session.execute(sql, {"courseId":courseId})
    return result.fetchone()

def addCourse(clubName, courseName, pars, lengths):
    try:
        sql = "INSERT INTO golf_courses (club, name) VALUES (:clubName, :courseName) RETURNING id"
        courseId = db.session.execute(sql, {"clubName":clubName,"courseName":courseName})
        db.session.commit()
        courseId = courseId.fetchone()

        for hole in range(1,19):
            addHoleToCourse(courseId[0], hole, int(pars[hole-1]), int(lengths[hole-1]))
        return True
    except:
        return False

def addHoleToCourse(courseId, holeNumber, par, length):
    try:
        sql = "INSERT INTO holes (course_id, hole, par, length) VALUES (:courseId, :holeNumber, :par, :length)"
        db.session.execute(sql, {"courseId":courseId,"holeNumber":holeNumber,"par":par, "length":length})
        db.session.commit()
        return True
    except:
        return False
