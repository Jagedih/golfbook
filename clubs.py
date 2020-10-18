from db import db

def get_club_names():
    sql = "SELECT club_name FROM golf_clubs"
    names = db.session.execute(sql);
    return names.fetchall()

def add_club(name,address,number):
    try:
        sql = "INSERT INTO golf_clubs (club_name, address, phone_number) VALUES(:name, :address, :number)"
        db.session.execute(sql, {"name":name,"address":address,"number":number})
        db.session.commit()
        return True
    except:
        return False
