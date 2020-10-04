from db import db

def getClubNames():
    sql = "SELECT club_name FROM golf_clubs"
    names = db.session.execute(sql);
    return names.fetchall()

def addClub(name,address,number):
    try:
        sql = "INSERT INTO golf_clubs (club_name, address, phone_number) VALUES(:name, :address, :number)"
        db.session.execute(sql, {"name":name,"address":address,"number":number})
        db.session.commit()
        return True
    except:
        return False
