from db import db

def get_course_hole_details(course_name):
    sql = "SELECT hole,par,length,name FROM holes LEFT JOIN golf_courses ON golf_courses.id = holes.course_id WHERE golf_courses.name=:course_name AND expired=:status"
    result = db.session.execute(sql, {"course_name":course_name, "status":'false'})
    return result.fetchall()

def get_course_details():
    sql = "SELECT name,club_name,address FROM golf_courses LEFT JOIN golf_clubs ON golf_clubs.club_name = golf_courses.club WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'})
    return result.fetchall()

def get_course_name(course_id):
    sql = "SELECT name from golf_courses WHERE id=:course_id"
    result = db.session.execute(sql, {"courseId":courseId})
    return result.fetchone()

def get_course_club(course_id):
    sql = "SELECT club from golf_courses WHERE id=:course_id"
    result = db.session.execute(sql, {"course_id":course_id})
    return result.fetchone()

def get_active_course_id(name):
    sql = "SELECT id FROM golf_courses WHERE name=:name AND expired=:status"
    result = db.session.execute(sql, {"name":name, "status":'false'})
    return result.fetchone()

def get_active_course_names():
    sql = "SELECT name FROM golf_courses WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'})
    return result.fetchall()

def get_all_course_ids():
    sql = "SELECT id FROM golf_courses WHERE expired=:status"
    result = db.session.execute(sql, {"status":'false'})
    return result.fetchall()

def get_course_hole_ids(course_id):
    sql = "SELECT id FROM holes WHERE course_id=:course_id"
    result = db.session.execute(sql, {"course_id":course_id})
    return result.fetchall()

def get_course_length(course_id):
    sql = "SELECT SUM (length) FROM holes LEFT JOIN golf_courses on golf_courses.id = holes.course_id WHERE course_id =:course_id"
    result = db.session.execute(sql, {"course_id":course_id})
    return result.fetchone()

def add_course(club_name, course_name, pars, lengths):
    try:
        sql = "INSERT INTO golf_courses (club, name) VALUES (:club_name, :course_name) RETURNING id"
        courseId = db.session.execute(sql, {"club_name":club_name,"course_name":course_name})
        db.session.commit()
        courseId = courseId.fetchone()

        for hole in range(1,19):
            add_hole_to_course(courseId[0], hole, int(pars[hole-1]), int(lengths[hole-1]))
        return True
    except:
        return False

def add_hole_to_course(courseId, holeNumber, par, length):
    try:
        sql = "INSERT INTO holes (course_id, hole, par, length) VALUES (:courseId, :holeNumber, :par, :length)"
        db.session.execute(sql, {"courseId":courseId,"holeNumber":holeNumber,"par":par, "length":length})
        db.session.commit()
        return True
    except:
        return False
