import sqlite3


def createTable():
    con = sqlite3.connect('medicine_requests.db')
    cur = con.cursor()
    cur.execute(
        """ SELECT count(name) FROM sqlite_master WHERE type='table' AND name='medicines' """)
    if cur.fetchone()[0] == 0:
        cur.execute(""" CREATE TABLE medicines (
			medicine_name text,
			medicine_details text,
			full_name text,
			location text,
			phone_number text
			)""")


def dbSubmit(medicineName, medicineDetails, fullName, location, phoneNumber):
    con = sqlite3.connect('medicine_requests.db')
    cur = con.cursor()
    cur.execute("INSERT INTO medicines VALUES (:medicineName, :medicineDetails, :fullName, :location, :phoneNumber)",
                {
                    'medicineName': medicineName,
                    'medicineDetails': medicineDetails,
                    'fullName': fullName,
                    'location': location,
                    'phoneNumber': phoneNumber
                })
    con.commit()
    con.close()


def dbQuery(recordId=-1):
    con = sqlite3.connect('medicine_requests.db')
    cur = con.cursor()
    if(recordId == -1):
        cur.execute("SELECT *, oid FROM medicines")
    else:
        cur.execute("SELECT * FROM medicines WHERE oid = :recordId",
                    {'recordId': recordId})

    recordsList = cur.fetchall()
    con.commit()
    con.close()
    return recordsList


def dbDelete(recordId):
    con = sqlite3.connect('medicine_requests.db')
    cur = con.cursor()
    cur.execute("DELETE from medicines WHERE oid = " + recordId)
    con.commit()
    con.close()


def dbUpdate(medicineName, medicineDetails, fullName, location, phoneNumber, recordId):
    con = sqlite3.connect('medicine_requests.db')
    cur = con.cursor()
    cur.execute("""UPDATE medicines SET
			medicine_name = :medicineName,
			medicine_details = :medicineDetails,
			full_name = :fullName,
			location = :location,
			phone_number = :phoneNumber

			WHERE oid = :oid""",
                {
                    'medicineName': medicineName,
                    'medicineDetails': medicineDetails,
                    'fullName': fullName,
                    'location': location,
                    'phoneNumber': phoneNumber,
                    'oid': recordId
                })
    con.commit()
    con.close()
